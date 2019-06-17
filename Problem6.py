#cat command
file = open("file.txt", "r")
print(file.read())

#for cat -e command
for line in file:
    print(line.strip() + "$")

#for cat -n command
count = 1
for line in file:
    print(str(count)+line.strip())
