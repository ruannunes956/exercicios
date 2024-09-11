#Neste exercício, você possui duas listas de Python. 
#Cada lista representa os gastos do mês de dois amigos, 
#João e Pedro. Cada valor na lista
#representa o gasto em uma das semanas do mês:

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [100, 400, 500, 700]


#Seu objetivo é encontrar quem gastou mais dinheiro 
#ao longo do mês, João ou Pedro. Para isso,
#crie um código em Python que responda a essa pergunta.


#minha resposta:
def calc_gastos(gastos_joao, gastos_pedro):
    
    total_joao = sum(gastos_joao)
    total_pedro = sum(gastos_pedro)
    if sum(gastos_joao) > sum(gastos_pedro):
        print(f"Os {gastos_joao=} foram maiores: {total_joao}")
    elif sum(gastos_pedro) > sum(gastos_joao):
        print(f"Os {gastos_pedro=} foram maiores: {total_pedro}")
    else:
        print("Os dois gastaram o mesmo")


calc_gastos(gastos_joao, gastos_pedro)


"""
#resolução:

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")
"""


#o que eu queria ter feito:
"""
def calc_gastos(gastos):

    totais = {nome: sum(valores) for nome, valores in gastos.items()}

    (nome1, total1), (nome2, total2) = totais.items()
    
    if total1 > total2:
        print(f"Os gastos de {nome1} foram maiores: {total1}")
    elif total2 > total1:
        print(f"Os gastos de {nome2} foram maiores: {total2}")
    else:
        print(f"Os dois gastaram o mesmo valor: {total1}")

gastos = {
    "João": [300, 500, 200, 800],
    "Pedro": [100, 400, 500, 700]
}

calc_gastos(gastos)
"""
