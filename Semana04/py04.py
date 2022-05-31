'''
materias = ['His', 'Mat', 'Fis','Comp']
print(materias)                             # imprime a lista
print(len(materias))                        # o tamanho da lista
print(materias[0])                          # o 1º da lista
print(materias[1])                          # o 2º da lista
print(materias[2])                          # o 3º da lista
print(materias[3])                          # o 4º da lista
print(materias[-1])                         # o ultimo da lista
print(materias[0:2])                        # os 2 primeiros
print(materias[:2])                         # os 2 primeiros
print(materias[2:])                         # do 2º até o fim

materias.append('Art')
print(materias)                             # acrescenta a lista

materias = ['His', 'Mat', 'Fis','Comp']
materias.insert(0, 'Art')
print(materias)                             # acrescenta a posição 0

materias = ['His', 'Mat', 'Fis','Comp']
materias_2 = ['Art', 'Edu']
materias.insert(0, materias_2)              # acrescenta a lista na posição 0
print(materias)
print(materias[0])                          # a string da posição 0

materias = ['His', 'Mat', 'Fis','Comp']
materias_2 = ['Art', 'Edu']
materias.extend(materias_2)                 # coloca o conteudo da lista em outra lista
print(materias)

materias = ['His', 'Mat', 'Fis','Comp']
materias_2 = ['Art', 'Edu']
materias.append(materias_2)                 # coloca a lista no final
print(materias)

materias = ['His', 'Mat', 'Fis','Comp']
materias.remove('Mat')                      # remove da lista
print(materias)                     

materias = ['His', 'Mat', 'Fis','Comp']
popp = materias.pop()                       # guarda e remove a ultima variavel da lista
print(popp)
print(materias)

materias = ['His', 'Mat', 'Fis','Comp']
materias.reverse()                          # inverte a lista
print(materias)

materias = ['His', 'Mat', 'Fis','Comp']
materias.sort()                             # organiza a lista 
print(materias)

materias = ['His', 'Mat', 'Fis','Comp']
num = [1, 5, 2, 4, 3]
materias.sort()                             # ordem alfabética
num.sort()                                  # do menor para o maior
print(materias)
print(num)

materias = ['His', 'Mat', 'Fis','Comp']
num = [1, 5, 2, 4, 3]
materias.sort(reverse=True)                 # ordem alfabética invertida
num.sort(reverse=True)                      # do menor para o maior invertida
print(materias)
print(num)

materias = ['His', 'Mat', 'Fis','Comp']
sourted_materias =sorted(materias)          # colocar em ordem e gravar em uma variável
print(sourted_materias)

num = [1, 5, 2, 4, 3]
print(min(num))                             # menor valor da lista
print(max(num))                             # maior valor da lista
print(sum(num))                             # soma dos valores

materias = ['His', 'Mat', 'Fis','Comp']
print(materias.index('Comp'))               # posição na lista
print('Art' in materias)                    # procurar Art na lista
print('Mat' in materias)                    # procurar Mat na lista

materias = ['His', 'Mat', 'Fis','Comp']
for iten in materias:                       # imprimir cada item da lista
    print(iten)

materias = ['His', 'Mat', 'Fis','Comp']
for course in materias:                     # imprimir cada item da lista
    print(course)
'''
materias = ['His', 'Mat', 'Fis','Comp']
for index, course in enumerate(materias):   # indice e item da lista
    print(index, course)

materias = ['His', 'Mat', 'Fis','Comp']
for index, course in enumerate(materias, start=1):  # indice e item começando pelo indice 1
    print(index, course)

materias = ['His', 'Mat', 'Fis','Comp']
course_str = ', '.join(materias)            # lista separada por virgula
print(course_str)

materias = ['His', 'Mat', 'Fis','Comp']
course_str = ' - '.join(materias)           # lista separada por hifen
new_list = course_str.split(' - ')          # lista separada por hifen
print(course_str)
print(new_list)

list_1 = ['His', 'Mat', 'Fis','Comp']
list_2 = list_1                             # atribuir lista 2 a lista 1
print(list_1)
print(list_2)
list_1[0] = 'Art'                           # trocar item da lista
print(list_1)
print(list_2)

tuple_1 = ('His', 'Mat', 'Fis', 'Comp')
tuple_2 = tuple_1                           # lista por parenteses
print(tuple_1)
print(tuple_2)

cs_courses = {'His', 'Mat', 'Fis', 'Comp', 'Mat'}
print(cs_courses)                           # lista por chaves

cs_courses = {'His', 'Mat', 'Fis', 'Comp', 'Mat'}
print('Mat' in cs_courses)                  # procurar item na lista 

cs_courses = {'His', 'Mat', 'Fis', 'Comp'}
art_courses = {'His', 'Mat', 'Art', 'Des'}
print(cs_courses.intersection(art_courses)) # itens em comum 
print(cs_courses.difference(art_courses))   # itens diferentes 
print(cs_courses.union(art_courses))        # união dos itens das listas
