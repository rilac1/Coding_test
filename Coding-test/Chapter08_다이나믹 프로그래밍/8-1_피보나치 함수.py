import time
start = time.time()

def fibo(x):
	if x == 1 or x == 2:
		return 1
	else:
		return fibo(x-1) + fibo(x-2)

fibo(40)
print("time: ", time.time() - start)

