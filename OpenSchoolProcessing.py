import requests
import json
import pygal

SchoolName = []
y = []
bar = pygal.Bar()



School = input("What is the School Name (MUST be Perfect) Leave Blank To Generate examples in EG.txt: ")

if School == "":
    eg = open("EG.txt", "w")
    eg.write("")
    eg.close()
    eg = open("EG.txt", "a")

# the url of the api we are using
ACT_url = "https://www.data.act.gov.au/resource/8mi2-3658.json"

# this code gets the data from the api and makes it available as a list
raw_data = requests.get(ACT_url)
list_data = json.loads(raw_data.text)




for item in list_data:
    SchoolName.append(item['school_name'])

if School == "":
    for l in SchoolName:
        if l not in y:
            y.append(l)
            eg.write(l + "\n")

# processing the data and getting the items we want.
School_Data = []
for item in list_data:

    if item['school_name'] == str(School):
        School_Data.append(item)

for item in School_Data:
    bar.add(item['year_level'], int(item['students']))

eg.close()
if School != "":
    bar.render_to_file(str(School)+'.svg')

