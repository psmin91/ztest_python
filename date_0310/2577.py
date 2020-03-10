a=1
for i in range(1,4):
	a=a*int(input())	
a=str(a)
lst=[0,0,0,0,0,0,0,0,0,0]

for i in range(len(a)):
	lst[int(a[i])]=lst[int(a[i])]+1
for i in range(0,10):
	print(lst[i])

