"""
 Tipo string
"""
 # Em Python, um dado é considerado string sempre que:
 # - Estiver entre áspas simples -> '234' , 'a'.(mais comum)
 # - Estiver entre áspas duplas -> "234" , "True".
 # - Também entre áspas triplas -> '''232''', '''True'''.
 # ex: nome = 'Geek University'

 # print(nome)
 # print(type(nome))
 # \n - usado para pular linha, ex: 'Angelina \nJolie' ou nome= 'Angelina
 # Jolie'.

 # print(nome.split()) -> Transforma em uma lista de strings.
 # ex de split: nome = 'Geek University'
 # ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
 # nome = 15 letras, começando no 0 e terminando na posição 14.

 # print(nome[0:3]) = 'Geek'. -> Slice de string
 # ex: print(nome.split()[0]) -> ['Geek', 'University']
 #                               [   0   ,     1      ]
"""
 [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta.
"""
# ex: print(nome[::-1])

# Inversão de String Pythônico - print(nome[::-1])
# print(nome.replace('G', 'P'))
# ex: nome = 'Ana'
# print(nome[::-1])
# resulatdo = 'Ana' -> Palíndromo.