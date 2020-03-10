testcase=int(input())
for i in range(0,testcase):
	lst=list(map(int,input().split()))
	k=(sum(lst)-lst[0])/lst[0]
	count=0
	for j in range(1,lst[0]+1):
		if lst[j]>k :
			count+=1
	print("{:.3f}%".format(count*100/lst[0]))	
