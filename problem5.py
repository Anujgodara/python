
import datetime

name =input("Give your Name:")

d=datetime.datetime.now()
curr_hour=d.hour
curr_min=d.minute
if curr_hour<12:
	print("Good Morning",name+"!")
elif curr_hour>11 and curr_hour<=16:
	print("Good Afternoon",name+"!")
elif curr_hour > 16 and curr_hour <=21:
	print("Good Evening",name+"!")
else:
print("Good Night", name+"!")
