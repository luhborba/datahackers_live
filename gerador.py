import pandas as pd
import random
from datetime import datetime, timedelta

# Definindo as opções para os selectboxes
produtos = [
    "TV",
    "Notebook",
    "Celular",
    "Tablet",
    "PC",
    "Geladeira",
    "Fogão",
    "Microondas",
]
categorias = ["Eletrodomesticos", "Informática"]
formas_pagamento = [
    "Dinheiro",
    "Cartão de Crédito",
    "Cartão de Debito",
    "Boleto",
    "Pix",
]

# Lista para armazenar os registros
registros = []


data_inicial = datetime.strptime("2024-03-01", "%Y-%m-%d")
data_final = datetime.strptime("2024-04-25", "%Y-%m-%d")
delta = data_final - data_inicial

for i in range(delta.days + 1):
    data_atual = data_inicial + timedelta(days=i)
    num_vendas = random.randint(1, 10)  # número aleatório de vendas por dia
    for _ in range(num_vendas):
        produto = random.choice(
            [
                "TV",
                "Notebook",
                "Celular",
                "Tablet",
                "PC",
                "Geladeira",
                "Fogão",
                "Microondas",
            ]
        )
        categoria = random.choice(["Eletrodomesticos", "Informática"])
        preco = round(random.uniform(50, 2000), 2)
        quantidade = random.randint(1, 10)
        forma_pagamento = random.choice(
            ["Dinheiro", "Cartão de Crédito", "Cartão de Debito", "Boleto", "Pix"]
        )
        data_venda = data_atual.strftime("%d/%m/%Y")  # Formato DD/MM/YYYY
        registros.append(
            [produto, categoria, preco, quantidade, forma_pagamento, data_venda]
        )

# Criando o DataFrame
df = pd.DataFrame(
    registros,
    columns=[
        "Produtos",
        "Categorias",
        "Preço",
        "Quantidade",
        "Forma de Pagamento",
        "DataVenda",
    ],
)

# Salvando o DataFrame em um arquivo CSV
df.to_csv("data/vendas.csv", index=False)
