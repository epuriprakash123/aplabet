n=int(input())
s=list(input())
l=['a','e','i','o','u']
k=[]
for i in s:
	if i not in l:
		k.append(i)
k=k[::-1]
print(''.join(k))
