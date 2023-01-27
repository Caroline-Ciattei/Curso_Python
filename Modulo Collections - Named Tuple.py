"""
Módulo Collections - Named (nomeada) Tuple

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parãmetros.

"""
# Recap tupla
tupla = (1, 2, 3)
print(tupla[1])

# Importando 
from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')


# Forma 3 - Declaração Named Tuple -  Mais adequada

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

# Acessando dados

# Forma 1

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome


# Forma 2

print(ray.idade) # idade
print(ray.raça) # raça
print(ray.nome) # nome


print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))