#Você fez uma pequena pesquisa de preferência entre
#três produtos A, B e C. Na entrevista, 
#cada entrevistado precisava escolher seu produto 
# preferido. Os votos obtidos nessa pesquisa estão
#representados na lista abaixo:

votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

#Agora, seu objetivo é calcular qual produto foi o mais
#votado. A partir da lista de votos, crie um dicionário 
#onde a chave é cada produto, e o valor é o 
#número de votos que o produto recebeu.

#minha resposta:

import collections

contagem = collections.Counter(votos)
print(contagem)

#solução:
contagem_votos = {}

for produto in votos:
    if produto in contagem_votos:
        contagem_votos[produto] += 1
    else:
        contagem_votos[produto] = 1

print(contagem_votos)

import collections

contagem = collections.Counter(votos)
print(contagem)

