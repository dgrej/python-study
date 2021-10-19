#exemplo 3 do livro introdução python3 - pg 31 e32
print ("Insira um número! para finalizar deixe em branco e aperte enter!")

total = 0
count = 0
while True:
    line = input("Número: ")
    if line:
        try:
            number = float(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
if count:
    print("\n Números =", count, "\n Soma = %.2f" %(total), "\n Media = %.2f" %(total /count))
