# Usually, would probably be best to create a wrapper class.

# See https://www.youtube.com/watch?v=b1E-4EZJ9OU for code

import ctypes
import pprint

sample = ctypes.CDLL('./sample.dll')

print("shown dir of sample:")
pprint.pprint(dir(sample))

print("sample.divizByTwo(4) <-", sample.divizByTwo(4))