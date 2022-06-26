
name_of_coffees = [x for x in input().split(" ")]
num_of_commands = int(input())

for i in range(num_of_commands):
    command = input()
    if "Include" in command:
        command = command.split(" ")
        name_of_coffees.append(command[1])
    elif "Remove" in command:
        command = command.split(" ")
        if command[1] == "first":
            try:
                for i in range(int(command[2])):
                    name_of_coffees.pop(0)
            except IndexError:
                continue
        elif command[1] == "last":
            try:
                for i in range(int(command[2])):
                    name_of_coffees.pop(-1)
            except IndexError:
                continue            
    elif "Prefer" in command:
        command = command.split(" ")
        try:
            coffee1 = int(command[1])
            coffee2 = int(command[2])
            name_of_coffees[coffee1], name_of_coffees[coffee2] = name_of_coffees[coffee2], name_of_coffees[coffee1]
        except IndexError:
            continue
    elif "Reverse" in command:
        name_of_coffees.reverse()
print(f"Coffees:")        
for i in name_of_coffees:
    print(i, end=" ")
    



