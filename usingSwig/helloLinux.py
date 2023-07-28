# For making it work in python 3.9, got info/functions from:
#  https://www.reddit.com/r/learnpython/comments/wmd9ry/python_unable_to_load_dll_filenotfounderror_but/
#  https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-find-module-libvlc-dll/59016932#59016932 (most helpful)
#  https://github.com/python/cpython/issues/93094
#  https://www.reddit.com/r/learnpython/comments/ntb5f7/ctypes_library_isnt_working_with_c_code/
#  https://stackoverflow.com/questions/74524163/wrapping-an-external-c-library-with-swig-not-finding-standard-libraries
#  https://stackoverflow.com/questions/68298520/python-filenotfounderror-using-module-ctypes-and-cdll
# For how to view the DLL dependencies
#  https://stackoverflow.com/questions/7378959/how-to-check-for-dll-dependency

# Python 3.8 stopped searching path and current working directory; Need to add C++ standard lib
# See also https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa
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