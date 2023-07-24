# Using newer versions of python may cause errors
# The .i file will need to be more advanced to include libraries, including default
# Video demonstrations:
#  https://www.youtube.com/watch?v=Dct-sVGXvic
#  https://www.youtube.com/watch?v=YhAFOBcSoLw
#  https://www.youtube.com/watch?v=0Btpe8ED-20
# Problem with newer versions of python:
#  https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa
# About using pyd file type
#  Another StackOverflow source mentioned why to use .pyd instead of .dll; could not find source again.
#  https://stackoverflow.com/questions/50278029/how-to-import-a-pyd-file-as-a-python-module
# For certain C++ standard library:
#  https://www.swig.org/Doc2.0/Library.html#Library_stl_cpp_library
python_loc = C:\Users\coder\AppData\Local\Programs\Python\Python39
python_lib = python39
python_version = 3.9

standard:
	swig -c++ -python example.i
	g++ -shared -o _example.pyd example.cpp example_wrap.cxx -I$(python_loc)\include -L$(python_loc)\libs -l$(python_lib)
	py -$(python_version) hello.py

clean:
	del _example.pyd
	del example_wrap.cxx
	del example.py
