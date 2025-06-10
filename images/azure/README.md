# Packaging instructions to create an Azure image

1. Login to azure if you haven't already:
   ```az login --scope https://graph.microsoft.com//.default```
2. Create a service principal with az ad sp create-for-rbac and output the credentials that Packer needs:
   ```az ad sp create-for-rbac --role Contributor --scopes /subscriptions/<subscription_id> --query "{ client_id: appId, client_secret: password, tenant_id: tenant }"```
3. Customize `user.pkr.hcl.template` as `user.pkr.hcl`.
4. Build the base image: `packer build -var-file=user.pkr.hcl azure-base.pkr.hcl`. Take a note of the resulting image id.
5. Modify `azure-spack.pkr.hcl` as needed around line 41 (`custom_managed_image_name`) with the base image id.
6. Build the spack image: `packer build -var-file=user.pkr.hcl azure-spack.pkr.hcl`.
7. Take a note of the image that was produced on Azure. Update the image id used on the CycleCloud cluster.


# Known issues / TODOs

- The base image does not provide Slurm. Unsure where this gets added to the CycleCloud Ubuntu image.
- A default installation of Cylc is not provided. Users can do this themselves.
- JupyterHub is not installed. Eventually, it should be installed and configured for user logons with Slurm-based launchers.
- matplotlib has some conflicts with setuptools, and this causes mpl_toolkits to not provide an __init__.py occasionally when one is needed. We may need to patch.
