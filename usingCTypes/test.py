# Usually, would probably be best to create a wrapper class.

# See https://www.youtube.com/watch?v=b1E-4EZJ9OU for code

# For making it work in python 3.9, got info/functions from:
#  https://www.reddit.com/r/learnpython/comments/wmd9ry/python_unable_to_load_dll_filenotfounderror_but/
#  https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-find-module-libvlc-dll/59016932#59016932 (most helpful; talks about os.add_dll_directory)
#  https://github.com/python/cpython/issues/93094
#  https://www.reddit.com/r/learnpython/comments/ntb5f7/ctypes_library_isnt_working_with_c_code/
#  https://stackoverflow.com/questions/74524163/wrapping-an-external-c-library-with-swig-not-finding-standard-libraries
#  https://stackoverflow.com/questions/68298520/python-filenotfounderror-using-module-ctypes-and-cdll
# For how to view the DLL dependencies
#  https://stackoverflow.com/questions/7378959/how-to-check-for-dll-dependency

import ctypes
import pprint
import sys

# Python 3.8 stopped searching path and current working directory; Need to add C++ standard lib
# See also https://stackoverflow.com/questions/69885600/swig-doesnt-work-on-windows-with-mingw-w64-when-binding-c-and-python-dll-loa
if sys.version_info.major > 2 and sys.version_info.minor >= 8:
    import os
    os.add_dll_directory("C:\\mingw\\mingw64\\bin")


sample = ctypes.CDLL('./sample.dll')

print("shown dir of sample:")
pprint.pprint(dir(sample))

print("sample.divizByTwo(4) <-", sample.divizByTwo(4))
print('Calling printInput(ctypes.create_string_buffer(b"hello"))')
sample.printInput(ctypes.create_string_buffer(b"hello\0"))