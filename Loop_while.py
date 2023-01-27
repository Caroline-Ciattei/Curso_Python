"""
 Loop while

 Forma geral

 while expressão booleana:
    //execução do loop

 O bloco do while será repetido enquanto a expressão booleana for verdadeira.
 Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.
 
 Exemplo:
 
 num = 5

 num > 5

# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1 -> Evita o loop infinito. 
Obs: Em um loop while, é importante que cuidemos do critério de parada para não causar loop infinito( Trava o software).

# Exemplo 2

reposta = " "

while reposta != sim:
    reposta = input("Já acabou o trabalho?   ")

"""