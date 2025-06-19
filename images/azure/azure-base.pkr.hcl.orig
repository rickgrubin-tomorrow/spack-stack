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

source "azure-arm" "ubuntu-2004-hb120rsv3" {
  client_id = "${var.client_id}"
  client_secret = "${var.client_secret}"
  tenant_id = "ead7805b-3ab5-4c45-bc8b-b2c957dff611"
  subscription_id = "${var.subscription_id}"
  managed_image_name = "Azure-Base-u2004-hb120rsv3-{{timestamp}}"
  managed_image_resource_group_name = "${var.resource_group}"

  os_type = "Linux"
  # Let's build an Ubuntu image.
  #microsoft-dsvm:ubuntu-hpc:2004:20.04.2023080201
  image_publisher = "microsoft-dsvm"
  image_offer = "ubuntu-hpc"
  image_sku = "2004"

  location = "East US"
  vm_size = "Standard_HB120rs_v3"
  # We need enough space to upgrade, to install the Intel compilers, and to build the Spack packages.
  os_disk_size_gb = 100
}
source "azure-arm" "ubuntu-2204-hb120rsv3" {
  client_id = "${var.client_id}"
  client_secret = "${var.client_secret}"
  tenant_id = "ead7805b-3ab5-4c45-bc8b-b2c957dff611"
  subscription_id = "${var.subscription_id}"
  managed_image_name = "Azure-Base-u2204-hb120rsv3-{{timestamp}}"
  managed_image_resource_group_name = "${var.resource_group}"

  os_type = "Linux"
  # Let's build an Ubuntu image.
  #microsoft-dsvm:ubuntu-hpc:2204:22.04.2023080201
  image_publisher = "microsoft-dsvm"
  image_offer = "ubuntu-hpc"
  image_sku = "2204"

  # AlmaLinux's provider charges for use of the images. Upstream JCSDA develops on Ubuntu,
  # so we're fine with that for the dev cluster.
  #almalinux:almalinux-hpc:8_5-hpc-gen2:latest
  #image_publisher = "almalinux"
  #image_offer = "almalinux-hpc"
  #image_sku = "8_5-hpc-gen2"

  location = "East US"
  vm_size = "Standard_HB120rs_v3"
  # We need enough space to upgrade, to install the Intel compilers, and to build the Spack packages.
  os_disk_size_gb = 100

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
    "source.azure-arm.ubuntu-2004-hb120rsv3",
    "source.azure-arm.ubuntu-2204-hb120rsv3"
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
      "rm -rf /tmp/etc"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # Ubuntu 20.04 base packages
  provisioner "shell" {
    only = ["azure-arm.ubuntu-2004-hb120rsv3"]
    inline         = [
      "umask 022",
      "export DEBIAN_FRONTEND=noninteractive",
      "echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections",
      "wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null",
      "echo \"deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main\" | sudo tee /etc/apt/sources.list.d/oneAPI.list",
      "sudo apt-get update",
      "sudo apt-get upgrade -y",
      "sudo apt-get install -y autoconf automake build-essential ca-certificates cmake cmake-curses-gui curl diffutils gcc-10 gfortran-10 g++-10 git git-lfs gnupg libcurl4-openssl-dev locales ninja-build patch perl pipx pkg-config subversion tzdata vim-nox",
      "sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 50",
      "sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 50",
      "sudo update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-10 50",
      "sudo apt-get install -y intel-basekit-2023.2.0 intel-hpckit-2023.2.0 intel-basekit-2024.0 intel-hpckit-2024.0"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # Ubuntu 22.04 base packages
  provisioner "shell" {
    only = ["azure-arm.ubuntu-2204-hb120rsv3"]
    inline         = [
      "umask 022",
      "export DEBIAN_FRONTEND=noninteractive",
      "echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections",
      "wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null",
      "echo \"deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main\" | sudo tee /etc/apt/sources.list.d/oneAPI.list",
      "sudo apt-get update",
      "sudo apt-get upgrade -y",
      "sudo apt-get install -y autoconf automake build-essential ca-certificates cmake cmake-curses-gui curl diffutils gcc gfortran g++ gcc-11 gcc-12 g++-11 g++-12 gfortran-11 gfortran-12 git git-lfs gnupg libcurl4-openssl-dev locales ninja-build patch perl pipx pkg-config subversion tzdata vim-nox",
      "sudo apt-get install -y intel-basekit-2023.2.0 intel-hpckit-2023.2.0 intel-basekit-2024.0 intel-hpckit-2024.0"
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
      "sudo mkdir -p /stacks"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # saml2aws
  provisioner "shell" {
    inline         = [
      "umask 022",
      "mkdir -p /tmp/saml2aws",
      "wget -c https://github.com/Versent/saml2aws/releases/download/v2.36.12/saml2aws_2.36.12_linux_amd64.tar.gz -O - | tar -C /tmp/saml2aws -xzv",
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

  provisioner "shell" {
    inline         = [
      "sudo /usr/sbin/waagent -force -deprovision+user && export HISTSIZE=0 && sync"
    ]
    inline_shebang = "/bin/sh -x"
  }
}

