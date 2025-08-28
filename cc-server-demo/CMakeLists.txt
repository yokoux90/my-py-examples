cmake_minimum_required(VERSION 3.28)

project(cc-server-demo)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB_RECURSE H_FILES "${CMAKE_CURRENT_SOURCE_DIR}/include/*.h")
file(GLOB_RECURSE CC_FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cc")

find_package(Drogon CONFIG REQUIRED)

include_directories("${CMAKE_CURRENT_SOURCE_DIR}/include")

add_executable(${PROJECT_NAME} ${H_FILES} ${CC_FILES})
target_link_libraries(${PROJECT_NAME} PRIVATE Drogon::Drogon)