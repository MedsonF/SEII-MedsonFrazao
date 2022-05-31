message = "Hello World"

print (message)                 # imprime o texto da variável
print (len(message))            # imprime o tamanho da variável
print (message[6])              # o caracter da posição 6
print (message[0:2])            # imprime os 3 primeiros carcateres 
print (message[5:])             # do 5º carcater até o final
print (message.lower())         # todo texto em minusculo
print (message.upper())         # todo teto em maiusculo
print (message.count('l'))      # quantos carcateres tem no texto 
print (message.find('W'))       # qual a posição do caracter

new = message.replace ('World','Universe')      
print(new)                      # troca um texto por outro

t1 = 'oi'
t2 = 'gente'
texto = t1 + ', ' + t2 + '. Bem vindo!'
print (texto)                   # imprime mensagem concatenada 

new = '{}, {}. Bem vindo!'.format(t1, t2)
print (new)                     # varias variáveis nas posições 

print (dir(t2))                 # informações sobre variável
print (help(str))               # informação sobre função