#Calcule a média dos valores dessa lista:
numeros = [10, 20, 30, 40, 50]

#minha resposta
def calc_media(list):
    
    media = sum(list) / len(list)
    print(media)

calc_media(numeros)

#resolução:
soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print("A média dos números é:", media)
