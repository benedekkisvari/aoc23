import re

nums_list = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
nums_digit_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

f = open("input", 'r')

lines = []
for line in f.readlines():
    line = line.strip()
    lines.append(line)
f.close()

num = 0
for line in lines:
    dl = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    first = dl[0]
    last = dl[-1]
    for i in range(len(nums_list)):
        first = first.replace(nums_list[i], nums_digit_list[i])
        last = last.replace(nums_list[i], nums_digit_list[i])
    toadd = int(first + last)
    num += toadd
print(num)

