X = 0

filename = input('What Is The File Name (FileName.FileType): ')

file = open(str(filename), 'r')
output = open("Output_" + str(filename), "w")
output.write("")


for line in file.read().splitlines():
    output = open("Output_" + str(filename), "a")
    if X == 0:
        output.writelines(str(line)+ "\n")
        X = 1

    elif X == 1:
        X = 0
        continue

    output.close()

file.close()


