import random
print("Apostas da Mega Sena, cada jogo custa R$ 4,50")

quantidade_matrizes = int(input("Digite a quantidade de jogos que você deseja gerar: "))

apostas = 4.50
total_apostas = quantidade_matrizes*apostas 

for i in range(quantidade_matrizes):
    numeros_aleatorios = random.sample(range(1, 61), 6)
    print("Jogo " + str(i+1) + ": " + str(numeros_aleatorios))

print("total gasto com apostas: R$ %.2f" % total_apostas)

