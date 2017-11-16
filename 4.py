from functools import reduce
def f(x,y):
	return 10*x+y
def ch2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(f,map(ch2num,'1234')))