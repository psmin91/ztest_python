x=input()
first=int(x)
y=0
count=0
if len(x)==1:
	x="0"+x

while 1:
	count+=1
	y=str(int(x[0])+int(x[1]))
	x=x[1]+y[len(y)-1]
	if first==int(x):
		break
print(count)
