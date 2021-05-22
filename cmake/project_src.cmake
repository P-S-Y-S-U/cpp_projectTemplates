# project files src files list #
set(PROJECT_SRC_FILES )

# library & executable config #
add_library(<lib_name> <SHARED|STATIC> ${PROJECT_SRC_FILES})
target_include_directories(<lib_name> PUBLIC    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
                                                $<INSTALL_INTERFACE:include>
                                                ${DEPENDENCIES_INCLUDE_DIR}) # not needed for conan #
target_link_libraries(<lib_name> <PUBLIC|PRIVATE> ${CONAN_TARGETS})                                                


# cmake install config #
install(TARGETS <targets>   EXPORT ${_EXPORT_PREFIX}
                            RUNTIME DESTINATION ${PROJECT_BIN}
                            LIBRARY DESTINATION ${PROJECT_LIB}
                            ARCHIVE DESTINATION ${PROJECT_ARCHIVE}
)

install(DIRECTORY ${PROJECT_SOURCE_DIR}/include DESTINATION ${PROJECT_INSTALL}/include)