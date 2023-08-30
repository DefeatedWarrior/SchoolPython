import statistics
import sys

File = open("Data.csv", "r")
Output = open("Out.csv", "w")
Array = []
Room_NR = []

for line in File.read().splitlines():
    if line:
        lines = line.split(",")
        if lines[1] == "Student":
            Array.append(str(lines[0]) + "," + str(lines[2]))
            Room_NR.append(lines[0])

Room_NR = list(dict.fromkeys(Room_NR))

results = {}

for Room in Array:
    S2 = Room.split(",")
    if S2[0] in results:
        results[S2[0]].append(int(S2[1]))
    else:
        results[S2[0]] = [int(S2[1])]

for x, y in results.items():
    AVG = (x + "," + str(round(statistics.mean(y), 2)))
    Output.write(AVG + "\n")

Output.close()
File.close()
sys.exit(":)")
