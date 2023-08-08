# Write your code here :-)
#you need to add the requests library
import requests
import json
import pygal

bar = pygal.Bar()
bar2 = pygal.Bar()
#the url of the api we are using
ACT_url = "https://www.data.act.gov.au/resource/8mi2-3658.json"

#this code gets the data from the api and makes it available as a list
raw_data = requests.get(ACT_url)
list_data = json.loads(raw_data.text)

#processing the data and getting the items we want.
eddies_data = []
School_Data = []
for item in list_data:
    School_Data.append(item)
    if item['school_name'] == "St Edmund's College Canberra":
        eddies_data.append(item)

for item in eddies_data:
    bar.add(item['year_level'], int(item['students']))

for item in School_Data:
    bar2.add(item['year_level'], int(item['students']))
    print(item['year_level'])

bar.render_to_file('Eddies_Student_Vol.svg')
bar2.render_to_file('All_Student_Vol.svg')
