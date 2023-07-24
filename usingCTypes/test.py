# Usually, would probably be best to create a wrapper class.

# See https://www.youtube.com/watch?v=b1E-4EZJ9OU for code

# For making it work in python 3.9, got info/functions from:
#  https://www.reddit.com/r/learnpython/comments/wmd9ry/python_unable_to_load_dll_filenotfounderror_but/
#  https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-find-module-libvlc-dll/59016932#59016932 (most helpful)
#  https://github.com/python/cpython/issues/93094
#  https://www.reddit.com/r/learnpython/comments/ntb5f7/ctypes_library_isnt_working_with_c_code/
#  https://stackoverflow.com/questions/74524163/wrapping-an-external-c-library-with-swig-not-finding-standard-libraries
#  https://stackoverflow.com/questions/68298520/python-filenotfounderror-using-module-ctypes-and-cdll

import ctypes
import pprint
import sys


# Python 3.8 stopped searching path and current working directory (see 2nd source), so add them back in
# until can think of a better solution
if sys.version_info.major > 2 and sys.version_info.minor >= 8:
    import os
    temp = os.getenv('path').split(os.pathsep)
    for path in temp:
        try:
            os.add_dll_directory(path)
        except:
            pass

    os.add_dll_directory(os.getcwd())


sample = ctypes.CDLL('./sample.dll')

print("shown dir of sample:")
pprint.pprint(dir(sample))

print("sample.divizByTwo(4) <-", sample.divizByTwo(4))
print('Calling printInput(ctypes.create_string_buffer(b"hello"))')
sample.printInput(ctypes.create_string_buffer(b"hello"))