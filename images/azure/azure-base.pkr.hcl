packer {
  required_plugins {
    azure = {
      source  = "github.com/hashicorp/azure"
      version = "~> 2"
    }
  }
}

variable "subscription_id" {
  type    = string
}

variable "resource_group" {
  type    = string
}

variable "gallery_name" {
  type = string
}

variable "client_id" {
  type = string
}

variable "client_secret" {
  type = string
}

source "azure-arm" "ubuntu-2204-Standard_D4ds_v5" {
  client_id = "${var.client_id}"
  client_secret = "${var.client_secret}"
  tenant_id = "ead7805b-3ab5-4c45-bc8b-b2c957dff611"
  subscription_id = "${var.subscription_id}"
  managed_image_name = "Azure-Base-u2204-Standard_D4ds_v5-{{timestamp}}"
  managed_image_resource_group_name = "${var.resource_group}"

  os_type = "Linux"
  # Let's build an Ubuntu image.
  #microsoft-dsvm:ubuntu-hpc:2204:22.04.2023080201
  image_publisher = "microsoft-dsvm"
  image_offer = "ubuntu-hpc"
  image_sku = "2204"

  location = "East US"
  vm_size = "Standard_HB120rs_v3"
  # We need enough space to upgrade, to install the Intel compilers, and to build the Spack packages.
  os_disk_size_gb = 200

  #shared_image_gallery_destination {
  #  subscription = "${var.subscription_id}"
  #  resource_group = "${var.resource_group}"
  #  gallery_name = "${var.gallery_name}"
  #  image_name = "MyTestImage-{{timestamp}}"
  #  image_version = "1.0.0"
  #  replication_regions = ["East US"]
  #}
}

