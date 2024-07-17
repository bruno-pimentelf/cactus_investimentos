# Calculadora de Investimentos 🌵 - Instituto Cactus

Esta aplicação, desenvolvida em Streamlit, permite aos funcionários do Instituto Cactus calcular quanto precisam aportar por mês, bem como outras variáveis financeiras, a depender de algumas variáveis de entrada.

## Funcionalidades

- **Valor Futuro (FV)**: Calcula o valor futuro de um investimento com base no valor presente, pagamentos periódicos, taxa de juros e número de períodos.
- **Valor Presente (PV)**: Calcula o valor presente de um investimento com base no valor futuro, pagamentos periódicos, taxa de juros e número de períodos.
- **Pagamento Mensal (PMT)**: Calcula o pagamento mensal necessário para alcançar um valor futuro desejado com base na taxa de juros e número de períodos.

## Como usar

1. **Clone o repositório**:
    ```sh
    git clone https://github.com/bruno-pimentelf/cactus_investimentos.git
    cd cactus_investimentos
    ```

2. **Instale as dependências**:
    Certifique-se de ter o Streamlit instalado. Se não tiver, instale-o usando:
    ```sh
    pip install streamlit
    ```

3. **Execute a aplicação**:
    ```sh
    streamlit run investment_app.py
    ```

4. **Navegue até a aplicação**:
    Abra o navegador e vá até o endereço exibido no terminal (geralmente `http://localhost:8501`).

## Estrutura do Projeto

- `investment_app.py`: Contém o código principal da aplicação Streamlit.

## Exemplos de Uso

### Valor Futuro
- **Valor Presente (PV)**: 1000
- **Pagamento por Período (PMT)**: 100
- **Taxa de Juros (decimal)**: 0.05 (para 5%)
- **Número de Períodos (N)**: 10

### Valor Presente
- **Valor Futuro (FV)**: 2000
- **Pagamento por Período (PMT)**: 100
- **Taxa de Juros (decimal)**: 0.05 (para 5%)
- **Número de Períodos (N)**: 10

### Pagamento Mensal
- **Valor Presente (PV)**: 1000
- **Taxa de Juros (decimal)**: 0.05 (para 5%)
- **Número de Períodos (N)**: 10

## Contribuindo

Se desejar contribuir com o projeto, sinta-se à vontade para fazer um fork do repositório e enviar pull requests.

## Licença

Este projeto está licenciado sob os termos da licença MIT.

## Contato

Para mais informações, entre em contato com [Bruno Pimentel](mailto:seuemail@exemplo.com).

---

**Nota**: Esta aplicação foi desenvolvida para fins educacionais e pode não cobrir todos os casos de uso financeiro. Utilize com cautela.
