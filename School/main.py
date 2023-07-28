import pygal
import os

Reaction = []
Burpees = []
Name = []
File = []
Sport = []


scatter = pygal.XY(scatter=False)
bar = pygal.Bar()
bar2 = pygal.Bar()

file = open('semester.csv', 'r')

for line in file.read().splitlines():
    if line:
        File = line.split(",")
        Reaction.append(File[0])
        Burpees.append(File[1])
        Name.append(File[2])
        Sport.append(File[3])
        scatter.add(str(File[2]), [(float(File[0]), float(File[1]))])
        bar.add(File[2], float(File[0]))
        bar2.add(File[2], float(File[1]))
file.close()

print("Reaction time (Ms) " + str(Reaction))
print("Amount of Burpees " + str(Burpees))
print("Name " + str(Name))
print("Primary Sport " + str(Sport))

scatter.render_to_file('Images/Scatter.svg')
bar.render_to_file('Images/Reaction.svg')
bar2.render_to_file('Images/Burpees.svg')
os.system("xcowsay --cow-size=small -d /home/will/PycharmProjects/School/Images/Reaction.svg")
os.system("xcowsay --cow-size=small -d /home/will/PycharmProjects/School/Images/Burpees.svg")
os.system("xcowsay --cow-size=small -d /home/will/PycharmProjects/School/Images/Scatter.svg")
os.system("test")