#Faça um programa que solicite dois números ao usuário (com decimais)
# Em seguida solicite que o usuário informe o resultado das quatro operações
# matemáticas (adição, subtração, multiplicação e divisão)

n1 = float(input('Digite um número com decimais:'))
n2 = float(input('Digite mais um número com decimais:'))
result = float(input('Digite qual operação quer utilizar:\n 1-adição \n 2-subtração \n 3-multiplicação \n 4-divisão'))
if result == 1:
    print("O resultado da adição é", n1 + n2)
elif result == 2:
    print("O resultado da subtração é:", n1-n2)
elif result == 3:
    print("O resultado da multiplicação é:", n1 * n2)
else:
    print("O resultado da divisão é:", n1/n2)