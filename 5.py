from functools import reduce
def f(x,y):
	return x*y
print(reduce(f,[1,2,3,4]))