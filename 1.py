#Desenvolva um programa que recebe do usuário, o placar de um jogo de
# futebol (os gols de cada time) e informa se o resultado foi um empate,
# se a vitória foi do primeiro time ou do segundo time.

gol1 = int(input('Digite os gols do primeiro time:'))
gol2 = int(input('Digite os gols do segundo time:'))

if gol1 > gol2:
    print("Vitória do primeiro time")
elif gol2 > gol1:
    print("Vitória do segundo time")
else:
    print("Empate")