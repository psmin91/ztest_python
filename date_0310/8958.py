testcase=int(input())
for i in range(0,testcase):
	strin=input()
	lst=[0]
	for j in range(1,len(strin)+1):
		if strin[j-1]=="X":
			lst.append(0)	
		else:
			lst.append(lst[j-1]+1)
	print(sum(lst))
