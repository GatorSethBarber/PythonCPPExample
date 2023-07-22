# C++ and Python Examples

The code in these modules illustrate how to build C++ so that it can be called with functions using two methods: `ctypes` and swig. Both make use of g++ and mingw32-make.

## `ctypes`

This utilizes the standard Python module `ctypes`. To build and illustrate the program, navigate to the ctypes folder and run 

```
mingw32-make
```

### Advantages

* Uses a standard Python library
* When using C, can directly call the functions by name
* Can call most system dlls.

### Disadvantages
* Requires user to write glue-code
* When using C++, must use `extern "C"` or names will be lost to name mangling

## swig

This is a 3rd party program that allows C/C++ to be built to a large number of languages, including Python. Before running the Makefile, perform the following steps:

1. Install Python 3.6 (more work needs to be done before later versions can be used) and make sure `py` runs from the comamnd line
2. In the Makefile, set the value of `python_loc` to be the location where that version of Python is installed.
3. Install swig (used verison 4.0.2) and add it to PATH.

To build and run a test program, run
```
mingw32-make
```

To remove all created files (including those needed for the test program hello.py), run
```
mingw32-make clean
```

# Sources

## For swig
* Various documentation/tutorials provided in the download for swig and on https://www.swig.org, the official site.
* Video demonstrations:
    * https://www.youtube.com/watch?v=Dct-sVGXvic
    * https://www.youtube.com/watch?v=YhAFOBcSoLw
    * https://www.youtube.com/watch?v=0Btpe8ED-20
* Problem with newer versions of python:
    * https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa
* About using pyd file type
    * Another StackOverflow source mentioned why to use .pyd instead of .dll; could not find source again.
    * https://stackoverflow.com/questions/50278029/how-to-import-a-pyd-file-as-a-python-module
* *Programming Python* by Mark Lutz contains a section on SWIG.

## For ctypes:
* https://www.youtube.com/watch?v=b1E-4EZJ9OU for code
* The documentation for ctypes (module) included with Python 3.9.5
