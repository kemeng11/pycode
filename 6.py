def te(x):
	a= x*x-4*x
	return a==0
print(list(filter(te,[0,1,2,3,4,,5])))
