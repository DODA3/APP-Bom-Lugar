import pandas as pd
import streamlit as st

# Carregar dados
try:
    df_folha = pd.read_excel("DADOS.xlsm", sheet_name="FOLHA-ADM", usecols="B:T", dtype=str)
    df_folha.columns = df_folha.columns.str.strip()  # Remover espaços extras nos nomes das colunas
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o nome e o caminho do arquivo.")
    st.stop()

# Converter colunas para formato de moeda com 2 casas decimais
colunas_moeda = ["PROVENTOS", "BASE DO INSS", "ENCARGOS", "FGTS", "PICPAY BENEFÍCIOS",
                 "PICPAY ASSIDUIDADE", "PLANO DE SAÚDE", "VALE TRANSPORTE",
                 "TOTAL", "HORAS EXTRAS", "FATURAMENTO"]

for coluna in colunas_moeda:
    if coluna in df_folha.columns:
        df_folha[coluna] = df_folha[coluna].astype(float).round(2).map("R$ {:,.2f}".format)

# Converter a coluna %S/F para formato percentual com 2 casas decimais
coluna_percentual = "%S/F"
if coluna_percentual in df_folha.columns:
    df_folha[coluna_percentual] = df_folha[coluna_percentual].astype(float).round(4) * 100
    df_folha[coluna_percentual] = df_folha[coluna_percentual].map("{:.2f}%".format)

# Exibir a folha de pagamento no Streamlit
st.title("Folha de Pagamento")
st.write("Visualizando dados da folha de pagamento com valores formatados.")

# Exibir a tabela com valores formatados
st.dataframe(df_folha, height=500)  # Mostra a tabela interativa no Streamlit
