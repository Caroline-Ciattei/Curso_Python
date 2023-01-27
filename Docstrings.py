"""
Documentando em funções com Docstrings

OBS: Podemos ter acesso á documentação de uma função em Python
utuçizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a função help() -> help(diz_oi())
"""
print(help(print))

# Exemplos

def diz_oi():
    """ Uma função simples que retorna 'Oi!"""
    return 'Oi! ' 

def exponencial(numero, potencia = 2): # Acesso por help(exponencial()) depois de from
    #docstrings import exponencial.
    """
    Função que retorna por padrâo o quadrado de 'numero' ou 'numero' á potência informada.
    : param numero: Número que desejamos gerar o exponencial.
    : param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia 

