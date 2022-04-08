# zero argument
def zero_args():
	print(f"This function has 0 arg")

def one_args(arg1):
	print(f"This function has 1 arg: {arg1}")

def two_args(arg1, arg2):
	print(f"This function has 2 args: {arg1} and {arg2}")

zero_args()
one_args("Hello")
two_args("Hello", "World")