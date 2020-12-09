# add features/modules/libraries to the script using "import"
# argv is the argument variable
from sys import argv
# importing datetime library
from datetime import datetime


script, user_name = argv
prompt = '->'

print(f"Hi {user_name}, ")
print("I'd like to ask few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

#getting input from user
name = input("What is your name?\n")
print(f"This script was executed by: {name}")

#shows current date and time, for e.g. 2020-08-26 15:08:28.183509
now = datetime.now()

#timestamp in epoch time
timestamp = datetime.timestamp(now)

print(f"This is {script} script, run by {user_name} who lives in {lives}.")
print(f"Last runtime: {now}" )
print("Timestamp:", timestamp)
