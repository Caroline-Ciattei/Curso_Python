"""
 Escopo de variáveis
 Dois casos de escopo: 
 1 - Variáveis globais;
   -Seu escopo compreende, todo o programa.

 2 - Variáveis locais;
   -Seu escopo está limitado ao bloco onde foi declarada.

 Para declarar variáveis em Python fazemos:
 nome_da_variavel = valor_da_variavel

 Pyhton é uma linguagem de tipagem dinâmica. Isso significa que 
 ao declararmos uma variável, nós não colocamos o tipo de dado dela.
 Esse tipo é inferido ao atribuirmos o valor à mesma.

 Exemplo em C: 
 int numero = 42;

 Exemplo em Java:
 int numero = 42;
 num = 42 # Exemplo de variável global.
 print(num)
 print(type(num))

# Exemplo de escopo local:
 numero = 2
if numero > 10:
    novo = numero + 10
    print(novo)
    
print(novo)
"""