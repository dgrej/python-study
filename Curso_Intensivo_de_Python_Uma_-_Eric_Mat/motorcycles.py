motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'  # altera a informação [0]
print(motorcycles)  # imprime nova lista alterada [0]

motorcycles.append('dafra')  # o metoro .append() acrescenta itens a lista
print(motorcycles)

# o metodo .insert isere informação a lista em qualquer posição
motorcycles.insert(2, 'kavasaki')
print(motorcycles)

# instrução del - deleta a infomação na posição 1 da lista ou em qualquer posição
del motorcycles[0]
print(motorcycles)

#há os metodos remove e pop para remover itens da lista - remove(usa o nome) / pop não deleta e dá a opção de reutilizar o dado da lista
