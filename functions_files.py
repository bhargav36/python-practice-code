from sys import argv

# argument varaibles
script, in_file = argv

# define function to print all
def print_all(f):
	print(f.read())

# define function to set the file's position
def rewind(f):
	f.seek(0)

# define function to print particular line
def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(in_file)

print("Print whole file:\n")
# call function to print all
print_all(current_file)

print("Rewind:\n")
#call funtion to reset the file offset
rewind(current_file)

print("Print 3 lines:\n")

current_line = 1
#call funtion to print line 1
print_a_line(current_line, current_file)

# Shorthand addition +=
current_line += 1
#call funtion to print line 2
print_a_line(current_line, current_file)

current_line = current_line + 1
#call funtion to print line 3
print_a_line(current_line, current_file)