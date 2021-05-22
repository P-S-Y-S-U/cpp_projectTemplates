cmake_minimum_required(VERSION <version>)
project(<project_name>)
set(CMAKE_CXX_STANDARD <cmake_std>)

# CMAKE C & CXX FLAGS SETUP

# PROJECT VARS SETUP
set(PROJECT_BIN     "bin")
set(PROJECT_LIB     "lib")
set(PROJECT_ARCHIVE "lib/static")
set(_EXPORT_PREFIX "Project_S_Export")
set(PROJECT_INSTALL ${CMAKE_INSTALL_PREFIX})

# PROJECT CMAKE SCRIPT REQUIREMENTS (Dependencies cmake script)#

# CONAN SETUP #
include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# Additional cmake scripts in sub-directory #
