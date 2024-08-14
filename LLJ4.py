import streamlit as st
st.title("Calcule o ano, mês e dia")
st.sidebar.header("Preciso de infromações: ")
nascimento = st.sidebar.number_input("Qual seu ano de nascimento?",min_value=1900,
                                     max_value=2100,step=1)
atual = st.sidebar.number_input('informe o ano atual? ',min_value=1900,
                                     max_value=2100,step=1)
calcular_bottom = st.sidebar.button("Calcular")
if calcular_bottom:
    ano = atual - nascimento
    mes = ano * 12
    dia = ano * 365
    st.success('f Voce tem {ano} anos, {mes} meses e {dia} dias aproximadamente')
