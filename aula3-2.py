a = int (input ('Primeiro bimestre: '))
b = int (input ('Segundo bimestre: '))
c = int (input ('Terceiro bimestre: '))
d = int (input ('Quarto bimestre: '))

media = (a+b+c+d) / 4
print ('média: {}'.format (media))

if a <= 10 and b <= 10 and c <= 10 and d <= 10: 
    if media >= 7:
            print ('Parabéns! Você foi aprovado!')
    else:
        print ('Que pena! Você foi reprovado!')
else:
    print ('Valores inválidos')