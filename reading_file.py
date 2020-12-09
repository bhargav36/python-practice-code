from sys import argv

script, filename = argv

prompt = '>>>'
txt = open(filename)

print(f"Your file to read: {filename}")
print(txt.read())
txt.close()

print("File name as input: ")
filename_again = input(prompt)

txt_again = open(filename_again)
print(txt_again.read())
txt_again.close()