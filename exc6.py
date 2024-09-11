#Crie um script capaz de detectar palíndromos. Um palíndromo é uma palavra que permanece a mesma se for lida de trás para frente,
#como “arara” ou “radar”.

#minha resposta:

def is_palindromo():
    palavra = input('digite a palavra: ')
    if palavra == palavra[::-1]:
        print(f"É palíndromo")
    else:
        print("Não é Palíndromo")

is_palindromo()

#resolução:

palavra = "arara"

palavra_invertida = palavra[::-1]
eh_palindromo = palavra == palavra_invertida

if eh_palindromo:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
