import pandas as pd #1ª célula

dados = pd.read_csv('A150850189_28_143_208.csv', encoding='ISO-8859-1', skiprows=3, sep=';', skipfooter=12, thousands='.', decimal=',', engine='python' ) #2ª célula

#Desafio

dados['2008/Ago'].mean()


dados.plot(x='Unidade da Federação', y='2008/Ago')

#Basicamente a Biblioteca matplotlib é uma biblioteca que nos auxilia na visualização de dados, Portanto, vamos utilizar varias vezes

import matplotlib.pyplot as plt

import matplotlib.ticker as ticker

#Kind (tipo de tabela)  figsize (tamanho da tabela)

axis = dados.plot(x='Unidade da Federação', y='2008/Ago', kind='bar', figsize=(9,6))

#Axis seria um "eixo" para as tabelas (StrMethodFormatter) seria a formatação da tabela

axis.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.2f}'))


#Definindo o nome da nossa tabela

plt.title('Tabela da Federeixuim')

#Exibindo o nome da nossa Tabela
plt.show()