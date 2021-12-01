floor = 0
with open("input.txt","r") as file:
    for index, letter in enumerate(file.read()):
        if letter == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print("The character at position", index+1, "made the santa enter the basement.")
            break