import datetime

persons = {}
print("Welcome to my Satr Project\nthis project to find the oldest/youngest person")
loop = int(input("how many persons you want to add: "))
while loop > 0:
	try:
		name = input("The name : ")
		date = list(map(int,input("date: ").split("-")))
		persons[name] = datetime.date(*date)
	except ValueError:
		print("Invalid date")
	loop -=1
y = datetime.datetime.now().year
for person in persons:
	print(f"{person} is {y- persons[person].year} years old and she/he was born on {persons[person].strftime('%A')}.")
if len(persons) == 1:
	print("There is no oldest or youngest person.")
else:
	print(f"The oldest one is {max(persons, key=persons.get)}.")
	print(f"The youngest one is {min(persons,key=persons.get)}")