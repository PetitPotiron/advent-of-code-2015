floor = 0
with open("../input.txt","r") as file:
    for instruction in file.read():
        if instruction == "(":
            floor += 1
        else:
            floor -= 1
print("The Santa will finish on the floor " + str(floor) + ".")
