"""
 Estruturas Lógicas: and (e), or (ou), not (não), is (é)

 Operadores unários:
    - not
 Operadores binários:
    - and, or, is
 Regras de funcionamento:

 Para o 'and', ambos os valores precisam ser True.
 Para o 'or', um ou outro valor precisa ser True.
 Para o 'not', o valor booleano é invertido.
 Para o 'is', o valor é comparado com um segundo.(comparação)

#  istitle()- Primeira letra da variável em maiúscula.
 obs: title()- Colocar 1 letra em maiúsculo.
"""
ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail.")

