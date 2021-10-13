cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort() #metodo sort - coloca a lista em ordem alfabetica
print("\nAqui está a lista original (sort) em ordem alfabetica: ")
print(cars)

cars.sort(reverse=True) # coloca a lista ao contrario
print("\nAqui está a lista ao contrario (com metodo reverse): ")
print(cars)

print("\nAqui está uma lista com o metodo sorted, que não altera a lista permanentemente: ")
print(sorted(cars)) # não altera a lista permanentemente

cars.reverse() #reverti para lista original antes de reverse in sort
print("\nAqui está a lista cars novamente: ")
print(cars)

print("\nAqui (utilizando o metodo len) está o numero de carros nessa lista: ")
print(len(cars)) #metodo len conta o numero de itens em uma lista