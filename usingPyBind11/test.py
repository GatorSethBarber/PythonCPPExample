import os
os.add_dll_directory("C:\\mingw\\mingw64\\bin")

import example

print(dir(example))

example.say_hello("Seth")

print("Creating object.")
obj = example.PyClassName()
print("Adding numbers")
obj.add_num(2)
obj.add_num(4)
obj.add_num(6)

print("printing")
obj.print_vec()
