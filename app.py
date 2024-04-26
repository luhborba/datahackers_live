import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.express as px


@st.cache_data
def carregar_dados():
    return pd.read_csv("data/vendas.csv")


def main():
    st.set_page_config(
        page_title="Sistema de Vendas - DH",
        page_icon=":bar_chart:",
        layout="wide",
    )
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.title("Sistema de Vendas - DH")
    data_atual = datetime.now().strftime("%d/%m/%Y")

    with st.expander("🛒 Finalizar Venda:"):
        with st.form("Registro de Venda"):
            produto = st.selectbox(
                "Selecione o Produto",
                [
                    "TV",
                    "Notebook",
                    "Celular",
                    "Tablet",
                    "PC",
                    "Geladeira",
                    "Fogão",
                    "Microondas",
                ],
                index=None,
                placeholder="Escolha o Produto",
            )
            categoria = st.selectbox(
                "Selecione a Categoria",
                ["Eletrodomesticos", "Informática"],
                index=None,
                placeholder="Escolha a Categoria",
            )
            preco = st.number_input("Preço R$", value=0.0)
            quantidade = st.number_input("Quantidade", value=0)
            forma_pagamento = st.selectbox(
                "Forma de Pagamento",
                ["Dinheiro", "Cartão de Crédito", "Cartão de Debito", "Boleto", "Pix"],
                index=None,
                placeholder="Escolha a Forma de Pagamento",
            )
            salvar = st.form_submit_button("Registrar Venda")

            if salvar:
                try:
                    df = carregar_dados()
                    novo_registro = pd.DataFrame(
                        [
                            [
                                produto,
                                categoria,
                                preco,
                                quantidade,
                                forma_pagamento,
                                data_atual,
                            ]
                        ],
                        columns=[
                            "Produtos",
                            "Categorias",
                            "Preço",
                            "Quantidade",
                            "Forma de Pagamento",
                            "DataVenda",
                        ],
                    )
                    df_final = pd.concat([df, novo_registro])
                    df_final.to_csv("data/vendas.csv", index=False)
                except:
                    df = pd.DataFrame(
                        [
                            [
                                produto,
                                categoria,
                                preco,
                                quantidade,
                                forma_pagamento,
                                data_atual,
                            ]
                        ],
                        columns=[
                            "Produtos",
                            "Categorias",
                            "Preço",
                            "Quantidade",
                            "Forma de Pagamento",
                            "DataVenda",
                        ],
                    )
                    df.to_csv("data/vendas.csv", index=False)

                st.success("Venda Registrada com Sucesso!")

    with st.expander("Listar Vendas:"):
        try:
            df = carregar_dados()
            data_filtro = st.date_input("Filtro Data da Venda", value=None)
            if data_filtro:
                data_filtro = data_filtro.strftime("%d/%m/%Y")
                df = df[df["DataVenda"] == data_filtro]

            st.dataframe(df)
        except:
            st.warning("Nenhuma Venda Registrada!")

    with st.expander("Dashboard Vendas"):
        try:
            df = carregar_dados()

            # Gráfico: Distribuição de vendas por categoria
            vendas_por_categoria = df["Categorias"].value_counts()
            plt.figure(figsize=(8, 5))
            plt.bar(vendas_por_categoria.index, vendas_por_categoria.values)
            plt.title("Distribuição de Vendas por Categoria")
            plt.xlabel("Categoria")
            plt.ylabel("Total de Vendas")
            plt.xticks(rotation=45)
            st.pyplot()
            st.divider()

            # Gráfico: Vendas por produtos
            vendas_por_produto = df["Produtos"].value_counts()
            plt.figure(figsize=(8, 5))
            plt.bar(vendas_por_produto.index, vendas_por_produto.values)
            plt.title("Vendas por Produto")
            plt.xlabel("Produto")
            plt.ylabel("Total de Vendas")
            plt.xticks(rotation=45)
            st.pyplot()
            st.divider()

            # Gráfico: Total de vendas por dia (usando plotly)
            vendas_por_dia = df["DataVenda"].value_counts().sort_index()
            fig = px.line(x=vendas_por_dia.index, y=vendas_por_dia.values, markers=True)
            fig.update_layout(
                title="Total de Vendas por Dia",
                xaxis_title="Data",
                yaxis_title="Total de Vendas",
                xaxis=dict(tickangle=-45),
                width=800,
                height=500,
                xaxis_rangeslider_visible=True,
            )
            st.plotly_chart(fig, use_container_width=True)
        except:
            st.warning("Nenhuma Venda Registrada!")


if __name__ == "__main__":
    main()
