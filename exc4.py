#Nesta atividade, você possui uma lista 
#de números qualquer. Por exemplo:
numeros = [32, 10, 58, 30, 55, 12, 28, 51]
#Seu objetivo é encontrar o segundo maior valor da lista
#(supondo que ela possua pelo menos dois elementos).

#possível resposta
def segundo_maior():
    numeros.sort()
    segundo_maior = numeros[-2]
    print(segundo_maior)

segundo_maior()

#solução:
numeros.sort()
segundo_maior = numeros[-2]

print("O segundo maior valor da lista é:", segundo_maior)

