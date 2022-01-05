

add_cython_target(_core _core.pyx CXX)
add_library(_core MODULE _core)
python_extension_module(_core)

install(TARGETS _core LIBRARY DESTINATION .)