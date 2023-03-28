def contagem(cont):
    if len(cont) >=8:
        return True
    else:
        return False

cont = (input("Digite seu password: "))
print(contagem(cont))