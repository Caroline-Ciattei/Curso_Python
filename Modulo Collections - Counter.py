"""
Modulo Collections - Counter (Contador)

Collections -> High-perfomance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

""" 

# realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualqier iterável, aqui usamos uma lista 
lista = [1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 45, 45, 66, 43, 34]


# Utilizando o  Counter

res = Counter(lista)

print(type(res))

print(res)

# Counter({3: 6, 1: 5, 4: 3, 2: 2, 45: 2, 66: 1, 43: 1, 34: 1})

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou um valor a quantidade de ocorrências.

# Exemplo 2

from collections import Counter

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


# Exemplo 3

texto = 'O céu está cheio de estrelas.'

palavras = texto.split()
print(palavras)

# Encontrando as 5 palavras com mais ocorrência no texto
print(texto.most_common(5))