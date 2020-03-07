
def BubbbleSort(x):

	x_len = len(x)
	for i in range(x_len):
		for j in range(x_len-1):
			if x[j] >x[j+1]:
				x[j],x[j+1] = x[j+1],x[j]
		
x=[1, 23, 14, 15] 
BubbbleSort(x)
print(x)

