import pandas as pd
import streamlit as st

# Carregar dados e garantir que os nomes das colunas estejam corretos
df_folha = pd.read_excel("DADOS.xlsm", sheet_name="FOLHA-ADM", usecols="B:T", dtype=str)

# Limpar espaços extras nos nomes das colunas (caso existam)
df_folha.columns = df_folha.columns.str.strip()

# Exibir a folha de pagamento no Streamlit
st.title("Folha de Pagamento")
st.write("Visualizando dados da folha de pagamento.")

# Exibir todas as colunas carregadas
st.dataframe(df_folha)  # Mostra a tabela interativa no Streamlit