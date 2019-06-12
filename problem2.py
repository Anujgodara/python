


list=[1,2,3,1,4,5,66,22,2,6,0,9]
p=[]
q=[]
for i in list:
	if i>5:
		print(i)
		p.append(i) 
print("\n")
for i in list:
	if i<=2:
		print(i)
		q.append(i)
print(p)
print(q)
