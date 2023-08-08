import pygal

time = []
accelerations = []

bar = pygal.Bar()
accelline = pygal.Line()

file = open('jack.csv', 'r')




for line in file.read().splitlines():
    if line:
        File = line.split(",")
        time.append(float(File[1]))
        accelerations.append(float(File[0])/1000)
        bar.add(File[1], float(File[0]))

file.close()

accelline.x_labels = map(str, range(0, len(time)))
accelline.add('jack', accelerations)

bar.render_to_file('Jack.svg')
accelline.render_to_file('line.svg')