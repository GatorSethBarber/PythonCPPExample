# For making it work in python 3.9, got info/functions from:
#  https://www.reddit.com/r/learnpython/comments/wmd9ry/python_unable_to_load_dll_filenotfounderror_but/
#  https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-find-module-libvlc-dll/59016932#59016932 (most helpful)
#  https://github.com/python/cpython/issues/93094
#  https://www.reddit.com/r/learnpython/comments/ntb5f7/ctypes_library_isnt_working_with_c_code/
#  https://stackoverflow.com/questions/74524163/wrapping-an-external-c-library-with-swig-not-finding-standard-libraries
#  https://stackoverflow.com/questions/68298520/python-filenotfounderror-using-module-ctypes-and-cdll

# Python 3.8 stopped searching path and current working directory (see 2nd source), so add them back in
# until can think of a better solution
import sys

if sys.version_info.major > 2 and sys.version_info.minor >= 8:
    import os
    temp = os.getenv('path').split(os.pathsep)
    for path in temp:
        try:
            os.add_dll_directory(path)
        except:
            pass

    os.add_dll_directory(os.getcwd())


import example
import pprint

print("dir of example:")
pprint.pprint(dir(example))

print("timesTwo(4) <-", example.timesTwo(4))
print("Executing echoPrint('hello')")
example.echoPrint('hello')

print("\n")

print("creating IncAndPrint")
inc = example.IncPrint()
print("calling printAndInc")
inc.printAndInc()
print("calling printAndInc")
inc.printAndInc()

print("\n\nBasic Overloading by calling overloaded")
inc.overloaded("hello")
inc.overloaded(3)
print("\n")
print("Example of an error will follow:")
inc.overloaded(2.3)