build {
  name = "base-ubuntu"
  sources = [
    "source.azure-arm.ubuntu-2204-Standard_D4ds_v5",
  ]

  # Profile customizations
  provisioner "file" {
    source = "etc"
    destination = "/tmp"
  }
  provisioner "shell" {
    inline         = [
      "umask 022",
      "sudo cp /tmp/etc/profile.d/90-intel-warning-suppression.sh /etc/profile.d/",
      "sudo cp /tmp/etc/profile.d/90-openmp-thread-sanity.sh /etc/profile.d/",
      "sudo rm -rf /tmp/etc"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # Ubuntu 22.04 base packages
  provisioner "shell" {
    only = ["azure-arm.ubuntu-2204-Standard_D4ds_v5"]
    inline         = [
      "umask 022",
      "export DEBIAN_FRONTEND=noninteractive",
      "echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections",
      "sudo apt update -y",
      "sudo apt install -y software-properties-common",
      "sudo apt upgrade -y",
      "sudo apt install -y gpg gnupg2 pkg-config build-essential",

      "sudo apt install -y autoconf automake autopoint build-essential ca-certificates cmake cmake-curses-gui curl"
      "sudo apt install -y diffutils environment-modules gcc-12 g++-12 gfortran-12 git git-lfs",
      "sudo apt install -y libdb5.3 libdb5.3-dev libtool-bin libcurl4-openssl-dev libkrb5-dev locales ninja-build",
      "sudo apt install -y patch perl pipx pkgconf snapd sphinx subversion tcl tcl-dev tcl-expect tzdata vim-nox wget ",

      # future: update-alternatives
      # update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 100
      # update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 100
      # update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-12 100

      # future: install lua / Lmod
      #   remove install of environment-modules if installing lua / lmod
      # Install lua/lmod manually because apt only has older versions
      # that are not compatible with the modern lua modules spack produces
      # https://lmod.readthedocs.io/en/latest/030_installing.html#install-lua-x-y-z-tar-gz
      "mkdir -p /opt/lua/5.1.4.9/src && cd $_",
      "wget https://sourceforge.net/projects/lmod/files/lua-5.1.4.9.tar.bz2",
      "tar -xvf lua-5.1.4.9.tar.bz2",
      "cd lua-5.1.4.9",
      "./configure --prefix=/opt/lua/5.1.4.9 2>&1 | tee log.config",
      "make VERBOSE=1 2>&1 | tee log.make",
      "make install 2>&1 | tee log.install",
 
      cat << 'EOF' >> /etc/profile.d/02-lua.sh",
      # Set environment variables for lua
      "export PATH=\"/opt/lua/5.1.4.9/bin:$PATH\"",
      "export LD_LIBRARY_PATH=\"/opt/lua/5.1.4.9/lib:$LD_LIBRARY_PATH\"",
      "export CPATH=\"/opt/lua/5.1.4.9/include:$CPATH\"",
      "export MANPATH=\"/opt/lua/5.1.4.9/man:$MANPATH\"",
      "EOF",

      "source /etc/profile.d/02-lua.sh",
      "mkdir -p /opt/lmod/8.7/src",
      "cd /opt/lmod/8.7/src",
      "wget https://sourceforge.net/projects/lmod/files/Lmod-8.7.tar.bz2",
      "tar -xvf Lmod-8.7.tar.bz2",
      "cd Lmod-8.7",
      # Note the weird prefix, lmod installs in PREFIX/lmod/X.Y automatically
      "./configure --prefix=/opt/ --with-lmodConfigDir=/opt/lmod/8.7/config 2>&1 | tee log.config",
      "make install 2>&1 | tee log.install",
      "ln -sf /opt/lmod/lmod/init/profile /etc/profile.d/z00_lmod.sh",
      "ln -sf /opt/lmod/lmod/init/cshrc /etc/profile.d/z00_lmod.csh",
      "ln -sf /opt/lmod/lmod/init/profile.fish /etc/profile.d/z00_lmod.fish",

      "sudo mkdir -p /etc/apt/keyrings",
      "wget -qO - https://dvc.org/deb/iterative.asc | gpg --dearmor -o /etc/apt/keyrings/packages.iterative.gpg",
      "echo \"deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.iterative.gpg] https://dvc.org/deb/ stable main\" | sudo tee /etc/apt/sources.list.d/dvc.list",
      "sudo chmod 644 /etc/apt/keyrings/packages.iterative.gpg /etc/apt/sources.list.d/dvc.list",
      "sudo apt install -y dvc",

      "sudo apt autoremove -y",

      "sudo sed -i 's/^[^#]/#&/' /etc/environment-modules/modulespath",
      "sudo sed -i '/module use/s/^/#/' /etc/environment-modules/initrc",
      "sudo echo \"module use /usr/share/modules/modulefiles\" | tee -a /etc/environment-modules/initrc",
      "sudo echo \"module use /opt/modulefiles/oneapi\" | tee -a /etc/environment-modules/initrc",
      "sudo echo \". /etc/environment-modules/initrc\" | tee -a /etc/profile.d/modules.sh",

      "sudo wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB -P /etc/apt/trusted.gpg.d/",
      "sudo apt-key add /etc/apt/trusted.gpg.d/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB",
      "sudo rm -f /etc/apt/trusted.gpg.d/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB",

      "sudo echo \"deb https://apt.repos.intel.com/oneapi all main\" | tee -a /etc/apt/sources.list.d/oneAPI.list",
      "sudo add-apt-repository -y \"deb https://apt.repos.intel.com/oneapi all main\"",
      "sudo apt install -y intel-basekit-2024.2 intel-basekit-runtime-2024.2 intel-basekit-env-2024.2 intel-hpckit-2024.2 intel-hpckit-runtime-2024.2 intel-hpckit-env-2024.2",
      "sudo /opt/intel/oneapi/modulefiles-setup.sh --output-dir=/opt/modulefiles/oneapi --ignore-latest",
    ]
    inline_shebang = "/bin/sh -x"
  }

  # Base package installations
  provisioner "shell" {
    inline         = [
      "umask 022",
      "export DEBIAN_FRONTEND=noninteractive",
      "curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash",
      "curl -sL https://aka.ms/downloadazcopy-v10-linux | tar -xz --exclude=NOTICE.txt --strip=1",
      "sudo cp azcopy /usr/local/bin/azcopy",
      "curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip",
      "unzip awscliv2.zip",
      "sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli",
      #"sudo mkdir -p /stacks"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # saml2aws
  provisioner "shell" {
    inline         = [
      "umask 022",
      "mkdir -p /tmp/saml2aws",
      "wget -c https://github.com/Versent/saml2aws/releases/download/v2.36.19/saml2aws_2.36.19_linux_amd64.tar.gz -O - | tar -C /tmp/saml2aws -xzv",
      "sudo cp /tmp/saml2aws/saml2aws /usr/local/bin/saml2aws",
      "sudo chmod 755 /usr/local/bin/saml2aws",
      "rm -rf /tmp/saml2aws"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # Mamba and pipx-provided packages
  provisioner "shell" {
    inline         = [
      "umask 022",
      "sudo PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install 'dvc[azure,s3,ssh]'",
      "curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba",
      "sudo cp bin/micromamba /usr/local/bin/micromamba",
      "sudo MAMBA_ROOT_PREFIX=/opt/mamba ./bin/micromamba create -n cylc -c conda-forge -y cylc-flow cylc-uiserver pipx"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # The cylc hub server is left unprovisioned for now. Getting conda and systemd to play nicely together is
  # a work in progress. Users can still spawn local servers.

  #provisioner "shell" {
  #  inline         = [
  #    "sudo /usr/sbin/waagent -force -deprovision+user && export HISTSIZE=0 && sync"
  #  ]
  #  inline_shebang = "/bin/sh -x"
  #}
}

