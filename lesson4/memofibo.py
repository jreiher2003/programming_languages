import timeit
t = timeit.Timer(stmt = """
chart = { }
def memofibo(n):
	if n in chart:
		return chart[n]
	elif n <= 2:
		chart[n] = 1
	else:
		chart[n] = memofibo(n-1) + memofibo(n-2)
	return chart[n]

memofibo(24)
""")
print t.timeit(number=100)

