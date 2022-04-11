shift_pattern = 3
text = input("Enter plain text:")
cipher = ""

for c in text:
    if c.isupper():

        #find the position in 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        #shift
        new_index = (c_index + shift_pattern) % 26
        new_unicode = new_index + ord("A")

        #convert to character
        new_char = chr(new_unicode)
        cipher = cipher + new_char
    else:
        # find the position in 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("a")

        # shift
        new_index = (c_index + shift_pattern) % 26
        new_unicode = new_index + ord("a")

        # convert to character
        new_char = chr(new_unicode)
        cipher = cipher + new_char


print("Plain Text: ", text)
print("Cipher Text: ", cipher)


