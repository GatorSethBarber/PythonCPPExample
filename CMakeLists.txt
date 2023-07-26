cmake_minimum_required(VERSION 3.18)
# https://www.youtube.com/watch?v=_5T70cAXDJ0
project(example)

add_subdirectory(extern/pybind11)

pybind11_add_module(example ../example.cpp ../pybinds.cpp)