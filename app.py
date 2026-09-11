import streamlit as st
import pandas as pd
from datetime import datetime, date
import random

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
# CORES / ESTILO
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
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
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

    .produto-card {
        background: white;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #E7E8EA;
        margin-bottom: 10px;
    }

    div.stButton > button {
        border-radius: 9px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# DADOS INICIAIS
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
])

PRODUTOS_INICIAIS.columns = [
    "ID", "Produto", "Categoria", "Preço", "Estoque", "Estoque Mínimo"
]


CLIENTES_INICIAIS = pd.DataFrame([
    ["Carlos Henrique", "99999-1111", 12, 487.50, "08/09/2026"],
    ["Mariana Souza", "99999-2222", 9, 361.00, "07/09/2026"],
    ["João Pedro", "99999-3333", 8, 298.50, "06/09/2026"],
    ["Ana Paula", "99999-4444", 7, 274.00, "05/09/2026"],
    ["Rafael Santos", "99999-5555", 6, 241.00, "04/09/2026"],
    ["Lucas Oliveira", "99999-6666", 5, 198.50, "03/09/2026"],
])

CLIENTES_INICIAIS.columns = [
    "Cliente", "Telefone", "Pedidos", "Total Gasto", "Última Compra"
]


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================

if "produtos" not in st.session_state:
    st.session_state.produtos = PRODUTOS_INICIAIS.copy()

if "clientes" not in st.session_state:
    st.session_state.clientes = CLIENTES_INICIAIS.copy()

if "pedidos" not in st.session_state:
    st.session_state.pedidos = []

if "mesa_atual" not in st.session_state:
    st.session_state.mesa_atual = None

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

if "vendas" not in st.session_state:

    st.session_state.vendas = pd.DataFrame([
        ["09/09/2026", "Mesa 01", "Carlos Henrique", 86.00, "Pix"],
        ["09/09/2026", "Mesa 03", "Mariana Souza", 72.00, "Cartão"],
        ["09/09/2026", "Mesa 05", "João Pedro", 124.00, "Pix"],
        ["09/09/2026", "Mesa 07", "Ana Paula", 58.00, "Dinheiro"],
        ["09/09/2026", "Mesa 02", "Rafael Santos", 94.00, "Pix"],
        ["08/09/2026", "Mesa 04", "Lucas Oliveira", 68.00, "Cartão"],
        ["08/09/2026", "Mesa 06", "Carlos Henrique", 112.00, "Pix"],
        ["08/09/2026", "Mesa 01", "Mariana Souza", 79.00, "Dinheiro"],
    ], columns=[
        "Data", "Mesa", "Cliente", "Valor", "Pagamento"
    ])


# =========================================================
# FUNÇÕES
# =========================================================

def dinheiro(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def total_carrinho():
    return sum(
        item["preco"] * item["quantidade"]
        for item in st.session_state.carrinho
    )


def adicionar_produto(produto):
    encontrado = False

    for item in st.session_state.carrinho:
        if item["id"] == produto["ID"]:
            item["quantidade"] += 1
            encontrado = True
            break

    if not encontrado:
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

    nova_venda = pd.DataFrame([[
        date.today().strftime("%d/%m/%Y"),
        f"Mesa {mesa:02d}",
        cliente if cliente else "Consumidor",
        total,
        pagamento
    ]], columns=[
        "Data", "Mesa", "Cliente", "Valor", "Pagamento"
    ])

    st.session_state.vendas = pd.concat(
        [st.session_state.vendas, nova_venda],
        ignore_index=True
    )

    for item in st.session_state.carrinho:

        mask = st.session_state.produtos["ID"] == item["id"]

        st.session_state.produtos.loc[
            mask,
            "Estoque"
        ] -= item["quantidade"]

    st.session_state.carrinho = []

    return True


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:10px 0 25px 0;
    ">
        <div style="font-size:38px;">🍢</div>
        <div style="
            font-size:22px;
            font-weight:800;
            color:white;
        ">
            GELADA EXPRESS
        </div>
        <div style="
            font-size:12px;
            color:#F2660D;
            margin-top:3px;
        ">
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
        '<div class="subtitulo">Visão geral do movimento da GELADA EXPRESS</div>',
        unsafe_allow_html=True
    )

    vendas = st.session_state.vendas

    faturamento = vendas["Valor"].sum()
    pedidos = len(vendas)
    ticket = faturamento / pedidos if pedidos else 0

    produtos_estoque_baixo = len(
        st.session_state.produtos[
            st.session_state.produtos["Estoque"]
            <= st.session_state.produtos["Estoque Mínimo"]
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">FATURAMENTO</div>
                <div class="card-valor">{dinheiro(faturamento)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">PEDIDOS</div>
                <div class="card-valor">{pedidos}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">TICKET MÉDIO</div>
                <div class="card-valor">{dinheiro(ticket)}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-titulo">ESTOQUE BAIXO</div>
                <div class="card-valor destaque">{produtos_estoque_baixo}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2 = st.columns([1.5, 1])

    with col1:

        st.subheader("Faturamento por dia")

        vendas_chart = vendas.copy()

        vendas_chart["Data"] = pd.to_datetime(
            vendas_chart["Data"],
            dayfirst=True
        )

        diario = (
            vendas_chart
            .groupby("Data")["Valor"]
            .sum()
            .sort_index()
        )

        st.line_chart(diario)

    with col2:

        st.subheader("Formas de pagamento")

        pagamentos = (
            vendas
            .groupby("Pagamento")["Valor"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(pagamentos)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Produtos em destaque")

        produtos_demo = pd.DataFrame([
            ["Espetinho de Carne", 87],
            ["Espetinho de Frango", 74],
            ["Itaipava 600ml", 61],
            ["Medalhão de Carne", 48],
            ["Coca-Cola Lata", 44],
        ], columns=["Produto", "Quantidade"])

        st.bar_chart(
            produtos_demo.set_index("Produto")
        )

    with col2:

        st.subheader("Clientes mais assíduos")

        clientes = st.session_state.clientes.copy()

        clientes = clientes.sort_values(
            "Pedidos",
            ascending=False
        )

        st.dataframe(
            clientes.head(5),
            use_container_width=True,
            hide_index=True
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
        '<div class="subtitulo">Controle de pedidos em tempo real</div>',
        unsafe_allow_html=True
    )

    # -------------------------
    # SELEÇÃO DA MESA
    # -------------------------

    mesas = list(range(1, 11))

    cols = st.columns(5)

    for i, mesa in enumerate(mesas):

        ocupada = (
            st.session_state.mesa_atual == mesa
        )

        with cols[i % 5]:

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

            categoria = st.selectbox(
                "Categoria",
                [
                    "Todas",
                    *sorted(
                        st.session_state.produtos[
                            "Categoria"
                        ].unique()
                    )
                ]
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
                        f"{produto['Categoria']}"
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

                for i, item in enumerate(
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
                        key=f"remove_{i}"
                    ):
                        remover_produto(i)
                        st.rerun()

                st.divider()

                total = total_carrinho()

                st.markdown(
                    f"""
                    <div style="
                        font-size:24px;
                        font-weight:800;
                        text-align:right;
                        color:#F2660D;
                    ">
                        TOTAL: {dinheiro(total)}
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

                        st.success(
                            "Pedido finalizado com sucesso!"
                        )

                        st.session_state.mesa_atual = None

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
        '<div class="subtitulo">Cadastro e gerenciamento do cardápio</div>',
        unsafe_allow_html=True
    )

    st.data_editor(
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

    st.info(
        "Nesta demonstração os dados são mantidos apenas durante a sessão. "
        "Na próxima etapa podemos salvar tudo automaticamente no Google Sheets."
    )


# =========================================================
# ESTOQUE
# =========================================================

elif pagina == "Estoque":

    st.markdown(
        '<div class="titulo">Estoque</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Acompanhamento dos produtos e alertas de reposição</div>',
        unsafe_allow_html=True
    )

    produtos = st.session_state.produtos.copy()

    baixo = produtos[
        produtos["Estoque"]
        <= produtos["Estoque Mínimo"]
    ]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Produtos cadastrados",
            len(produtos)
        )

    with c2:
        st.metric(
            "Itens em estoque",
            int(produtos["Estoque"].sum())
        )

    with c3:
        st.metric(
            "Estoque baixo",
            len(baixo)
        )

    st.divider()

    if len(baixo) > 0:

        st.warning(
            f"{len(baixo)} produto(s) precisam de reposição."
        )

        st.dataframe(
            baixo,
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
        '<div class="subtitulo">Relacionamento e frequência dos clientes</div>',
        unsafe_allow_html=True
    )

    clientes = st.session_state.clientes.copy()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Clientes cadastrados",
            len(clientes)
        )

    with c2:
        st.metric(
            "Pedidos registrados",
            int(clientes["Pedidos"].sum())
        )

    with c3:
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

                novo = pd.DataFrame([[
                    nome,
                    telefone,
                    0,
                    0.00,
                    "-"
                ]], columns=clientes.columns)

                st.session_state.clientes = pd.concat(
                    [
                        st.session_state.clientes,
                        novo
                    ],
                    ignore_index=True
                )

                st.success(
                    "Cliente cadastrado!"
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
        '<div class="subtitulo">Histórico das vendas realizadas</div>',
        unsafe_allow_html=True
    )

    vendas = st.session_state.vendas.copy()

    faturamento = vendas["Valor"].sum()
    quantidade = len(vendas)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Faturamento",
            dinheiro(faturamento)
        )

    with c2:
        st.metric(
            "Pedidos",
            quantidade
        )

    with c3:
        st.metric(
            "Ticket médio",
            dinheiro(
                faturamento / quantidade
                if quantidade
                else 0
            )
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
            vendas["Pagamento"]
            == filtro_pagamento
        ]

    st.dataframe(
        vendas.sort_index(
            ascending=False
        ),
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

    resumo = (
        vendas
        .groupby("Pagamento")["Valor"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(resumo)
