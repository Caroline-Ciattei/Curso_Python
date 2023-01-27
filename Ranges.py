"""
Ranges

 - Precisamos conhecer o loop for para usar os ranges.
 - Precisamos conhecer os ranges para trabalhar melhor com loops for.

 Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
 mas sim de maneira especificada.

 Formas gerais:
 # Forma 1

 range(valor_de_parada)

 Obs: valor_de_parada não inclusive (início padrão 0, ou especificado pelo usuário, e passo de 1 em 1).

# Exemplo de Forma 1
for num in range(11):
    print(num)

# Forma 2
 range(valor_de_início, valor_de_parada)
# Exemplo de Forma 2
for num in range(1, 11):
    print(num)

# Forma 3
 range(valor_de_início, valor_de_parada, passo)
 Obs: O passo é especificado pelo usuário.
# Exemplo de Forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4 (inverso da Forma 3)
 range(valor_início, valor_de_parada, passo)
 Obs: valor_início é especificado pelo usuário.
# Exemplo de Forma 4
for num in range(10, 0, -1): OBS: Se quiser até o 0, colocar -1 no valor_de_parada e no passo.
    print(num)
# exemplo:
Lista = list(range(10))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
"""