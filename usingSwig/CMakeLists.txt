cmake_minimum_required(VERSION 3.18)

#See https://stackoverflow.com/questions/31038963/how-do-you-rename-a-library-filename-in-cmake for proper
# way to change name.
# See also:
#  https://stackoverflow.com/questions/65626613/assigning-output-name-based-on-c-header-file-and-cmake-command
# For add_dependencies: 
#  https://stackoverflow.com/questions/24614624/in-cmake-how-can-i-make-a-target-depend-on-another-target
# See CMake documentation

project(testingSwig)

add_custom_target(swigStuff
	COMMAND swig -c++ -python ../example.i
)
set_target_properties(swigStuff PROPERTIES PREFIX "")
set_target_properties(swigStuff PROPERTIES SUFFIX "")
set_target_properties(swigStuff PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)

add_library(example SHARED example.cpp ${PROJECT_SOURCE_DIR}/example_wrap.cxx)

add_dependencies(example swigStuff)

set_target_properties(example PROPERTIES PREFIX "_")
set_target_properties(example PROPERTIES SUFFIX ".pyd")

target_include_directories(example PUBLIC C:/Users/coder/AppData/Local/Programs/Python/Python311/include)
target_link_libraries(example C:/Users/coder/AppData/Local/Programs/Python/Python311/libs/python311.lib)
