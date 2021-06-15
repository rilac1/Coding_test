str = input()
num=[]
for i in str:
	num.append(int(i))
	
ret = 0	
for n in num:
	if ret <=1 or n<=1:
		ret += n
	else:
		ret *= n
print(ret)	 	
	 	
	
