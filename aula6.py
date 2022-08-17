conjunto = {1, 2, 3, 4, 5}
conjunto_2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union (conjunto_2)

conjunto_intersseccao = conjunto.intersection (conjunto_2)

conjunto_diferenca = conjunto.difference (conjunto_2)

conjunto_diferenca2 = conjunto_2.difference (conjunto)

conjunto_diferenca_simetrica = conjunto.symmetric_difference (conjunto_2)
conjunto_diferenca_simetrica2 = conjunto_2.symmetric_difference (conjunto)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4 ,5}

conjunto_subset = conjunto_a.issubset (conjunto_b)
conjunto_superset = conjunto_b.issuperset (conjunto_a)

#remover duplicidade

lista = ['gato', 'gato', 'cachorro', 'cachorro', 'boi', 'boi']

conjunto_animais = set (lista)

lista = list (conjunto_animais)






