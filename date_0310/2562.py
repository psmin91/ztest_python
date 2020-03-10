lst=[]
for i in range(1,10):
    lst.append(int(input()))

a = max(lst)
print(a)
print(lst.index(a)+1)
