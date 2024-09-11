#Vamos para o último desafio: crie uma função que
#retorna uma letra do alfabeto, dado o seu índice.
#Por exemplo, o índice 1 deve retornar a letra "A",
#o índice 2 deve retornar a letra "B" e assim por diante.
#Caso o índice esteja acima ou abaixo dos limites do
#alfabeto, a função deve retornar um string vazio.

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def achar_letra(indice):
    if 1 <= indice <= 26:
        return (alfabeto[indice - 1])
    return ''
    
print(achar_letra(28))

#resolução:
"""
def indice_do_alfabeto(indice):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 1 <= indice <= 26:
        return alfabeto[indice - 1]
    else:
        return ''

print(indice_do_alfabeto(1))
# output: "A"

print(indice_do_alfabeto(3))
# output: "C"

print(indice_do_alfabeto(30))
# output: ""
"""









