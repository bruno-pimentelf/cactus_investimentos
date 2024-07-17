import streamlit as st

st.set_page_config(page_title="Investimentos Cactus", page_icon="🌵")
def calculadora_investimento(fv=None, pv=None, pmt=None, taxa=None, n_periodos=None, calc='fv'):
    if calc == 'fv':
        if pv is not None and taxa is not None and n_periodos is not None and pmt is not None:
            fv = pv * (1 + taxa) ** n_periodos + pmt * (((1 + taxa) ** n_periodos - 1) / taxa)
        elif pv is not None and taxa is not None and n_periodos is not None:
            fv = pv * (1 + taxa) ** n_periodos
        else:
            raise ValueError("Parâmetros insuficientes para calcular o valor futuro.")
        return fv
    
    elif calc == 'pmt':
        if pv is not None and taxa is not None and n_periodos is not None and fv is not None:
            pmt = (fv - pv * (1 + taxa) ** n_periodos) / (((1 + taxa) ** n_periodos - 1) / taxa)
        else:
            raise ValueError("Parâmetros insuficientes para calcular o pagamento.")
        return pmt
    
    elif calc == 'taxa':
        raise NotImplementedError("Cálculo da taxa é complexo e requer métodos iterativos.")
    
    elif calc == 'n_periodos':
        raise NotImplementedError("Cálculo do número de períodos é complexo e requer métodos iterativos.")
    
    else:
        raise ValueError("Tipo de cálculo inválido especificado.")

# Aplicativo Streamlit
st.title("Calculadora de Investimentos 🌵 - Instituto Cactus")
st.markdown("Esta calculadora ajuda a determinar o valor futuro ou o pagamento mensal de um investimento com base nos dados fornecidos.")

tipo_calc = st.selectbox("Selecione o Tipo de Cálculo", ['Valor Futuro', 'Pagamento Mensal'])

if tipo_calc == 'Valor Futuro':
    st.markdown("### Valor Futuro")
    st.markdown("O valor futuro (FV) é o valor que um investimento terá em uma data futura baseada em uma taxa de juros especificada.")
    pv = st.number_input("Valor Presente (PV)", min_value=0.0, format="%f", help="O valor atual do seu investimento. Exemplo: 1000")
    pmt = st.number_input("Pagamento por Período (PMT)", min_value=0.0, format="%f", help="O valor que você paga em cada período. Exemplo: 100")
    taxa = st.number_input("Taxa de Juros (decimal)", min_value=0.0, max_value=1.0, format="%f", help="A taxa de juros por período (em decimal). Exemplo: 0.05 para 5%")
    n_periodos = st.number_input("Número de Períodos (N)", min_value=0, format="%d", help="O número de períodos durante os quais o investimento é feito. Exemplo: 10")
    if st.button("Calcular Valor Futuro"):
        resultado = calculadora_investimento(pv=pv, pmt=pmt, taxa=taxa, n_periodos=n_periodos, calc='fv')
        st.write(f"Valor Futuro: {resultado:.2f}")

elif tipo_calc == 'Pagamento Mensal':
    st.markdown("### Pagamento Mensal")
    st.markdown("O pagamento mensal (PMT) é o valor que você precisa aportar a cada período para atingir um valor futuro desejado.")
    pv = st.number_input("Valor Presente (PV)", min_value=0.0, format="%f", help="O valor atual do seu investimento. Exemplo: 1000")
    fv = st.number_input("Valor Futuro (FV)", min_value=0.0, format="%f", help="O valor futuro desejado do seu investimento. Exemplo: 2000")
    taxa = st.number_input("Taxa de Juros (decimal)", min_value=0.0, max_value=1.0, format="%f", help="A taxa de juros por período (em decimal). Exemplo: 0.05 para 5%")
    n_periodos = st.number_input("Número de Períodos (N)", min_value=0, format="%d", help="O número de períodos durante os quais o investimento é feito. Exemplo: 10")
    if st.button("Calcular Pagamento Mensal"):
        resultado = calculadora_investimento(pv=pv, fv=fv, taxa=taxa, n_periodos=n_periodos, calc='pmt')
        st.write(f"Pagamento por Período: {resultado:.2f}")

# Execute a aplicação com: streamlit run investment_app.py
