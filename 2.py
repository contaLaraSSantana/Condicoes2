#Faça um algoritmo que receba um valor de uma compra e receba o numero de
#prestações, apresente o valor das prestações sem juros. Se o valor for maior
#da prestação for maior que 500 diga que o usuário não consegue pagar.

v = int(input('Digite o valor da compra:'))
p = int(input('Digite o número de prestações sem juros:'))
conta = v/p

if conta > 500:
    print("O usuário não consegue pagar, pois o valor será de ",conta)
else:
    print("O usuário consegue pagar, pois o valor será de ",conta)