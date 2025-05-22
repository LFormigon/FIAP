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

#Desafio Aula 02 (Fazer uma tabela como no exercicio anterior só que com os dados mais atualizados, E deixa as unidades de federação com as letras inclinidas com algum grau)

#Basicamente a Biblioteca matplotlib é uma biblioteca que nos auxilia na visualização de dados, Portanto, vamos utilizar varias vezes

import matplotlib.pyplot as plt

import matplotlib.ticker as ticker



#Axis seria um "eixo" para as tabelas (StrMethodFormatter) seria a formatação da tabela

#Kind (tipo de tabela)  figsize (tamanho da tabela)

axis = dados.plot(x='Unidade da Federação', y='2021/Ago', kind='bar', figsize=(9,6))

#em Axis estamos formantando a tabela para aparecer somente 2 casas após o '.' e exibindo os valores corretos apos a ','

axis.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.2f}'))

# em Axis na nossa tabela o campo "x" seria nossa unidade de federação (nome dos estados) caso eu queria deixar os nomes apresentado com alguma inclinição de grau esse seria o metado:

axis.set_xticklabels(axis.get_xticklabels(), rotation=85)


#Definindo o nome da nossa tabela

plt.title('Tabela da Federeixuim')

#Exibindo o nome da nossa Tabela
plt.show()

#Desafio Aula 02 (Fazer uma tabela como no exercicio anterior só que com os dados mais atualizados, E deixa as unidades de federação com as letras inclinidas com algum grau)

#Basicamente a Biblioteca matplotlib é uma biblioteca que nos auxilia na visualização de dados, Portanto, vamos utilizar varias vezes

import matplotlib.pyplot as plt

import matplotlib.ticker as ticker



#Axis seria um "eixo" para as tabelas (StrMethodFormatter) seria a formatação da tabela

#Kind (tipo de tabela)  figsize (tamanho da tabela)

axis = dados.plot(x='Unidade da Federação', y='2021/Ago', kind='bar', figsize=(9,6))

#em Axis estamos formantando a tabela para aparecer somente 2 casas após o '.' e exibindo os valores corretos apos a ','

axis.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.2f}'))

# em Axis na nossa tabela o campo "x" seria nossa unidade de federação (nome dos estados) caso eu queria deixar os nomes apresentado com alguma inclinição de grau esse seria o metado:

axis.set_xticklabels(axis.get_xticklabels(), rotation=85)


#Definindo o nome da nossa tabela

plt.title('Tabela da Federeixuim')

#Exibindo o nome da nossa Tabela
plt.show()

#Selecionado as colunas no qual eu quero trabalhar (O comando .head por padrão ele vai trazar as 5 primeiras linhas para que possamos trabalho
#porem, podemos aumentar a quantida de linhas caso desejar dentro do parametro)

dados[["2008/Ago", "2008/Set"]].head ()
