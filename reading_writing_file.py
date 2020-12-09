from sys import argv

script, filename = argv

txt = open(filename)
print(f"Your file to read: {filename}")
print(txt.read())

print(f"We are going to truncate the {filename}, to proceed hit RETURN")
input("?")

print("Opening file....")
target = open(filename,'w')

print("Truncating file....")
target.truncate()

print("Write new contents to file...")

line1 = input("1. ")
line2 = input("2. ")
line3 = input("3. ")

print(f"Writing ^^ to file -> {filename}")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
