def compute_n_fibonacci(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return compute_n_fibonacci(n-1) + compute_n_fibonacci(n-2)

print compute_n_fibonacci(3)
print compute_n_fibonacci(5)
