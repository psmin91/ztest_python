#hardcoding


#algo
lst=[]
for i in range(0,10000):
	lst.append(i)	

for a in range(0,10):
	num1=a*1001
	if num1 in lst:
		lst.remove(num1)

	for b in range(0,10):
		num2=b*101+num1
		if num2 in lst:
			lst.remove(num2)

		for c in range(0,10):
			num3=c*11+num2
			if num3 in lst:
				lst.remove(num3)

			for d in range(0,10):
				num4=d*2+num3
				if num4 in lst:
					lst.remove(num4)


for i in range(0,len(lst)):
	print(lst[i])



