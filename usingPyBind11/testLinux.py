import os
import sys

import buildLinux.example as example

print(dir(example))

if len(sys.argv) > 1:
    quit()
    

example.say_hello("Seth")

print("Creating object.")
obj = example.PyClassName()
print("Adding numbers")
obj.add_num(2)
obj.add_num(4)
obj.add_num(6)

print("printing")
obj.print_vec()

import numpy as np

print("\nGrad mult:")
list_input = [1, 2, 3, 4, 5]
print("input:", list_input)
print("output:", obj.grad_product(list_input))
print("\nGrad mult numpy")
print("output:", obj.g_prod_numpy(np.array([[1, 2], [3, 4]])))

print("\nCreate tuple")
print("Output:", example.create_tuple("hello", 3.14))

print("\nMake Triplet")
print("Output:", example.make_triplet(0, "hello to yu"))

print("\nTesting property")
print(obj.my_var)
obj.my_var = 3