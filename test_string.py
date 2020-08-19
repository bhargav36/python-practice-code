types_of_people = 10
# Basic use of fstring
x = f"There are {types_of_people} people in the room"
print(x)

#Function that will be called from fstring
def to_lowercase(input):
	return input.lower()

name = "Bob Alice"
age = "32"
length = 100
# Calling function
y=f"{to_lowercase(name)} is funny"
print(y)

# Calling method directly
z=f"{name.upper()} is {age} years and his height is {length + 1} inches"
print(z)

print(f"Hi, {name}, hello from print function")

