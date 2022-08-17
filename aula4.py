a = int (input("Entre com um valor: "))

for num in range(a):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print("Número {} é primo".format(num))
    else:
        print("Número {} não é primo".format(num))
        
b = 0
while a <= 10:
    print (a)
    a += 1
        