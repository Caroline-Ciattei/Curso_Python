"""
 Estrutura condicionais
 if(Se), else(Se não), elif- Junção do else if(Se não, se ) só existe em python.
# Em Java e C o elif seria else if.
 # Identação vai ser sempre 4 espaços. 
"""

idade = 18

"""
# Estrutura condicional if, else, em C

if(idade < 18){
    printf("Menor de idade");
}

# Estrutura condicional if, else, em Java
 if(idade < 18){
    System.out.println("Menor de idade");
 }
 else{
    System.out.println("Maior de idade");
 }
"""
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')

if idade > 18:
    print('Maior de idade')

if idade == 18:
    print('Tem 18 anos')

if idade == 26:
    print('tem 26 anos')


