
list_of_phones = [x for x in input().split(", ")]

while True:
    command = input()
    if "Add" in command:
        command = command.split(" ")
        if command[2] in list_of_phones:
            continue
        else:
            list_of_phones.append(command[2])
    if "Remove" in command:
        command = command.split(" ")
        if command[2] in list_of_phones:
            list_of_phones.remove(command[2])

    if "Bonus phone" in command:
        command = command.split(" ")
        phones = command[3].split(":")
        if phones[0] in list_of_phones:
            list_of_phones.append(phones[1])

    if "Last" in command:
        command = command.split(" ")
        if command[2] in list_of_phones:
            list_of_phones.remove(command[2])
            list_of_phones.append(command[2])

    if command == "End":
        break
for i in range(len(list_of_phones) - 1):
    list_of_phones[i] += ", "
for i in list_of_phones:
    print(i, end="")

