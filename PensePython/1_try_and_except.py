#exercio pag 27 - bookintrod linguagem python
#exempli manipulaçãobasica de exceção - try and except
s = input ("enter an integer: ")
try:
    i = int (s)
    print ("valid integer entered: ", i)
except ValueError as err:
    print(err)



