visited_houses_by_santa = [(0,0)]
visited_houses_by_robo_santa = [(0,0)]
with open("../input.txt", "r") as file:
    k = 0
    for instruction in file.read():
        if k % 2 == 0:
            visited_houses = visited_houses_by_santa
        else:
            visited_houses = visited_houses_by_robo_santa
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
        k += 1
print(len(set(visited_houses_by_santa+visited_houses_by_robo_santa)), "houses receive at least 1 present.")
