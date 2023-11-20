floor = 0
with open("../input.txt","r") as file:
    for position, instruction in enumerate(file.read()):
        if instruction == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print("The instruction at position", index+1, "made the santa enter the basement.")
            break
