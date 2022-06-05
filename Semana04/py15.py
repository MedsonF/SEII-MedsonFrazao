import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)

    for line in csv_reader:
        print(line)




import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line(2))




import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_name.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

    for line in csv_reader:
        csv_writer.writerow(line)




import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_name.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

    for line in csv_reader:
        csv_writer.writerow(line)




import csv

with open('new_nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)



import csv

with open('new_nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)



import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)




import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])




import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_nome.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)




import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_nome.csv', 'w') as new_file:
        fieldnome = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnome=fieldnome, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)





import csv

with open('nome.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_nome.csv', 'w') as new_file:
        fieldnome = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnome=fieldnome, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
