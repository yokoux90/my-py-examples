cmake_minimum_required(VERSION 3.28)

project(
    "cc_module_demo" 
    VERSION 0.1.0 
    DESCRIPTION "A C++ 20 Module Demo"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# GCC
# add_compile_options(-fmodules-ts)
# Clang
# add_compile_options(-fmodules -fcxx-modules)
# MSVC
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zf")

# Linux
# add_compile_options(-fmodules-ts)
# Clang
# add_compile_options(-fmodules)

set(MOD_NAME "cc_module")
# Dynamic Libary Output Directory
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
# Static Libary Output Directory
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
# Executable File Output Directory
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Project CPP Source Files
file(GLOB_RECURSE CC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")
# Module Source Files
file(GLOB_RECURSE M_I_FILES "${CMAKE_CURRENT_SOURCE_DIR}/module/*.ixx")
# file(GLOB_RECURSE M_CC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/module/*.cpp")

add_library(${MOD_NAME} STATIC ${M_I_FILES})
set_target_properties(${MOD_NAME} PROPERTIES OUTPUT_NAME ${MOD_NAME} LINKER_LANGUAGE CXX)

target_sources(
    ${MOD_NAME}
    PUBLIC 
    FILE_SET CXX_MODULES 
    TYPE CXX_MODULES
    FILES ${M_I_FILES}
)

add_executable(${PROJECT_NAME} ${CC_FILES})
target_link_libraries(${PROJECT_NAME} PRIVATE ${MOD_NAME})
