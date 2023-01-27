"""
Funções com retorno

OBS 1: Em Python, qunado uma função não retorna valor, o retorno é None.

OBS 2: Funções Python que retornam valores, devem retornar estes valores com
a palavra reservada return.

OBS 3: Não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemospassar a execução da função para outras funções.
"""

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

# Exemplo função 

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')  

# Vamos retornar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')  

print(f'Retorno: {quadrado_de_7()}')

# Retornando a primeira função

def diz_oi(): # Mais adequado
    return 'Oi'

print(diz_oi())

# Ou

def diz_oi():
    print('Oi') 
    
diz_oi()

alguem = 'Pedro!'

diz_oi()
print(alguem)

"""
OBS 4: Sobre a palavra reservada return 

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos
valores;
"""
# Exemplo 1 -  Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('Estou sendo executado após o retorno....')
    return 'Oi!'
    print('Estou sendo executado após o retorno....') # Nunca vai ser executado, pois return
#finaliza a função

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns;

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos
#valores;

def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico (aleatório, mas pode ter repetição) entre 0 e 1
    valor = random()
    if valor > 0.5: # Ou if random() > 0.5
        return 'Cara'
    return 'Coroa'

print(joga_moeda()) 

# Erros comuns na utilização do retorno, que na verdade é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False # É desnecessário o else.
    
print(eh_impar())
