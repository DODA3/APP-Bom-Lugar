import pandas as pd

# Lendo o arquivo e ajustando as linhas e colunas conforme necessário
df = pd.read_excel("vendas.xlsx", skiprows=4).iloc[:, 1:]

# Criando a tabela pivotada
df_pivot = df.pivot_table(index=["CODIGO", "DESCRICAO"], columns="FIL", values="TOT.VENDA", aggfunc="sum")

# Resetando o índice para melhor visualização
df_pivot.reset_index(inplace=True)

# Renomeando as colunas das filiais
df_pivot.rename(columns={35: "loja1", 36: "loja2", 37: "loja3"}, inplace=True)

# Removendo as duas últimas colunas
df_pivot = df_pivot.iloc[:, :-2]

# Salvando o DataFrame pivotado em um arquivo Excel
df_pivot.to_excel("vendas_pivot.xlsx", index=False)

print("Arquivo 'vendas_pivot.xlsx' salvo com sucesso!")

import pandas as pd
import streamlit as st

# Carregar os dados
df_pivot = pd.read_excel("vendas_pivot.xlsx")

# Substituir valores None/NaN por 0 para evitar problemas na filtragem
df_pivot.fillna(0, inplace=True)

# Criar inputs interativos para definir os valores e operadores de comparação
valor_loja1 = st.number_input("Digite o valor para loja1:", min_value=0, value=100)
comparacao_loja1 = st.selectbox("Escolha a comparação para loja1:", [">=", "<="])

valor_loja2 = st.number_input("Digite o valor para loja2:", min_value=0, value=0)
comparacao_loja2 = st.selectbox("Escolha a comparação para loja2:", [">=", "<="])

valor_loja3 = st.number_input("Digite o valor para loja3:", min_value=0, value=0)
comparacao_loja3 = st.selectbox("Escolha a comparação para loja3:", [">=", "<="])

# Construir filtros usando eval() para interpretar as comparações corretamente
filtro_loja1 = df_pivot.eval(f"loja1 {comparacao_loja1} @valor_loja1")
filtro_loja2 = df_pivot.eval(f"loja2 {comparacao_loja2} @valor_loja2")
filtro_loja3 = df_pivot.eval(f"loja3 {comparacao_loja3} @valor_loja3")

# Aplicar o filtro final combinando as condições corretamente
df_filtrado = df_pivot[filtro_loja1 & filtro_loja2 & filtro_loja3]

# Exibir os dados filtrados
st.title("Comparativo de Vendas por Filial")
st.dataframe(df_filtrado)
