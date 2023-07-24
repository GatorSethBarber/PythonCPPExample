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