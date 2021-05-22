from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

# class <pak_name>Conan(ConanFile): #
class Conan(ConanFile):
    name = ""
    version = ""
    license = ""
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {'shared':[True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = [""] # src files export list #

    @property
    def _is_msvsc(self):
        return self.settings.os == 'Windows'
    
    @property
    def _is_linux(self):
        return self.settings.os == 'linux'

    def source(self):
        # url = <source_url>
        # sha256 = <file_hash>
        tools.get(url=f'', sha256='')

    def configure_cmake(self):
        cmake = CMake(self)

        # CMAKE DEFINITIONS #
        cmake.definitions['BUILD_SHARED_LIBS'] = 'ON' if self.options.shared == True else 'OFF'
        
        cmake.configure(source_folder=f'', build_folder= f'{self.build_folder}/build' )
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
        
    def package_info(self):
        self.cpp_info.libs = [''] # link library list #
        self.output.info(f'LIBS : {self.cpp_info.libs}')