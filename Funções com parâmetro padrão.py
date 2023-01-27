"""
Funções com Parâmetro padrão (Default Paramters)
- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

"""
# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
# print(quadrado()) # TypeError

def exponencial(numero = 4, potencia = 2):
    return numero ** potencia


print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva á potência informada pelo usuário, substituindo o 2.

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potencia. Então 
# será calculada a esta potência.

#print(exponencial())


# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# Erro!
#def teste(num = 2, potencia): # Teria que ser -> teste(potencia, numero = 2)
   # return num ** potencia

#print(teste(6))
# Outros exemplos

def soma(num1 =5, num2 = 4):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) 
print(soma()) 


# Exemplo mais complexo

def mostra_informacao(nome = 'Geek', instrutor = False):
    if nome  == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}.'

print(mostra_informacao())
print(mostra_informacao(instrutor = True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome = 'Stephany'))

# Por quê utlizar parâmetros com valor default?
"""
- Nos permite ser mais flexíveis nas funções;
- Evita erro com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

"""
# Quais tipos de dados podemos utlizar como valores default para parâmetros?
"""
- Qualquer tipo de dado:
    - números, strings, booleanos, listas, dicionários, funções e etc;

"""

def diz_oi():
    print('Oi')

variavel = diz_oi

variavel()

# exemplos de funções como parâmetro

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun = soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões.....

# Variáveis  globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o memso nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # Variável local - reconhecida somente dentro do bloco que foi definida.
    return f'Olá {prof}'

print(diz_oi()) 

#print(prof) -> NameError

# ATENÇÂO com variáveis globais (Se puder evitar, evite!)
"""
total = 0

def incremente():
    total = total + 1 # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incremente())

"""
total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador # nonlocal não é uma variável local e nem global.

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

# OBS: A função dentro() só é reconhecida dentro da função fora().
