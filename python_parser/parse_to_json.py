import json

file_name = "log.txt"
file = open(file_name, "r")
data = []
order = ["date", "url", "type", "message"]

for line in file.readlines():
    details = line.split("|")
    print("First details ********")
    print(details)
    details = [x.strip() for x in details]
    print("Second details ********")
    print(details)
    structure = {key: value for key, value in zip(order, details)}
    print("Structure ********")
    print(structure)
    data.append(structure)

for entry in data:
    print(json.dumps(entry, indent=4))