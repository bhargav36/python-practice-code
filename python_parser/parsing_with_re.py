import sys
import re

file_name = "example.logs"
new_file_name = "parsed_text.txt"
new_file = []
pattern_ip = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s'
pattern_code = ' 20\d+ | 30\d+ | 40\d+ | 50\d+ '

with open(file_name, 'r') as f:
    lines = f.readlines()

for line in lines:
    match_ip = re.search(pattern_ip, line)
    match_code = re.search(pattern_code, line)
    if match_ip:
        new_line = match_ip.group() + '->'
        new_file.append(new_line)

    if match_code:
        new_line = match_code.group() + '\n'
        new_file.append(new_line)

with open(new_file_name, 'w') as w:
    w.writelines(new_file)
    print("Parsed text added to file")



