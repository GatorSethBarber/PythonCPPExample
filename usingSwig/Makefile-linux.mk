# Using newer versions of python may cause errors
# The .i file will need to be more advanced to include libraries, including default
# Video demonstrations:
#  https://www.youtube.com/watch?v=Dct-sVGXvic
#  https://www.youtube.com/watch?v=YhAFOBcSoLw
#  https://www.youtube.com/watch?v=0Btpe8ED-20
# For certain C++ standard library:
#  https://www.swig.org/Doc2.0/Library.html#Library_stl_cpp_library
# For getting include path for python: Answer by Robᵩ in https://stackoverflow.com/questions/35071192/how-to-find-out-where-the-python-include-directory-is
# For finding problems with makefile: https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop
pythonInc = $$(python3-config --includes)

standard:
	swig -c++ -python example.i
	g++ -shared -o _example.so example.cpp example_wrap.cxx $(pythonInc) -fPIC
	python3 helloLinux.py

clean:
	rm _example.so
	rm example_wrap.cxx
	rm example.py
