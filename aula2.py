from re import sub

from traitlets import observe
import traitlets


a = int (input ('Entre com o primeiro valor: '))
b = int (input ('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


#print ('Subtração: ' + str (subtracao))

#print ('Multiplicaçaõ: ' + str (multiplicacao))

#print ('Divisão: ' + str (int (divisao)))

#print ('Resto: ' + str (resto))

resultado = ('Soma: {soma}. \n Subtração: {sub}. '
       '\n multiplicação: {multiplicacao}.' 
       '\n Divisão: {divisao}.'
       '\n Resto {resto}.'.format(soma = soma,
                                        sub = subtracao,
                                        multiplicacao = multiplicacao,
                                        divisao = divisao,
                                        resto = resto))

print (resultado)
