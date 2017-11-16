class test0(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
		
	def print_message(self):
		print('%s : %s' % (self.name,self.score))

class test1(test0):
	pass
bart=test1('bart palo',59)
bart.print_message()
print(type(bart))