import pygal

bar = pygal.Bar()
File = open('Out.csv', 'r')


for line in File.read().splitlines():
    if line:
        lines = line.split(",")
        bar.add(lines[0], float(lines[1])-70)
bar.render_to_file("WifiRSSI.png")
bar.render_in_browser()
