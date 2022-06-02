
num = [1, 2, 3, 4, 5]
for num in num:
    print(num)         		# conteudo de cada item da lista 


num = [1, 2, 3, 4, 5]
for num in num:
    if num == 3:
        print('Found:')
        break				# sai da condição
    print(num)


num = [1, 2, 3, 4, 5]
for num in num:
    if num == 3:
        print('Found:')
        continue			# sai da confição mas continua no for
    print(num)


num = [1, 2, 3, 4, 5]
for num in num:
    for letra in 'abc':
        print(num, letra)		# define sequencia de letras, sequencia alfabética


for i in range(10):
    print(i)				# contagem de 1 a 9


for i in range(1, 11):
    print(i)				# contagem de 1 a 10


x = 0
while x < 10:
    print(x)				# contagem de 1 a 9
    x += 1


x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1


#x = 0
#while True:
#    print(x)
#    x += 1toush