message = 'Hello World'

print ('Hello World') # imprime o texto

print (len(message)) # imprime a quantidade de caracteres da variavel

print (message[0:5]) # imprime os 5 primeiros caracteres

print (message[6:]) # imprime a partir do 6º caractere

print (message.lower()) # imprime todo texto em minusculo

print (message.upper()) # imprime todo texto em maiusculo 

print (message.count('Hello')) # imprime a quantidade de caracteres selecionados

print (message.find('o')) # a partir de qual caractere esta escrito 

new_message = message.replace ('World', 'Universe') # altera o texto por outro

print (new_message)

greeting = 'Hello'
name = 'Paulo'

char = greeting + ', ' + name + ". Welcome" # concatena variáveis de string

print (char)

char = '{}, {}. Welcome!'.format(greeting, name) # imprime variaveis diferentes nas chaves do texto

print (char)

print (help(str.lower)) # informações sobre variavel
