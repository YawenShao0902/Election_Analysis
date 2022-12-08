print("Hello World")
counties = ['Arapahoe', 'Denver', 'Jefferson']
print(counties [2])
print(len(counties))
print(counties [0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
print(counties.append("El Paso"))
print(counties)
print(counties.insert(2,'El Paso'))
print(counties)
print(counties.remove('El Paso'))
print(counties)
print(counties.pop(3))
print(counties)
counties[2]='El paso'
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(counties_tuple)
print(len(counties_tuple))
print(counties[1])
counties_dict = {}
counties_dict['Arapahoe']= 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get('Denver'))
print(counties_dict['Arapahoe'])
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
print(len(voting_data))
voting_data.insert(1,{"county":"El paso}","registered_votes":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El paso is in the list of counties.")
else:
    print("El paso is not in the list of counties.")

x=0
while x<=5:
    print(x)
    x=x+1

for county in counties:
    print(county)

numbers=[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county,voters in counties_dict.items():
    print(county,voters)

voting_data = [{"county":"Arapahoe","Registered_voters":422829},{"county":"Dever","Registered_voters":463353},{"county":"Jefferson","Registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
    
for county_dict in voting_data:
    print(county_dict["county"])

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")









