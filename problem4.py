import os
username=input("enter username")
flag=0
number=[0,1,2,3,4,5,6,7,8,9]
for i in username:
	if i in str(number):
		flag=1
if(flag==1):
	print("invalid usrname")
else:
	password="hello"+username
	print("user added")
