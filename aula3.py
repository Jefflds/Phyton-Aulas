a = int (input ('primeiro valor: '))
b = int (input('segundo valor: '))
c = int (input ('terceiro valor: '))

if a > b and a > c:
    print ('O maior número é: {}'.format(a))
    resto = a % 2
    if resto == 0:
        print('{} é par'.format(a))
    else:
        print('{} é impar'.format(a))
elif b > a and b > c:
    print ('O maior número é: {}'.format(b))
    resto = b % 2
    if resto == 0:
        print('{} é par'.format(b))
    else:
        print('{} é impar'.format(b))
else:
    print ('O maior número é: {}'.format(c))
    resto = c % 2
    if resto == 0:
        print('{} é par'.format(b))
    else:
        print('{} é impar'.format(c))
print ('fim do progama')

