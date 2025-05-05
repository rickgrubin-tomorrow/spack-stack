
import os
import sys

from spack.package import *

class ConvertGeotiff(AutotoolsPackage):
    """A small commandline utility for converting data from GeoTIFF to geogrid format used by WRF."""

    homepage = "http://www.openwfm.org/"
    url = "https://github.com/openwfm/convert_geotiff/archive/refs/tags/v0.1.tar.gz"
    maintainers("rickgrubin-tomorrow")

    license("unlicense")

    version("0.1",
        sha256="0629c656f734b6036538aef8202a189e0f3464bcc28c5d5bc3f5c83609ae0e8c",
        url="https://github.com/openwfm/convert_geotiff/archive/refs/tags/v0.1.tar.gz",
    )

    depends_on("c", type="build")

    patch("v01.patch")

    depends_on("libtiff")
    depends_on("libgeotiff")
    depends_on("netcdf-c")

    requires(
        "%gcc",
        "%intel",
        "%oneapi",
        policy="one_of",
        msg="convert_geotiff supports only the GCC and Intel compilers",
    )

    def setup_run_environment(self, env):
        env.set("WRFDA_HOME", self.prefix)
        env.append_path("PATH", self.prefix.main)
        env.append_path("PATH", self.prefix.tools)

    def setup_build_environment(self, env):
        spec = self.spec

        ldflags = []
        tiff = spec["libtiff"]
        geotiff = spec["libgeotiff"]
        ldflags.append(tiff.prefix.lib)
        ldflags.append(geotiff.prefix.lib)

        netcdfc = spec["netcdf-c"]
        env.set("NETCDF", netcdfc.prefix)
