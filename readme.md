# C++ and Python Examples

The code in these modules illustrate how to build C++ so that it can be called with functions using two methods: `ctypes` and swig. Both make use of g++ and mingw32-make and currently require that the PATH is properly configured using mingw or whatever folders contain the tools and files necessary for C++.

Note on python version: Python version 3.8, (according to 2nd source in hack), removed the current working directory and the path from the search for DLLs. This causes the code to naturally break for newer versions, as the C++ standard library DLL is not included. Thus, it needs to be added in. Following advice in https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa, have added the bin folder for mingw to the include path, which includes the DLL libstdc++-6.dll on my machine.

Note: Two other DLLs are also built into the DLLs created by the Makefiles. However, these are apparently already included by default.

Additionally, note that the above functionality was taken out for security reasons.

## `ctypes`

This utilizes the standard Python module `ctypes`. To build and illustrate the program, navigate to the ctypes folder and run 

```
mingw32-make
```

Currently, some of the functionality of the included C++ code is broken.

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

### Advantages
* Allows conversion of C/C++ to many languages with only minor alterations to the build process (mainly changing one flag and potentially the output file type)
* Once set up, is relatively easy to use
* Implements most of function overloading
* Is (apparently) fully set up for C

### Disadvantages
* Can be difficult to set up
* Documentation is not plentiful
* While full coverage of the standard C++ library is underway, it is apparently not complete
* In function overloading, does not distinguish between datatypes of the same general group. For example, does not distinguish between int and long (will just discard one of them)

# Sources
* For a discussion about swig vs ctypes, see https://stackoverflow.com/questions/135834/python-swig-vs-ctypes

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
* For how to include (parts of the) C++ standard library:
    * https://www.swig.org/Doc2.0/Library.html#Library_stl_cpp_library
* For how overloading is handled:
    * https://www.swig.org/Doc4.1/SWIGPlus.html#SWIGPlus_nn25

## For ctypes:
* https://www.youtube.com/watch?v=b1E-4EZJ9OU for code
* The documentation for ctypes (module) included with Python 3.9.5

## For hack to get it working on newer versions of python
* For making it work in python 3.9, got info/functions from:
    * https://www.reddit.com/r/learnpython/comments/wmd9ry/python_unable_to_load_dll_filenotfounderror_but/
    * https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-find-module-libvlc-dll/59016932#59016932 (most helpful)
    * https://github.com/python/cpython/issues/93094
    * https://www.reddit.com/r/learnpython/comments/ntb5f7/ctypes_library_isnt_working_with_c_code/
    * https://stackoverflow.com/questions/74524163/wrapping-an-external-c-library-with-swig-not-finding-standard-libraries
    * https://stackoverflow.com/questions/68298520/python-filenotfounderror-using-module-ctypes-and-cdll
    * See also source above (https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa)
* For how to view the DLL dependencies
    * https://stackoverflow.com/questions/7378959/how-to-check-for-dll-dependency