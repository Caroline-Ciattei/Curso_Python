"""
 Loop -> Estrutura de repetição.

 For -> Uma dessas estruturas

 C ou Java
 for(int i = 0; i < 10; i++){
    //execução do loop
    }

 Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

 Exemplos de iteráveis:
 - String
   nome = 'Geek University'
 - Lista
   lista = [1, 3, 5. 7, 9]
 - Range
   numeros = range(1,10)

"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista.

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando em uma range)
""" 
 range( valor_inicial, valor_final)
 OBS: O valor final não é inclusive, ou seja, até o penúltimo número.
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10 - Não
"""
"""
 Enumerate:
 ((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

 for _, letra in enumerate(nome):
    print(nome)
Obs: Quando não precisamos de um valor, podemos descartá-lo utilizando underline (_).
 for indice, letra in enumerate(nome):
    print(nome[indice])
#for numero in range(1, 10):
#    print(numero)
""" 

for indice, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd):
    print(f'Imprimindo {n}')

soma = 0
for n in range(1, qtd +1):
    num = int(input(f'Infome o {n}/{qtd} valor:   '))
    soma = soma + num
print(f'A soma é {soma}.')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')
# end -> mostrar a variável em uma única linha, ou seja, não pulando linha.
"""
Exemplos em for:
nome = 'Geek'
nome + 'University -> Exemplo de concatenação.
 'Geek University'
 # Para imprimir um emoji precisamos do unicode dele.
 Original : U+1F60D
 Modificado : U0001F60D - Vai ser utilizada como string.
"""
for _ in range(3):
    for num in range(1, 10):
        print('\U0001F60D' * num)