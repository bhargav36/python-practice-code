from sys import argv
from os.path import exists

#taking file name as the argument
script, from_file, to_file = argv


#static file name to read
#from_file = "from_file.txt"
print(f"Copying data from {from_file} to {to_file}")


in_data = open(from_file).read()

print(f"Does file exists? {exists(to_file)}")
print(f"Hit Return to continue,")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print(f"Done...")

out_file.close()
