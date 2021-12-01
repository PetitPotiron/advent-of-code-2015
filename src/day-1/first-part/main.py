floor = 0
with open("input.txt","r") as file:
    for letter in file.read():
        if letter == "(":
            floor += 1
        else:
            floor -= 1
print("The Santa will finish on the floor", str(floor) + ".")