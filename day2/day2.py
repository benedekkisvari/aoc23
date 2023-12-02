f = open("input", 'r')

lines = []
for line in f:
    line = line.strip("Game: ").strip().replace(", ", ",").replace(" ,", ",").split(":")
    line[1] = line[1].split(";")
    line[1] = [show.strip().split(",") for show in line[1]]
    lines.append(line)
f.close()

num = 0
for line in lines:
    # Maximum search for part 2
    maxcolors = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    #Valid = True
    for show in line[1]:
        #Valid = True
        for cubes in show:
            number = int(cubes[0:cubes.find(" ")])
            if number > maxcolors[cubes[cubes.find(" ") + 1:]]:
                #Valid = False #check validity for part 1
                maxcolors[cubes[cubes.find(" ") + 1:]] = number
    #num += Valid * int(line[0])
    num += (maxcolors["red"] * maxcolors["green"] * maxcolors["blue"])
print(num)
