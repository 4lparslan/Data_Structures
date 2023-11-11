cache = [None]*(100)

def fibonacci(n):
	if n <= 1:
		return n 
	if cache[n] is None:
		cache[n] = fibonacci(n-1) + fibonacci(n-2)
	return cache[n]

print(fibonacci(6))

# Cache list is not functional but this is only an example for dynamic programming.