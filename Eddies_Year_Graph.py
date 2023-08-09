import pygal

Student_NR = []
Student_NR_Back = []
Year = ""

lines = pygal.Line()

file = open('Census_Data_for_all_ACT_Schools.csv', 'r')

for line in file.read().splitlines():
    if line:
        File = line.split(",")
        if File[1] == "St Edmund's College Canberra":
            if File[3] == "Year 10":
                Student_NR.append(int(File[4]))
                print(File[0])
                Year = File[3]
file.close()

Student_NR_Back = Student_NR[::-1]

lines.add(Year, Student_NR_Back)
lines.render_to_file('line.svg')
