class animal(object):
	def type_1(self):
		print('this is an animal')
class mammal(animal):
	def type_2(self):
		print('this is an mammal')
class bird(animal):
	def type_2(self):
		print('this is a bird')

class Run(object):
	def walk_type(self):
		print('run')
class Fly(object):
	def walk_type(self):
		print('fly')


class dog(mammal,Run):
	def type_3(self):
		print('this is a dog')
class parrot(bird,Fly):
	def type_3(self):
		print('this is a parrot')


a=dog()
a.type_1()
a.type_2()
a.type_3()
a.walk_type()
print('-------------------------')
b=parrot()
b.type_1()
b.type_2()
b.type_3()
b.walk_type()