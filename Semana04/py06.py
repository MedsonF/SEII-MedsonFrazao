			# usando condicionais com comparativos
language = 'Python'
if language == 'Python':			
	print('Conditional was True')


language = 'Python'
if language == 'Python':
	print('Language is Python')
else:
	print('No match')


language = 'Java'
if language == 'Python':
	print('Language is Python')
else:
	print('No, is Other')


language = 'Java'
if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('No, is Other')


language = 'Java'
if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
elif language == 'JavaScript':
	print('Language is JavaScript')
else:
	print('No, is Other')


			# condicional com mais condições
user = 'Admin'
login = True
if user == 'Admin' and login:
	print('Admin Page')
else:
	print('Bad Creds')


user = 'Admin'
login = False
if user == 'Admin' and login:
	print('Admin Page')
else:
	print('Bad Creds')


user = 'Admin'
login = False
if user == 'Admin' or login:
	print('Admin Page')
else:
	print('Bad Creds')


user = 'Admin'
login = False
if not login:
	print('Please Log In')
else:
	print('Welcome')


a = [1,2,3]
b = [1,2,3]
print(a==b)

a = [1,2,3]
b = [1,2,3]
print(a is b)

a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print(a==b)

a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))

			# condicionais fixos
condition = False
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')


condition = None
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')


condition = 10
if condition:
	print('Evalued to True')	
else:
	print('Evalued to False')

							
condition = []
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')


condition = ''
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')


condition = 'Test'
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')