from conans import ConanFile, CMake, tools

# <pak_name>Conan(ConanFile) #
class Conan(ConanFile):
    name = ""
    version = ""
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        # url = <source_url>
        # sha256 = <file_hash>
        tools.get(url=f'', sha256='')

    def build(self):
        print("Nothing to Build")

    def package(self):
        print("Installs in Package")
        # Package steps #
        
    def package_info(self):
        print("Package Info header only lib")

    def package_id(self):
        self.info.header_only()        