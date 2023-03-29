nome = input("Qual seu nome?: ") #input metodo para inserir informações via prompt
sobrenome = input("E sobrenome?: ")
mensagem = "Olá %s %s! Seja bem-vindo!" % (nome, sobrenome) #metodo funcional antigo
#metodo novo apartir do python 3.6
mensagem = f"Olá {nome} {sobrenome}. Seja Bem Vindo!"#nesse metodo utilizasse o f a frente da msg e {}
print(mensagem)