# C++ and Python Examples

The code in these modules illustrate how to build C++ so that it can be called with functions using two methods: `ctypes` and swig. Both make use of g++ and mingw32-make and currently require that the PATH is properly configured using mingw or whatever folders contain the tools and files necessary for C++.

Note on operating system: Tested on Windows and Ubuntu

## Setting up for local python version

Python version 3.8, (according to 2nd source in hack), removed the current working directory and the path from the search for DLLs for security reasons. This causes the code to naturally break for newer versions of python on Windows, as the C++ standard library DLL is not included. Thus, if using Windows, it needs to be added in. Following advice in https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa, I have added the bin folder for mingw to the include path where necessary, which includes the DLL libstdc++-6.dll on my machine. Two other DLLs are also built into the DLLs created by the Makefiles. However, these are standard Windows dlls.

The actual versions of Python used were 3.11 for Windows and 3.10 for Ubuntu Linux (apparently, the current default). To change these, replace the appropriate directory and specifications in the make and cmake files that need to be ran. This editing usually boils down to just changing the numbers to agree with the version. For example, if running (64-bit) Python 3.9 on Windows, just change occurrences of python311 to python39 and 3.11 to 3.9.

## Note on outermost CMakeLists.txt
Note: The CMakeLists.txt fild in the main folder is for pybinds11. It was placed there so it could access the extern folder. For information on running, see the appropriate section below. It was mainly copied from https://www.youtube.com/watch?v=_5T70cAXDJ0.

## `ctypes`

This utilizes the standard Python module `ctypes`. To build and illustrate the program, navigate to the ctypes folder and run:

```
mingw32-make                 // on Windows
make -f Makefile-linux.mk    // on Linux
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

* For Windows:
    1. Install swig (used version 4.0.1) from https://www.swig.org/download.html, unzip the download, add it the appropriate folder to the path
    2. In the Makefile, set the value of `python_loc` to be the location where that version of Python is installed if using `mingw32-make`
    3. Appropritately modify CMakeLists.txt if using cmake
* For Linux:
    Attempt to install swig via the following commands, perhaps tailored to the appropriate Linux distribution:
    ```
    sudo apt-get update
    sudo apt-get install swig
    ```
    If not available through the package manager, download from https://www.swig.org/download.html and make it so swig is accessible from the command line.

### Building using a Makefile
To build and run a test program, run
```
mingw32-make                   // on Windows
make -f Makefile-linux.mk      // on Linux
```

To remove all created files (including those needed for the test program hello.py), run
```
mingw32-make clean                 // on Windows
make -f Makefile-linux.mk clean    // on Linux
```

### Building using CMake and Testing

#### Windows

See the notes under pybind11 for the requirements needed to build using cmake on Windows. Rahter than running cmake directly, it is reommended to run the batch file instead, the same as for pybind11.

To test, run hello.py.


#### Linux

If using Linux, delete (or rename) the current CMakeLists.txt and rename LinuxCMakeLists.txt as CMakeLists.txt. Then run the following commands (after creating the build-linux directory).
```
cmake -S . -B build-linux
cd build
make
cd ..
python3 helloLinux.py
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

# pybind11

Note: The test python files assume that numpy has been installed for the python version bing used.

This is a newer tool than the others. Similar to swig, it is a third party tool. However, unlike Swig, it is focused purely on C/C++ to Python. Using pybind11 is similar to using emscripten. In a .cpp file, bindings are specified that will be used to allow python to access (public) functionaligy of a C++ class or function. (In this code, these are placed into a separate file.) Before pybinds11 can be used, it must be installed. The way it was installed for this was the method by adding a git submodule as described in https://pybind11.readthedocs.io/en/stable/installing.html. More specifically, in a git project, run the following two commands:
```
git submodule add -b stable ../../pybind/pybind11 extern/pybind11
git submodule update --init
```
Afterwards, the pybind11 module can be accessed like any 3rd-party C++ module.

### Building with Makefile
One way of building the code is by directly using a g++ command in a makefile. Doing so requires that the name of the file be the same as the given name of the pybind module and that the file extension match one specified by Python. Thus, while it is doable, it would be more preferable to use CMake instead.

To build using the original makefile, run
```
mingw32-make                // on Windows
make -f Makefile-linux.mk   // on Linux
```

Both of these will run a shortened version of the appropriate python file used for demonstration.

#### Building With CMake on Windows

To build with CMake on Windows, both CMake and MSBuild are required. They come with the C++ tools installed with Windows; however, they are installed in the Developer Command Prompt.

To run, perform the following steps:
1. Navigate to usingPybBind11 in the Developer Command Prompt if CMake and MSBuild are inaccessible through the normal command prompt or PowerShell.
2. If the subdirectory build has not been created in usingPyBind11, create it.
3. Run the `cmake_build.bat` file:
    1. In command prompt, do so by `cmake_build.bat`
    2. In PowerShell, do so by `./cmake_build.bat`

### Building with CMake on Linux
In the directory, run the following commands (after creating the buildLinux directory):
```
cmake -S .. -B buildLinux
cd buildLinux
make
cd ..
```

To test, run
```
python3 testLinunx.py
```

### Advantages
* Once set up, relatively easy to use
* Good control over what is integrated into Python and how it is integrated
* Good for working with numpy in C++ (see video tutorial)

### Disadvantages
* Best done using CMake, and CMake behaves differently in Windows than in Unix.

# Sources
* For a discussion about swig vs ctypes, see https://stackoverflow.com/questions/135834/python-swig-vs-ctypes
* For a video going over various ways of integrating Python and C++, see https://www.youtube.com/watch?v=vvyTuFOJRrk

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

## For pybind11
* For compilation statement: https://stackoverflow.com/questions/60699002/how-can-i-build-manually-c-extension-with-mingw-w64-python-and-pybind11
* Official compilation resource: https://pybind11.readthedocs.io/en/stable/compiling.html
* For tutorial: https://www.youtube.com/watch?v=_5T70cAXDJ0
* Official documentation to get pybind11: https://pybind11.readthedocs.io/en/stable/installing.html

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

* For having multiple Makefiles per directory, see
    * https://stackoverflow.com/questions/12057852/multiple-makefiles-in-one-directory

## Sources solely for CMake
* Official CMake Documentation
* See https://stackoverflow.com/questions/31038963/how-do-you-rename-a-library-filename-in-cmake for proper way to change name.
* https://stackoverflow.com/questions/65626613/assigning-output-name-based-on-c-header-file-and-cmake-command
* For add_dependencies https://stackoverflow.com/questions/24614624/in-cmake-how-can-i-make-a-target-depend-on-another-target

## Sources for batch file for Swig
* For comments: https://www.tutorialspoint.com/batch_script/batch_script_comments.htm
* For user input: https://www.geeksforgeeks.org/batch-script-input-output/
* For conditional: https://stackoverflow.com/questions/5591491/conditional-statements-in-batch-files
* For MSBuild release option: https://docs.revenera.com/installshield22helplib/helplibrary/MSBuild_CmdLine.htm

## For why need to use release build in Windows:
* https://stackoverflow.com/questions/17028576/using-python-3-3-in-c-python33-d-lib-not-found

### Related
* https://stackoverflow.com/questions/42456284/how-to-link-shared-library-dll-with-cmake-in-windows
* https://stackoverflow.com/questions/30129155/linking-a-library-that-not-have-a-standarized-name-extension

## Makefile related
* For getting include path for python: Answer by Robᵩ in https://stackoverflow.com/questions/35071192/how-to-find-out-where-the-python-include-directory-is
* For finding problems with makefile: https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop
