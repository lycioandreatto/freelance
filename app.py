import streamlit as st
import pandas as pd
from datetime import date

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="GELADA EXPRESS",
    page_icon="🍢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ESTILO
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #F4F5F7;
}

[data-testid="stSidebar"] {
    background-color: #22252A;
}

[data-testid="stSidebar"] * {
    color: white;
}

.titulo {
    font-size: 32px;
    font-weight: 800;
    color: #22252A;
    margin-bottom: 0;
}

.subtitulo {
    color: #6B7078;
    font-size: 15px;
    margin-top: -5px;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #E7E8EA;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.card-titulo {
    color: #777D85;
    font-size: 14px;
    font-weight: 600;
}

.card-valor {
    color: #22252A;
    font-size: 28px;
    font-weight: 800;
    margin-top: 5px;
}

.destaque {
    color: #F2660D;
}

.insight {
    background: white;
    padding: 18px;
    border-radius: 14px;
    border-left: 5px solid #F2660D;
    border-top: 1px solid #E7E8EA;
    border-right: 1px solid #E7E8EA;
    border-bottom: 1px solid #E7E8EA;
    margin-bottom: 10px;
}

.mesa-livre {
    background: white;
    border: 2px solid #E7E8EA;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
}

.mesa-ocupada {
    background: #FFF4ED;
    border: 2px solid #F2660D;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
}

div.stButton > button {
    border-radius: 9px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# PRODUTOS INICIAIS
# =========================================================

PRODUTOS_INICIAIS = pd.DataFrame([
    [1, "Espetinho de Carne", "Espetinhos", 12.00, 38, 10],
    [2, "Espetinho de Frango", "Espetinhos", 10.00, 42, 10],
    [3, "Espetinho de Coração", "Espetinhos", 10.00, 25, 8],
    [4, "Espetinho Misto", "Espetinhos", 10.00, 31, 10],
    [5, "Queijo Coalho", "Espetinhos", 10.00, 20, 8],
    [6, "Medalhão de Carne", "Medalhões", 14.00, 18, 5],
    [7, "Medalhão de Frango", "Medalhões", 14.00, 22, 5],
    [8, "Linguiça Toscana", "Espetinhos", 10.00, 30, 10],
    [9, "Pão de Alho", "Acompanhamentos", 7.00, 24, 8],
    [10, "Batata Frita", "Acompanhamentos", 15.00, 16, 5],
    [11, "Coca-Cola Lata", "Bebidas", 5.00, 35, 10],
    [12, "Guaraná Lata", "Bebidas", 5.00, 28, 10],
    [13, "Água Mineral", "Bebidas", 3.00, 40, 10],
    [14, "Itaipava 600ml", "Bebidas", 8.00, 22, 8],
    [15, "Brahma 600ml", "Bebidas", 10.00, 18, 6],
    [16, "Heineken Long Neck", "Bebidas", 7.00, 15, 5],
], columns=[
    "ID",
    "Produto",
    "Categoria",
    "Preço",
    "Estoque",
    "Estoque Mínimo"
])

# =========================================================
# CLIENTES INICIAIS
# =========================================================

CLIENTES_INICIAIS = pd.DataFrame([
    ["Carlos Henrique", "99999-1111", 12, 487.50, "08/09/2026"],
    ["Mariana Souza", "99999-2222", 9, 361.00, "07/09/2026"],
    ["João Pedro", "99999-3333", 8, 298.50, "06/09/2026"],
    ["Ana Paula", "99999-4444", 7, 274.00, "05/09/2026"],
    ["Rafael Santos", "99999-5555", 6, 241.00, "04/09/2026"],
    ["Lucas Oliveira", "99999-6666", 5, 198.50, "03/09/2026"],
], columns=[
    "Cliente",
    "Telefone",
    "Pedidos",
    "Total Gasto",
    "Última Compra"
])

# =========================================================
# VENDAS INICIAIS
# =========================================================

VENDAS_INICIAIS = pd.DataFrame([
    [
        "09/09/2026",
        "Mesa 01",
        "Carlos Henrique",
        86.00,
        "Pix",
        [
            {"produto": "Espetinho de Carne", "quantidade": 3},
            {"produto": "Espetinho de Frango", "quantidade": 2},
            {"produto": "Itaipava 600ml", "quantidade": 1},
            {"produto": "Coca-Cola Lata", "quantidade": 2},
            {"produto": "Água Mineral", "quantidade": 4}
        ]
    ],
    [
        "09/09/2026",
        "Mesa 03",
        "Mariana Souza",
        72.00,
        "Cartão",
        [
            {"produto": "Medalhão de Carne", "quantidade": 1},
            {"produto": "Espetinho de Carne", "quantidade": 1},
            {"produto": "Espetinho de Frango", "quantidade": 2},
            {"produto": "Itaipava 600ml", "quantidade": 1},
            {"produto": "Pão de Alho", "quantidade": 1},
            {"produto": "Coca-Cola Lata", "quantidade": 1},
            {"produto": "Água Mineral", "quantidade": 2}
        ]
    ],
    [
        "09/09/2026",
        "Mesa 05",
        "João Pedro",
        124.00,
        "Pix",
        [
            {"produto": "Batata Frita", "quantidade": 2},
            {"produto": "Medalhão de Carne", "quantidade": 2},
            {"produto": "Espetinho de Carne", "quantidade": 2},
            {"produto": "Espetinho de Frango", "quantidade": 2},
            {"produto": "Itaipava 600ml", "quantidade": 2},
            {"produto": "Coca-Cola Lata", "quantidade": 2},
            {"produto": "Água Mineral", "quantidade": 2}
        ]
    ],
    [
        "09/09/2026",
        "Mesa 07",
        "Ana Paula",
        58.00,
        "Dinheiro",
        [
            {"produto": "Medalhão de Carne", "quantidade": 1},
            {"produto": "Espetinho de Carne", "quantidade": 1},
            {"produto": "Espetinho de Frango", "quantidade": 2},
            {"produto": "Pão de Alho", "quantidade": 1},
            {"produto": "Coca-Cola Lata", "quantidade": 1}
        ]
    ],
    [
        "09/09/2026",
        "Mesa 02",
        "Rafael Santos",
        94.00,
        "Pix",
        [
            {"produto": "Batata Frita", "quantidade": 1},
            {"produto": "Medalhão de Carne", "quantidade": 1},
            {"produto": "Espetinho de Carne", "quantidade": 2},
            {"produto": "Espetinho de Frango", "quantidade": 1},
            {"produto": "Itaipava 600ml", "quantidade": 1},
            {"produto": "Coca-Cola Lata", "quantidade": 2},
            {"produto": "Água Mineral", "quantidade": 1},
            {"produto": "Queijo Coalho", "quantidade": 1}
        ]
    ],
    [
        "08/09/2026",
        "Mesa 04",
        "Lucas Oliveira",
        68.00,
        "Cartão",
        [
            {"produto": "Batata Frita", "quantidade": 1},
            {"produto": "Medalhão de Carne", "quantidade": 1},
            {"produto": "Espetinho de Carne", "quantidade": 1},
            {"produto": "Espetinho de Frango", "quantidade": 1},
            {"produto": "Pão de Alho", "quantidade": 1},
            {"produto": "Coca-Cola Lata", "quantidade": 2}
        ]
    ],
    [
        "08/09/2026",
        "Mesa 06",
        "Carlos Henrique",
        112.00,
        "Pix",
        [
            {"produto": "Batata Frita", "quantidade": 2},
            {"produto": "Medalhão de Carne", "quantidade": 2},
            {"produto": "Espetinho de Carne", "quantidade": 2},
            {"produto": "Espetinho de Frango", "quantidade": 2},
            {"produto": "Pão de Alho", "quantidade": 1},
            {"produto": "Água Mineral", "quantidade": 1}
        ]
    ],
    [
        "08/09/2026",
        "Mesa 01",
        "Mariana Souza",
        79.00,
        "Dinheiro",
        [
            {"produto": "Batata Frita", "quantidade": 1},
            {"produto": "Medalhão de Carne", "quantidade": 1},
            {"produto": "Espetinho de Carne", "quantidade": 1},
            {"produto": "Espetinho de Frango", "quantidade": 2},
            {"produto": "Itaipava 600ml", "quantidade": 1},
            {"produto": "Pão de Alho", "quantidade": 1},
            {"produto": "Água Mineral", "quantidade": 1}
        ]
    ]
], columns=[
    "Data",
    "Mesa",
    "Cliente",
    "Valor",
    "Pagamento",
    "Itens"
])

# =========================================================
# SESSION STATE
# =========================================================

if "produtos" not in st.session_state:
    st.session_state.produtos = PRODUTOS_INICIAIS.copy()

if "clientes" not in st.session_state:
    st.session_state.clientes = CLIENTES_INICIAIS.copy()

if "vendas" not in st.session_state:
    st.session_state.vendas = VENDAS_INICIAIS.copy()

if "pedidos" not in st.session_state:
    st.session_state.pedidos = []

if "mesa_atual" not in st.session_state:
    st.session_state.mesa_atual = None

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# =========================================================
# FUNÇÕES
# =========================================================

def dinheiro(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def total_carrinho():
    return sum(
        item["preco"] * item["quantidade"]
        for item in st.session_state.carrinho
    )


def adicionar_produto(produto):
    for item in st.session_state.carrinho:
        if item["id"] == produto["ID"]:
            item["quantidade"] += 1
            return

    st.session_state.carrinho.append({
        "id": produto["ID"],
        "produto": produto["Produto"],
        "preco": produto["Preço"],
        "quantidade": 1
    })


def remover_produto(index):
    if 0 <= index < len(st.session_state.carrinho):
        st.session_state.carrinho.pop(index)


def finalizar_pedido(mesa, cliente, pagamento):

    if not st.session_state.carrinho:
        return False

    total = total_carrinho()

    itens = []

    for item in st.session_state.carrinho:
        itens.append({
            "produto": item["produto"],
            "quantidade": item["quantidade"]
        })

        mask = st.session_state.produtos["ID"] == item["id"]

        st.session_state.produtos.loc[
            mask,
            "Estoque"
        ] -= item["quantidade"]

    nova_venda = pd.DataFrame([[
        date.today().strftime("%d/%m/%Y"),
        f"Mesa {mesa:02d}",
        cliente.strip() if cliente.strip() else "Consumidor",
        total,
        pagamento,
        itens
    ]], columns=[
        "Data",
        "Mesa",
        "Cliente",
        "Valor",
        "Pagamento",
        "Itens"
    ])

    st.session_state.vendas = pd.concat(
        [
            st.session_state.vendas,
            nova_venda
        ],
        ignore_index=True
    )

    if cliente.strip():

        nome = cliente.strip()

        mask_cliente = (
            st.session_state.clientes["Cliente"].str.lower()
            == nome.lower()
        )

        if mask_cliente.any():

            st.session_state.clientes.loc[
                mask_cliente,
                "Pedidos"
            ] += 1

            st.session_state.clientes.loc[
                mask_cliente,
                "Total Gasto"
            ] += total

            st.session_state.clientes.loc[
                mask_cliente,
                "Última Compra"
            ] = date.today().strftime("%d/%m/%Y")

        else:

            novo_cliente = pd.DataFrame([[
                nome,
                "",
                1,
                total,
                date.today().strftime("%d/%m/%Y")
            ]], columns=[
                "Cliente",
                "Telefone",
                "Pedidos",
                "Total Gasto",
                "Última Compra"
            ])

            st.session_state.clientes = pd.concat(
                [
                    st.session_state.clientes,
                    novo_cliente
                ],
                ignore_index=True
            )

    st.session_state.carrinho = []

    return True


def produtos_vendidos(vendas):

    registros = []

    for _, venda in vendas.iterrows():

        if not isinstance(venda["Itens"], list):
            continue

        for item in venda["Itens"]:

            registros.append({
                "Produto": item["produto"],
                "Quantidade": item["quantidade"]
            })

    if not registros:
        return pd.DataFrame(
            columns=["Produto", "Quantidade"]
        )

    return pd.DataFrame(registros)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:10px 0 25px 0;">
        <div style="font-size:38px;">🍢</div>
        <div style="font-size:22px; font-weight:800; color:white;">
            GELADA EXPRESS
        </div>
        <div style="font-size:12px; color:#F2660D; margin-top:3px;">
            SISTEMA DE GESTÃO
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

pagina = st.sidebar.radio(
    "MENU",
    [
        "Dashboard",
        "Mesas / Pedidos",
        "Produtos",
        "Estoque",
        "Clientes",
        "Vendas"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Demonstração")
st.sidebar.caption("GELADA EXPRESS")
st.sidebar.caption("Versão 1.0")

# =========================================================
# DASHBOARD
# =========================================================

if pagina == "Dashboard":

    st.markdown(
        '<div class="titulo">Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Visão gerencial da GELADA EXPRESS</div>',
        unsafe_allow_html=True
    )

    vendas = st.session_state.vendas.copy()

    vendas["DataConvertida"] = pd.to_datetime(
        vendas["Data"],
        dayfirst=True
    )

    # -----------------------------------------------------
    # FILTRO
    # -----------------------------------------------------

    periodo = st.selectbox(
        "Período analisado",
        [
            "Todo o período",
            "Últimos 7 dias",
            "Últimos 30 dias"
        ]
    )

    if periodo == "Últimos 7 dias":

        data_final = vendas["DataConvertida"].max()
        data_inicial = data_final - pd.Timedelta(days=6)

        vendas_filtradas = vendas[
            (vendas["DataConvertida"] >= data_inicial)
            & (vendas["DataConvertida"] <= data_final)
        ]

    elif periodo == "Últimos 30 dias":

        data_final = vendas["DataConvertida"].max()
        data_inicial = data_final - pd.Timedelta(days=29)

        vendas_filtradas = vendas[
            (vendas["DataConvertida"] >= data_inicial)
            & (vendas["DataConvertida"] <= data_final)
        ]

    else:

        vendas_filtradas = vendas.copy()

    # -----------------------------------------------------
    # INDICADORES
    # -----------------------------------------------------

    faturamento = vendas_filtradas["Valor"].sum()
    pedidos = len(vendas_filtradas)

    ticket_medio = (
        faturamento / pedidos
        if pedidos > 0
        else 0
    )

    clientes_atendidos = vendas_filtradas[
        vendas_filtradas["Cliente"] != "Consumidor"
    ]["Cliente"].nunique()

    produtos_venda = produtos_vendidos(
        vendas_filtradas
    )

    unidades_vendidas = (
        produtos_venda["Quantidade"].sum()
        if not produtos_venda.empty
        else 0
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">FATURAMENTO</div>
                <div class="card-valor">{dinheiro(faturamento)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">PEDIDOS</div>
                <div class="card-valor">{pedidos}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">TICKET MÉDIO</div>
                <div class="card-valor">{dinheiro(ticket_medio)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">CLIENTES</div>
                <div class="card-valor">{clientes_atendidos}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">ITENS VENDIDOS</div>
                <div class="card-valor">{unidades_vendidas}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # -----------------------------------------------------
    # EVOLUÇÃO
    # -----------------------------------------------------

    st.subheader("Evolução do faturamento")

    if not vendas_filtradas.empty:

        faturamento_diario = (
            vendas_filtradas
            .groupby("DataConvertida")["Valor"]
            .sum()
            .sort_index()
        )

        st.line_chart(
            faturamento_diario,
            height=300
        )

    else:

        st.info("Não existem vendas nesse período.")

    # -----------------------------------------------------
    # PAGAMENTO E PRODUTOS
    # -----------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Faturamento por pagamento")

        pagamentos = (
            vendas_filtradas
            .groupby("Pagamento")["Valor"]
            .sum()
            .sort_values(ascending=False)
        )

        if not pagamentos.empty:
            st.bar_chart(
                pagamentos,
                height=280
            )
        else:
            st.info("Sem dados.")

    with col2:

        st.subheader("Produtos mais vendidos")

        if not produtos_venda.empty:

            ranking_produtos = (
                produtos_venda
                .groupby("Produto")["Quantidade"]
                .sum()
                .sort_values(ascending=False)
                .head(8)
            )

            st.bar_chart(
                ranking_produtos,
                height=280
            )

        else:

            st.info("Sem produtos registrados.")

    st.divider()

    # -----------------------------------------------------
    # DESEMPENHO DOS PRODUTOS
    # -----------------------------------------------------

    st.subheader("Desempenho dos produtos")

    if not produtos_venda.empty:

        ranking = (
            produtos_venda
            .groupby("Produto")["Quantidade"]
            .sum()
            .sort_values(ascending=False)
        )

        produto_lider = ranking.index[0]
        quantidade_lider = ranking.iloc[0]

        produto_menor_saida = ranking.index[-1]
        quantidade_menor_saida = ranking.iloc[-1]

        total_unidades = ranking.sum()

        participacao_lider = (
            quantidade_lider / total_unidades * 100
            if total_unidades > 0
            else 0
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-titulo">
                        PRODUTO MAIS VENDIDO
                    </div>
                    <div class="card-valor destaque">
                        {produto_lider}
                    </div>
                    <div style="color:#777D85;">
                        {quantidade_lider} unidades
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-titulo">
                        PARTICIPAÇÃO DO LÍDER
                    </div>
                    <div class="card-valor">
                        {participacao_lider:.1f}%
                    </div>
                    <div style="color:#777D85;">
                        das unidades vendidas
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-titulo">
                        MENOR SAÍDA
                    </div>
                    <div class="card-valor">
                        {produto_menor_saida}
                    </div>
                    <div style="color:#777D85;">
                        {quantidade_menor_saida} unidades
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        tabela_produtos = ranking.reset_index()
        tabela_produtos.columns = [
            "Produto",
            "Quantidade Vendida"
        ]

        st.dataframe(
            tabela_produtos,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("Ainda não existem produtos vendidos.")

    st.divider()

    # -----------------------------------------------------
    # CLIENTES
    # -----------------------------------------------------

    col1, col2 = st.columns([1.3, 1])

    with col1:

        st.subheader("Clientes que mais compram")

        clientes_periodo = vendas_filtradas[
            vendas_filtradas["Cliente"] != "Consumidor"
        ]

        if not clientes_periodo.empty:

            ranking_clientes = (
                clientes_periodo
                .groupby("Cliente")
                .agg(
                    Pedidos=("Valor", "count"),
                    Total=("Valor", "sum")
                )
                .sort_values(
                    "Total",
                    ascending=False
                )
                .head(8)
            )

            ranking_clientes_exibicao = ranking_clientes.copy()

            ranking_clientes_exibicao["Total"] = (
                ranking_clientes_exibicao["Total"]
                .apply(dinheiro)
            )

            st.dataframe(
                ranking_clientes_exibicao,
                use_container_width=True
            )

        else:

            st.info("Nenhum cliente identificado no período.")

    with col2:

        st.subheader("Formas de pagamento")

        if not pagamentos.empty:

            total_pagamentos = pagamentos.sum()

            for pagamento, valor in pagamentos.items():

                percentual = (
                    valor / total_pagamentos * 100
                    if total_pagamentos > 0
                    else 0
                )

                st.write(
                    f"**{pagamento}** — "
                    f"{dinheiro(valor)} "
                    f"({percentual:.1f}%)"
                )

                st.progress(
                    min(percentual / 100, 1.0)
                )

    st.divider()

    # -----------------------------------------------------
    # ESTOQUE
    # -----------------------------------------------------

    st.subheader("Alertas operacionais")

    estoque = st.session_state.produtos.copy()

    estoque_baixo = estoque[
        estoque["Estoque"] <= estoque["Estoque Mínimo"]
    ].copy()

    col1, col2 = st.columns(2)

    with col1:

        if not estoque_baixo.empty:

            st.warning(
                f"{len(estoque_baixo)} produto(s) "
                f"atingiram o estoque mínimo."
            )

            for _, produto in estoque_baixo.iterrows():

                st.write(
                    f"🔴 **{produto['Produto']}** — "
                    f"{produto['Estoque']} unidades "
                    f"(mínimo: {produto['Estoque Mínimo']})"
                )

        else:

            st.success(
                "Nenhum produto atingiu o estoque mínimo."
            )

    with col2:

        if not produtos_venda.empty:

            st.write("**Produtos com maior saída:**")

            for posicao, (produto, quantidade) in enumerate(
                ranking.head(3).items(),
                start=1
            ):

                st.write(
                    f"{posicao}. **{produto}** — "
                    f"{quantidade} unidades"
                )

    # -----------------------------------------------------
    # INSIGHTS
    # -----------------------------------------------------

    st.divider()

    st.subheader("💡 Insights do negócio")

    insights = []

    if pedidos > 0:

        insights.append(
            f"O período registrou **{pedidos} pedidos**, "
            f"gerando **{dinheiro(faturamento)}** "
            f"de faturamento."
        )

        insights.append(
            f"O ticket médio atual é de "
            f"**{dinheiro(ticket_medio)} por pedido**."
        )

    if not produtos_venda.empty:

        insights.append(
            f"O produto com maior saída foi "
            f"**{produto_lider}**, com "
            f"**{quantidade_lider} unidades vendidas**."
        )

    if not pagamentos.empty:

        pagamento_principal = pagamentos.index[0]
        valor_principal = pagamentos.iloc[0]

        percentual_principal = (
            valor_principal / pagamentos.sum() * 100
        )

        insights.append(
            f"**{pagamento_principal}** foi a principal "
            f"forma de pagamento, representando "
            f"**{percentual_principal:.1f}%** do faturamento."
        )

    if clientes_atendidos > 0:

        clientes_com_mais_de_um_pedido = (
            clientes_periodo
            .groupby("Cliente")
            .size()
        )

        recorrentes = (
            clientes_com_mais_de_um_pedido >= 2
        ).sum()

        if recorrentes > 0:

            insights.append(
                f"{recorrentes} cliente(s) realizaram "
                f"mais de um pedido no período, "
                f"indicando recorrência de compra."
            )

    if not estoque_baixo.empty:

        insights.append(
            f"Existem **{len(estoque_baixo)} produto(s)** "
            f"que precisam ser acompanhados para evitar "
            f"falta de estoque."
        )

    if insights:

        for insight in insights:

            st.markdown(
                f"""
                <div class="insight">
                    {insight}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Ainda não existem dados suficientes "
            "para gerar insights."
        )

# =========================================================
# MESAS / PEDIDOS
# =========================================================

elif pagina == "Mesas / Pedidos":

    st.markdown(
        '<div class="titulo">Mesas / Pedidos</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Controle de pedidos em tempo real'
        '</div>',
        unsafe_allow_html=True
    )

    mesas = list(range(1, 11))

    colunas = st.columns(5)

    for indice, mesa in enumerate(mesas):

        ocupada = st.session_state.mesa_atual == mesa

        with colunas[indice % 5]:

            if ocupada:

                st.markdown(
                    f"""
                    <div class="mesa-ocupada">
                        <div style="font-size:25px;">🍢</div>
                        <b>MESA {mesa:02d}</b>
                        <br>
                        <span style="color:#F2660D;">
                            EM ATENDIMENTO
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="mesa-livre">
                        <div style="font-size:25px;">🪑</div>
                        <b>MESA {mesa:02d}</b>
                        <br>
                        <span style="color:#777D85;">
                            Disponível
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            if st.button(
                "Abrir mesa",
                key=f"mesa_{mesa}",
                use_container_width=True
            ):

                st.session_state.mesa_atual = mesa
                st.session_state.carrinho = []

                st.rerun()

    st.divider()

    if st.session_state.mesa_atual is None:

        st.info(
            "Selecione uma mesa para iniciar um pedido."
        )

    else:

        mesa = st.session_state.mesa_atual

        st.subheader(
            f"Pedido — Mesa {mesa:02d}"
        )

        col_produtos, col_pedido = st.columns(
            [1.5, 1]
        )

        with col_produtos:

            st.markdown("### Produtos")

            categorias = sorted(
                st.session_state.produtos["Categoria"]
                .dropna()
                .unique()
                .tolist()
            )

            categoria = st.selectbox(
                "Categoria",
                ["Todas"] + categorias
            )

            produtos = st.session_state.produtos.copy()

            if categoria != "Todas":

                produtos = produtos[
                    produtos["Categoria"] == categoria
                ]

            for _, produto in produtos.iterrows():

                col1, col2, col3 = st.columns(
                    [3, 1, 1]
                )

                with col1:

                    st.write(
                        f"**{produto['Produto']}**"
                    )

                    st.caption(
                        produto["Categoria"]
                    )

                with col2:

                    st.write(
                        dinheiro(produto["Preço"])
                    )

                with col3:

                    if st.button(
                        "+",
                        key=f"add_{produto['ID']}"
                    ):

                        adicionar_produto(produto)
                        st.rerun()

        with col_pedido:

            st.markdown("### Pedido atual")

            if not st.session_state.carrinho:

                st.info(
                    "Nenhum produto adicionado."
                )

            else:

                for indice, item in enumerate(
                    st.session_state.carrinho
                ):

                    subtotal = (
                        item["preco"]
                        * item["quantidade"]
                    )

                    col1, col2, col3 = st.columns(
                        [3, 1, 1]
                    )

                    with col1:

                        st.write(
                            f"**{item['produto']}**"
                        )

                    with col2:

                        st.write(
                            f"{item['quantidade']}x"
                        )

                    with col3:

                        st.write(
                            dinheiro(subtotal)
                        )

                    if st.button(
                        "Remover",
                        key=f"remover_{indice}"
                    ):

                        remover_produto(indice)
                        st.rerun()

                st.divider()

                st.markdown(
                    f"""
                    <div style="
                        font-size:24px;
                        font-weight:800;
                        text-align:right;
                        color:#F2660D;
                    ">
                        TOTAL: {dinheiro(total_carrinho())}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write("")

                cliente = st.text_input(
                    "Cliente",
                    placeholder="Nome do cliente"
                )

                pagamento = st.selectbox(
                    "Forma de pagamento",
                    [
                        "Pix",
                        "Cartão",
                        "Dinheiro"
                    ]
                )

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        "Finalizar pedido",
                        type="primary",
                        use_container_width=True
                    ):

                        finalizar_pedido(
                            mesa,
                            cliente,
                            pagamento
                        )

                        st.session_state.mesa_atual = None

                        st.success(
                            "Pedido finalizado com sucesso!"
                        )

                        st.rerun()

                with col2:

                    if st.button(
                        "Cancelar",
                        use_container_width=True
                    ):

                        st.session_state.carrinho = []
                        st.session_state.mesa_atual = None

                        st.rerun()

# =========================================================
# PRODUTOS
# =========================================================

elif pagina == "Produtos":

    st.markdown(
        '<div class="titulo">Produtos</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Cadastro e gerenciamento do cardápio'
        '</div>',
        unsafe_allow_html=True
    )

    produtos_editados = st.data_editor(
        st.session_state.produtos,
        use_container_width=True,
        hide_index=True,
        disabled=["ID"],
        column_config={
            "Preço": st.column_config.NumberColumn(
                "Preço",
                format="R$ %.2f"
            ),
            "Estoque": st.column_config.NumberColumn(
                "Estoque",
                min_value=0
            ),
            "Estoque Mínimo": st.column_config.NumberColumn(
                "Estoque Mínimo",
                min_value=0
            )
        },
        key="editor_produtos"
    )

    st.session_state.produtos = produtos_editados.copy()

# =========================================================
# ESTOQUE
# =========================================================

elif pagina == "Estoque":

    st.markdown(
        '<div class="titulo">Estoque</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Acompanhamento dos produtos e alertas de reposição'
        '</div>',
        unsafe_allow_html=True
    )

    produtos = st.session_state.produtos.copy()

    estoque_baixo = produtos[
        produtos["Estoque"] <= produtos["Estoque Mínimo"]
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Produtos cadastrados",
            len(produtos)
        )

    with col2:

        st.metric(
            "Itens em estoque",
            int(produtos["Estoque"].sum())
        )

    with col3:

        st.metric(
            "Estoque baixo",
            len(estoque_baixo)
        )

    st.divider()

    if not estoque_baixo.empty:

        st.warning(
            f"{len(estoque_baixo)} produto(s) "
            "precisam de reposição."
        )

        st.dataframe(
            estoque_baixo,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.success(
            "Todos os produtos estão com estoque adequado."
        )

    st.divider()

    st.subheader("Estoque atual")

    st.dataframe(
        produtos,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Preço": st.column_config.NumberColumn(
                "Preço",
                format="R$ %.2f"
            )
        }
    )

# =========================================================
# CLIENTES
# =========================================================

elif pagina == "Clientes":

    st.markdown(
        '<div class="titulo">Clientes</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Relacionamento e frequência dos clientes'
        '</div>',
        unsafe_allow_html=True
    )

    clientes = st.session_state.clientes.copy()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Clientes cadastrados",
            len(clientes)
        )

    with col2:

        st.metric(
            "Pedidos registrados",
            int(clientes["Pedidos"].sum())
        )

    with col3:

        st.metric(
            "Valor movimentado",
            dinheiro(clientes["Total Gasto"].sum())
        )

    st.divider()

    st.subheader("Clientes mais assíduos")

    clientes_ordenados = clientes.sort_values(
        "Pedidos",
        ascending=False
    )

    st.dataframe(
        clientes_ordenados,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Total Gasto": st.column_config.NumberColumn(
                "Total Gasto",
                format="R$ %.2f"
            )
        }
    )

    st.divider()

    st.subheader("Novo cliente")

    with st.form("novo_cliente"):

        nome = st.text_input("Nome")
        telefone = st.text_input("Telefone")

        salvar = st.form_submit_button(
            "Cadastrar cliente"
        )

        if salvar:

            if nome.strip():

                novo_cliente = pd.DataFrame([[
                    nome.strip(),
                    telefone.strip(),
                    0,
                    0.00,
                    "-"
                ]], columns=[
                    "Cliente",
                    "Telefone",
                    "Pedidos",
                    "Total Gasto",
                    "Última Compra"
                ])

                st.session_state.clientes = pd.concat(
                    [
                        st.session_state.clientes,
                        novo_cliente
                    ],
                    ignore_index=True
                )

                st.success(
                    "Cliente cadastrado com sucesso."
                )

                st.rerun()

            else:

                st.error(
                    "Informe o nome do cliente."
                )

# =========================================================
# VENDAS
# =========================================================

elif pagina == "Vendas":

    st.markdown(
        '<div class="titulo">Vendas</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">'
        'Histórico das vendas realizadas'
        '</div>',
        unsafe_allow_html=True
    )

    vendas = st.session_state.vendas.copy()

    faturamento = vendas["Valor"].sum()
    quantidade = len(vendas)

    ticket_medio = (
        faturamento / quantidade
        if quantidade > 0
        else 0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Faturamento",
            dinheiro(faturamento)
        )

    with col2:

        st.metric(
            "Pedidos",
            quantidade
        )

    with col3:

        st.metric(
            "Ticket médio",
            dinheiro(ticket_medio)
        )

    st.divider()

    filtro_pagamento = st.selectbox(
        "Filtrar por pagamento",
        [
            "Todos",
            "Pix",
            "Cartão",
            "Dinheiro"
        ]
    )

    if filtro_pagamento != "Todos":

        vendas = vendas[
            vendas["Pagamento"] == filtro_pagamento
        ]

    vendas_exibicao = vendas.copy()

    vendas_exibicao["Itens"] = vendas_exibicao["Itens"].apply(
        lambda itens: ", ".join(
            [
                f"{item['produto']} ({item['quantidade']}x)"
                for item in itens
            ]
        )
        if isinstance(itens, list)
        else ""
    )

    st.dataframe(
        vendas_exibicao,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Valor": st.column_config.NumberColumn(
                "Valor",
                format="R$ %.2f"
            )
        }
    )

    st.divider()

    st.subheader("Resumo por forma de pagamento")

    resumo_pagamento = (
        vendas
        .groupby("Pagamento")["Valor"]
        .sum()
        .sort_values(ascending=False)
    )

    if not resumo_pagamento.empty:

        st.bar_chart(
            resumo_pagamento,
            height=300
        )

    else:

        st.info("Não existem vendas para esse filtro.")
