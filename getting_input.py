print("What is your name?")
name = input()
# using end=' ' so that input doesn't go to the newline
print("What is your age?", end=' ')
age = input()

location = input("Enter your location:")

# typecasting user input to integer and float value, by default input() is string
number1 = int(input("Enter number1:"))
number2 = float(input("Enter number2:"))
total = number1 + number2


print(f"Hi {name}, you are {age} years old and live in {location}. Your total is: {total}")
