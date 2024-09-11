#Partindo de uma lista de palavras qualquer, como:
palavras = ["python", "mercafacil", "código", "web", "programação"]

#Crie um código que seja capaz de encontrar e exibir 
#a maior e a menor palavra da lista 
#(em número de caracteres)

#minha resposta:

def maior_menor():
    maior_palavra = palavras[0]
    menor_palavra = palavras[0]

    for palavra in palavras:

        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        if len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    print("A maior palavra é:", maior_palavra)
    print("A menor palavra é:", menor_palavra)

maior_menor()
        


#resolução:
"""
palavras = ["python", "asimov", "código", "web", "programação"]

def encontrar_maior_menor_palavra(palavras):

    maior_palavra = max(palavras, key=len)
    menor_palavra = min(palavras, key=len)
    
    print(f"A maior palavra é '{maior_palavra}' com {len(maior_palavra)} caracteres.")
    print(f"A menor palavra é '{menor_palavra}' com {len(menor_palavra)} caracteres.")


encontrar_maior_menor_palavra(palavras)

"""
