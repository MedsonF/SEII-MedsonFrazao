def func():
    pass
func()


def func():
    print('Hello function')
func()          		# chama função


def func():
    print('Hello function')
print('Hello ')
print('Hello ')
print('Hello ')
print('Hello ')


def func():
    print('Hello function')
print('Hello .')
print('Hello .')
print('Hello .')
print('Hello .')


def func():
    print('Hello function!')
func()
func()
func()
func()


def func():
    return 'Hello function.'
print(func())				# executa função e printa


def func():
    return 'Hello function.'
print(len('Test'))			# tamanho do texto


def func():
    return 'Hello function.'
print(func().upper())			# imprime tudo em maiusculo


def func(greeting):			# guarda string na variável da função
    return '{} Funtion.'.format(greeting)
print(func('Hi'))


def func(greeting, name='You'):				# se variável nao foi declarada ela vai pela definição da função
    return '{}, {}'.format(greeting, name)
print(func('Hi'))


def func(greeting, name='You'):				# se a variável é declarada na chamada é o que vale
    return '{}, {}'.format(greeting, name)
print(func('Hi', name = 'Corey'))



def func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

def student_info(*args, **kwargs):
    print(args)					# printa os dois primeiros argumentos
    print(kwargs)				# printa os dois ultimos 

student_info('Mat', 'Art', name='John', age=22)



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Mat', 'Art')
info = {'name': 'John', 'age': 22, }

student_info(courses, info)



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('Mat', 'Art')
info = {'name': 'John', 'age': 22, }

student_info(*courses, **info)



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(is_leap(2017))


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(is_leap(2020))


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days(month)
print(days_in_month(2017, 2)) 