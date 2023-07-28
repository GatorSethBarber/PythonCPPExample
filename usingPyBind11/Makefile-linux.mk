# For compilation statement: https://stackoverflow.com/questions/60699002/how-can-i-build-manually-c-extension-with-mingw-w64-python-and-pybind11
# Official compilation resource: https://pybind11.readthedocs.io/en/stable/compiling.html
# For tutorial: https://www.youtube.com/watch?v=_5T70cAXDJ0
# Official documentation to get pybind11: https://pybind11.readthedocs.io/en/stable/installing.html
# For getting include path for python: Answer by Robᵩ in https://stackoverflow.com/questions/35071192/how-to-find-out-where-the-python-include-directory-is
# For finding problems with makefile: https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop

standard:
	g++ -shared -o buildLinux/example$$(python3-config --extension-suffix) example.cpp pybinds.cpp -I../extern/pybind11/include/  $$(python3-config --includes) -fPIC
	python3 testLinux.py test