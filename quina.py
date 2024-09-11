import random
print("Apostas da Quina, cada jogo custa R$ 2,50")

quantidade_matrizes = int(input("Digite a quantidade de jogos que você deseja gerar: "))

apostas = 2.50
total_apostas = quantidade_matrizes*apostas 

for i in range(quantidade_matrizes):
    numeros_aleatorios = random.sample(range(1, 81), 5)
    print("Jogo " + str(i+1) + ": " + str(numeros_aleatorios))

print("total gasto com apostas: R$ %.2f" % total_apostas)

