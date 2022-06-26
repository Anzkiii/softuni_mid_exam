
list_of_phones = [x for x in input().split(", ")]

while True:
    command = input()
    if "Add" in command:
        command = command.split(" ")
        if command[2] in list_of_phones:
            continue
        else:
            list_of_phones.append(command[2])
    elif "Remove" in command:
        command = command.split(" ")
        if command[2] in list_of_phones:
            list_of_phones.remove(command[2])
        else:
            continue
    elif "Bonus phone" in command:
        command = command.split(" ")
        phones = command[3].split(":")
        if phones[0] in list_of_phones:
            list_of_phones.append(phones[1])
        else:
            continue
    elif "Last" in command:
        command = command.split(" ")
        if command[2] in list_of_phones:
            list_of_phones.remove(command[2])
            list_of_phones.append(command[2])
    elif command == "End":
        break
for i in range(len(list_of_phones) - 1):
    list_of_phones[i] += ", "
for i in list_of_phones:
    print(i, end="")

