#Você possui uma loja de computadores. No mês passado, 
#suas vendas subiram significativamente. 
#Então, você calculou a porcentagem de aumento vendas e
#anotou o valor como um número (float) em Python:

aumento_vendas = 32.048701

#Formate o número em duas casas decimais,
#exibindo o seguinte texto:
#"O aumento percentual de vendas foi de 32.05%".

#minha resposta:
print(f'O aumento percentual de venda foi {aumento_vendas:.2f}')

#resolução:

aumento_formatado = "{:.2f}".format(aumento_vendas)
print(f"O aumento percentual de vendas foi de {aumento_formatado}%")
