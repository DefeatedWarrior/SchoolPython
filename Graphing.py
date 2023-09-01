import pygal
import os

def LineCharts():
    os.system("mkdir Images/")
    os.system("mkdir Images/Line/")
    File2 = open("CSV/Data.csv", "r")
    Array = []
    # linechart = pygal.Line()

    for line in File2.read().splitlines():
        if line:
            lines = line.split(",")
            if lines[1] == "Student":
                Array.append(str(lines[0]) + "," + str(lines[2]))

    results = {}

    for Room in Array:
        S2 = Room.split(",")
        if S2[0] in results:
            results[S2[0]].append(int(S2[1]))
        else:
            results[S2[0]] = [int(S2[1])]

    for x, y in results.items(): # X is the room Number, Y is the Values
        linechart = pygal.Line()
        linechart.add(x, y)
        linechart.render_to_file('Images/Line/' + str(x) + '_line.svg')
    File2.close()
def BarChart():

    bar = pygal.Bar()
    File = open('CSV/Out.csv', 'r')
    for line in File.read().splitlines():
        if line:
            lines = line.split(",")
            bar.add(lines[0], float(lines[1])-70)
    bar.render_to_file("Images/WifiRSSI.png")
    File.close()

LineCharts()
BarChart()


