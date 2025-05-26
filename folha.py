import pandas as pd
import streamlit as st

# Carregar dados
try:
    df_folha = pd.read_excel("DADOS.xlsm", sheet_name="FOLHA-ADM", usecols="B:T", dtype=str)
    df_folha.columns = df_folha.columns.str.strip()  # Remover espaços extras nos nomes das colunas
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o nome e o caminho do arquivo.")
    st.stop()

# Converter a coluna %S/F para formato percentual
coluna_percentual = "%S/F"
if coluna_percentual in df_folha.columns:
    df_folha[coluna_percentual] = df_folha[coluna_percentual].astype(float) * 100

# Exibir a folha de pagamento no Streamlit
st.title("Folha de Pagamento")
st.write("Visualizando dados da folha de pagamento.")

# Exibir todas as colunas carregadas com formatação
df_folha_formatado = df_folha.style.format({coluna_percentual: "{:.2f}%"})
st.dataframe(df_folha_formatado, height=500)  # Mostra a tabela interativa no Streamlit
