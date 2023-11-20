visited_houses = [(0,0)]
with open("../input.txt", "r") as file:
    for instruction in file.read():
        next_house = list(visited_houses[-1])
        if instruction == "^":
          next_house[1] += 1
        elif instruction == ">":
          next_house[0] += 1
        elif instruction == "v":
          next_house[1] -= 1
        elif instruction == "<":
          next_house[0] -= 1
        visited_houses.append(tuple(next_house))
print(len(set(visited_houses)), "houses receive at least 1 present.")
