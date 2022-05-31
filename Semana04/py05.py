student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student)
print(student['name'])                      #imprime os dados da coluna nome
print(student['courses'])                   # imprime os dados da coluna courses
print(student['age'])                       # imprime os dados da coluna age

student = {1: 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student[1])                           # dados do parametro numerado

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student.get('name'))                  # dados do parametro name   

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student.get('phone'))                 # procura o parametro phone e retorna

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(student.get('phone', 'Not Found'))    # retorna ausencia de paramentro cao true

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)                              # adciona duas novas colunas a lista

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)                              # atualiza a lista

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
del student['age']
print(student)                              # deleta uma coluna

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
age = student.pop('age')                    # retira a coluna e quarda a variável
print(student)
print(age)

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
print(len(student))                         # quantidade de itens na lista 
print(student.keys())                       # titulos das colunas
print(student.values())                     # conteudo das colunas
print(student.items())                      # cada coluna separada

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
for key in student:
    print(key)                              # imprime cada titulo de cada item

student = {'name': 'John', 'age': 25, 'courses': ['Mat', 'Comp']}
for key, value in student.items():
    print(key, value)                       # imprime cada titulo e conteudo de cada item 