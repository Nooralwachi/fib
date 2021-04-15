def fib(n):
	if n in(0,1):
		return n
	else:
		return(fib(n-1) +fib(n-2))

for i in range(11):
	print(i, fib(i))

cache={}
def fib_caching(n):
	#print(cache)
	if n in (0,1):
		cache[n]=n
		return n
	elif n in cache:
		return cache[n]
	value = fib_caching(n-2) +fib_caching(n-1) 
	cache[n]=value
	return value
	
for i in range(11):
	print(i, fib_caching(i))