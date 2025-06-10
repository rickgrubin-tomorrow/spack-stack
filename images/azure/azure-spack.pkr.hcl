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

source "azure-arm" "ubuntu-2204-hb120rsv3" {
  client_id = "${var.client_id}"
  client_secret = "${var.client_secret}"
  tenant_id = "ead7805b-3ab5-4c45-bc8b-b2c957dff611"
  subscription_id = "${var.subscription_id}"
  managed_image_name = "tomorrow-stack-1.6.0-ubuntu-22.04-{{timestamp}}"
  managed_image_resource_group_name = "${var.resource_group}"

  os_type = "Linux"

  # Let's customize our Azure-base image
  custom_managed_image_name = "Azure-Base-u2204-hb120rsv3-1707340845"
  custom_managed_image_resource_group_name = "${var.resource_group}"

  #ManagedImageResourceGroupName: hpc-poc
  #ManagedImageName: MyTestImage-1698868765
  #ManagedImageId: /subscriptions/32144b4b-8247-427b-b803-3b5b76ab6895/resourceGroups/hpc-poc/providers/Microsoft.Compute/images/MyTestImage-1698868765
  #ManagedImageLocation: East US

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
    "source.azure-arm.ubuntu-2204-hb120rsv3"
  ]

  # Profile customizations: get more recent fixes from when the base image was applied.
  provisioner "file" {
    source = "etc"
    destination = "/tmp"
  }
  provisioner "shell" {
    inline         = [
      "umask 022",
      "sudo cp /tmp/etc/profile.d/90-intel-warning-suppression.sh /etc/profile.d/",
      "rm -rf /tmp/etc"
    ]
    inline_shebang = "/bin/sh -x"
  }

  # Stack loads
  provisioner "file" {
    source = "stacks"
    destination = "/tmp"
  }

  # Spack installation
  provisioner "shell" {
    inline         = [
      "umask 022",
      "sudo mkdir -p /stacks/climacell",
      "sudo mkdir -p /stacks/views/1.6.0/skylab",
      "sudo chown -R `whoami`:`id -g -n` /stacks",
      "cp -r /tmp/stacks/loads /stacks/loads",
      "rm -rf /tmp/stacks",
      "mkdir -p /tmp/mirror",
      "ssh-keyscan github.com >> ~/.ssh/known_hosts",
      "git clone --recursive -b tomorrow/release/1.6.0 git@github.com:climacell/spack-stack.git /stacks/climacell/1.6.0",
      ". /stacks/climacell/1.6.0/setup.sh",
      ". /opt/intel/oneapi/setvars.sh",
      ". /opt/intel/oneapi/compiler/2023.2.0/env/vars.sh",
      "spack stack create env --name 1.6.0 --site tomorrow-azure-ubuntu-2204 --template tomorrow-nwp-azure",
      "cd /stacks/climacell/1.6.0/envs/1.6.0",
      "spack env activate -p /stacks/climacell/1.6.0/envs/1.6.0",
      "spack compiler list",
      "spack concretize -f -U > log.conc",
      "spack mirror create -a -d /tmp/mirror",
      "spack mirror add local-image /tmp/mirror",
      "spack install",
      "spack view -d no symlink -i /stacks/views/1.6.0/skylab fv3-jedi mpas-jedi soca oops ioda ufo saber vader",
      "spack view -d yes symlink -i /stacks/views/1.6.0/ufs/atm/2023-03 ufs-weather-model",
      "spack clean -dsf",
      "spack mirror rm local-image",
      "sudo chown -R 0:0 /stacks",
      "rm -rf /tmp/mirror"
    ]
    inline_shebang = "/bin/bash -e"
  }


  provisioner "shell" {
    inline         = [
      "sudo /usr/sbin/waagent -force -deprovision+user && export HISTSIZE=0 && sync"
    ]
    inline_shebang = "/bin/sh -x"
  }
}

