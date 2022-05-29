val1 = int (input("- Digite um numero inteiro: "))
val2 = int (input("- Digite um outro número inteiro: "))

maior = []
menor = []

if val1 > val2:
    maior = val1
    menor = val2
else:
    maior = val2
    menor = val1

print('\nValores digitados: Maior: {} e o Menor: {}'.format(maior, menor))

mmc = 0

for k in range (1, maior+1):
    aux = k * menor
    if (aux % maior) == 0:
        mmc = aux

print('\n\n>> MMC: ', mmc)