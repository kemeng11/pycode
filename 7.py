def f(x):
	return abs(x)+2
print(sorted([-4,2,3,4,5],key=f))