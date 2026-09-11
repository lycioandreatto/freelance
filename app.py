import streamlit as st
import pandas as pd
from datetime import date, datetime
from zoneinfo import ZoneInfo


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Aura Beauty Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CORES E ESTILO
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap');

    :root {
        --orange: #E85D2A;
        --orange-dark: #C9471C;
        --cream: #FFF8F3;
        --background: #F5F3F1;
        --white: #FFFFFF;
        --text: #292624;
        --muted: #89817C;
        --border: #E8E2DE;
        --soft-orange: #FFF0E8;
        --green: #3F8A68;
        --soft-green: #EDF7F1;
        --red: #C95555;
        --soft-red: #FCEEEE;
        --yellow: #C58A28;
        --soft-yellow: #FFF7E7;
        --purple: #7565A8;
        --soft-purple: #F1EFF8;
    }


    /* ========================================================
       BASE
       ======================================================== */

    .stApp {
        background: var(--background);
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 125px;
        padding-bottom: 60px;
        padding-left: 55px;
        padding-right: 55px;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }


    /* ========================================================
       MENU SUPERIOR - SAAS
       ======================================================== */

    .topbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999999;

        height: 76px;

        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);

        border-bottom: 1px solid var(--border);

        box-shadow:
            0 4px 18px rgba(45, 37, 32, 0.045);
    }

    .topbar-inner {
        max-width: 1450px;
        height: 76px;
        margin: 0 auto;

        padding: 0 30px;

        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .topbar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        min-width: 210px;
    }

    .topbar-logo {
        width: 39px;
        height: 39px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 11px;

        background: var(--soft-orange);
        color: var(--orange);

        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: 600;

        border: 1px solid #F6D9CB;
    }

    .topbar-brand-name {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: 500;
        color: var(--text);
        line-height: 1;
    }

    .topbar-brand-subtitle {
        margin-top: 4px;

        color: var(--muted);

        font-size: 8px;
        font-weight: 700;

        letter-spacing: 2.1px;
        text-transform: uppercase;
    }


    /* Área do menu horizontal */

    div[data-testid="stHorizontalBlock"] {
        gap: 0.8rem;
    }

    .topbar-nav {
        width: 100%;
    }

    .topbar-nav div[data-testid="stRadio"] {
        margin: 0;
    }

    .topbar-nav div[data-testid="stRadio"] > label {
        display: none;
    }

    .topbar-nav div[role="radiogroup"] {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 4px;

        flex-wrap: nowrap;
    }

    .topbar-nav div[role="radiogroup"] > label {
        min-height: 40px;

        padding: 0 11px;

        border-radius: 10px;
        border: 1px solid transparent;

        display: flex;
        align-items: center;

        cursor: pointer;

        color: #756D68 !important;

        transition:
            background 0.18s ease,
            color 0.18s ease,
            border-color 0.18s ease,
            transform 0.18s ease;
    }

    .topbar-nav div[role="radiogroup"] > label p {
        margin: 0 !important;

        color: #756D68 !important;

        font-family: 'DM Sans', sans-serif !important;
        font-size: 12px !important;
        font-weight: 600 !important;

        white-space: nowrap;
    }

    .topbar-nav div[role="radiogroup"] > label:hover {
        background: #FAF7F5;
        border-color: #EEE7E3;

        transform: translateY(-1px);
    }

    .topbar-nav div[role="radiogroup"] > label:hover p {
        color: var(--orange) !important;
    }

    .topbar-nav div[role="radiogroup"] > label[data-checked="true"] {
        background: var(--soft-orange);
        border-color: #F5D5C5;
    }

    .topbar-nav div[role="radiogroup"] > label[data-checked="true"] p {
        color: var(--orange) !important;
        font-weight: 700 !important;
    }

    .topbar-nav div[role="radiogroup"] > label > div:first-child {
        display: none;
    }


    /* ========================================================
       TIPOGRAFIA
       ======================================================== */

    h1,
    h2,
    h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 500 !important;
        color: var(--text);
        letter-spacing: -0.4px;
    }

    h1 {
        font-size: 39px !important;
        line-height: 1.15 !important;
    }

    h2 {
        font-size: 30px !important;
    }

    h3 {
        font-size: 21px !important;
    }

    p {
        font-family: 'DM Sans', sans-serif;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        line-height: 1.1;
        color: var(--text);
        margin-bottom: 5px;
    }

    .main-subtitle {
        color: var(--muted);
        font-size: 14px;
        margin-bottom: 28px;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 25px;
        margin-top: 32px;
        margin-bottom: 16px;
        color: var(--text);
    }

    .eyebrow {
        color: var(--orange);
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 7px;
    }

    .page-heading {
        font-family: 'Playfair Display', serif;
        font-size: 37px;
        line-height: 1.15;
        color: var(--text);
        margin-bottom: 5px;
    }

    .page-description {
        color: var(--muted);
        font-size: 13px;
        margin-bottom: 28px;
    }


    /* ========================================================
       CABEÇALHOS
       ======================================================== */

    .custom-page-header {
        margin-bottom: 30px;
    }

    .welcome-header {
        margin-bottom: 30px;
    }

    .welcome-header .eyebrow {
        margin-bottom: 8px;
    }

    .welcome-header .welcome-title {
        font-family: 'Playfair Display', serif;
        font-size: 40px;
        line-height: 1.1;
        color: var(--text);
        margin-bottom: 7px;
    }

    .welcome-header .welcome-description {
        color: var(--muted);
        font-size: 14px;
    }


    /* ========================================================
       CARDS / MÉTRICAS
       ======================================================== */

    div[data-testid="stMetric"] {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 19px 20px 17px 20px;
        min-height: 112px;
        box-shadow: 0 2px 8px rgba(45, 37, 32, 0.025);
    }

    div[data-testid="stMetric"]:hover {
        border-color: #DDD3CD;
        box-shadow: 0 5px 18px rgba(45, 37, 32, 0.055);
    }

    div[data-testid="stMetricLabel"] {
        color: var(--muted) !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    div[data-testid="stMetricValue"] {
        color: var(--text) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 28px !important;
        font-weight: 600 !important;
        letter-spacing: -0.7px;
        margin-top: 4px;
    }

    div[data-testid="stMetricDelta"] {
        font-size: 11px !important;
    }


    /* ========================================================
       CONTAINERS
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--white);
        border: 1px solid var(--border);
        border-radius: 14px;
        box-shadow: 0 2px 8px rgba(45, 37, 32, 0.025);
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #DDD5D0;
    }


    /* ========================================================
       BOTÕES
       ======================================================== */

    .stButton > button {
        border-radius: 10px !important;
        border: 1px solid var(--border) !important;
        min-height: 42px;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 13px !important;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: var(--orange) !important;
        color: var(--orange) !important;
    }

    .stButton > button[kind="primary"] {
        background: var(--orange) !important;
        border-color: var(--orange) !important;
        color: #FFFFFF !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: var(--orange-dark) !important;
        border-color: var(--orange-dark) !important;
        color: #FFFFFF !important;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="input"] {
        border-radius: 9px;
    }

    div[data-baseweb="input"] > div {
        border-color: var(--border);
        background: #FFFFFF;
    }

    div[data-baseweb="input"] > div:focus-within {
        border-color: var(--orange);
        box-shadow: 0 0 0 1px var(--orange);
    }

    div[data-baseweb="select"] > div {
        border-radius: 9px;
        border-color: var(--border);
    }

    div[data-baseweb="select"] > div:focus-within {
        border-color: var(--orange);
        box-shadow: 0 0 0 1px var(--orange);
    }

    label[data-testid="stWidgetLabel"] p {
        color: #625A56 !important;
        font-size: 12px !important;
        font-weight: 600 !important;
    }


    /* ========================================================
       DATAFRAMES / TABELAS
       ======================================================== */

    div[data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 12px;
        overflow: hidden;
    }


    /* ========================================================
       ALERTAS
       ======================================================== */

    div[data-testid="stAlert"] {
        border-radius: 11px;
        border-width: 1px;
        font-size: 13px;
    }


    /* ========================================================
       GRÁFICOS
       ======================================================== */

    div[data-testid="stVegaLiteChart"],
    div[data-testid="stArrowVegaLiteChart"] {
        background: transparent;
    }


    /* ========================================================
       ELEMENTOS AUXILIARES
       ======================================================== */

    .small-muted {
        color: var(--muted);
        font-size: 13px;
    }

    .orange-box {
        background: linear-gradient(
            135deg,
            #E85D2A 0%,
            #D94D20 100%
        );
        color: white;
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 8px 22px rgba(232, 93, 42, 0.16);
    }

    .orange-box-title {
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: rgba(255,255,255,0.75);
        margin-bottom: 8px;
    }

    .orange-box-value {
        font-size: 28px;
        font-weight: 600;
        color: white;
    }

    .orange-box-small {
        font-size: 12px;
        color: rgba(255,255,255,0.82);
        margin-top: 5px;
    }

    .insight-box {
        background: var(--soft-orange);
        border: 1px solid #F7D8C9;
        border-left: 3px solid var(--orange);
        border-radius: 11px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }

    .service-name {
        font-family: 'Playfair Display', serif;
        font-size: 21px;
        color: var(--text);
    }

    .service-category {
        color: var(--orange);
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 8px;
    }

    .service-price {
        font-size: 20px;
        font-weight: 600;
        margin-top: 10px;
    }

    .agenda-time {
        font-family: 'DM Sans', sans-serif;
        font-size: 20px;
        font-weight: 600;
        color: var(--text);
    }

    .agenda-client {
        font-size: 14px;
        font-weight: 600;
        color: var(--text);
    }

    .agenda-service {
        font-size: 12px;
        color: var(--muted);
        margin-top: 3px;
    }

    .status-pill {
        display: inline-block;
        padding: 5px 9px;
        border-radius: 20px;
        font-size: 10px;
        font-weight: 700;
        white-space: nowrap;
    }

    .status-confirmado {
        background: var(--soft-green);
        color: var(--green);
    }

    .status-pendente {
        background: var(--soft-yellow);
        color: var(--yellow);
    }

    .status-concluido {
        background: var(--soft-purple);
        color: var(--purple);
    }

    .status-cancelado {
        background: var(--soft-red);
        color: var(--red);
    }

    .section-divider {
        height: 1px;
        background: var(--border);
        margin: 28px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DADOS INICIAIS
# ============================================================

servicos_iniciais = pd.DataFrame(
    [
        ["Unhas Postiças", "Unhas", 85.00, 90],
        ["Alongamento em Gel", "Unhas", 150.00, 120],
        ["Manicure", "Unhas", 35.00, 45],
        ["Pedicure", "Unhas", 40.00, 50],
        ["Sobrancelha", "Sobrancelhas", 35.00, 30],
        ["Design de Sobrancelha", "Sobrancelhas", 55.00, 45],
        ["Lash Lifting", "Cílios", 120.00, 75],
        ["Extensão de Cílios", "Cílios", 160.00, 120],
        ["Manutenção de Cílios", "Cílios", 100.00, 90],
    ],
    columns=[
        "Serviço",
        "Categoria",
        "Preço",
        "Duração"
    ]
)


clientes_iniciais = pd.DataFrame(
    [
        ["Amanda Oliveira", "99999-1001", "08/09/2026", 14, 1280.00],
        ["Juliana Santos", "99999-1002", "07/09/2026", 11, 975.00],
        ["Camila Souza", "99999-1003", "06/09/2026", 9, 820.00],
        ["Mariana Alves", "99999-1004", "05/09/2026", 8, 735.00],
        ["Larissa Lima", "99999-1005", "04/09/2026", 7, 690.00],
        ["Beatriz Costa", "99999-1006", "03/09/2026", 6, 520.00],
        ["Fernanda Rocha", "99999-1007", "02/09/2026", 5, 445.00],
        ["Isabela Martins", "99999-1008", "01/09/2026", 4, 380.00],
        ["Gabriela Ferreira", "99999-1009", "30/08/2026", 4, 355.00],
        ["Rafaela Mendes", "99999-1010", "29/08/2026", 3, 290.00],
        ["Patricia Gomes", "99999-1011", "28/08/2026", 3, 270.00],
        ["Nicole Almeida", "99999-1012", "27/08/2026", 2, 180.00],
    ],
    columns=[
        "Cliente",
        "Telefone",
        "Última Visita",
        "Visitas",
        "Total Gasto"
    ]
)


# ============================================================
# GASTOS INICIAIS
# ============================================================

gastos_iniciais = pd.DataFrame(
    [
        [
            date(2026, 9, 1),
            "Compra de materiais",
            "Materiais",
            "Gasto",
            280.00,
            "Produtos para atendimento"
        ],
        [
            date(2026, 9, 3),
            "Produtos para cílios",
            "Materiais",
            "Gasto",
            190.00,
            "Reposição de estoque"
        ],
        [
            date(2026, 9, 5),
            "Marketing",
            "Marketing",
            "Investimento",
            120.00,
            "Divulgação nas redes sociais"
        ],
        [
            date(2026, 9, 7),
            "Energia elétrica",
            "Despesas fixas",
            "Gasto",
            180.00,
            "Conta de energia"
        ],
        [
            date(2026, 9, 9),
            "Novo equipamento",
            "Equipamentos",
            "Investimento",
            350.00,
            "Equipamento para o studio"
        ]
    ],
    columns=[
        "Data",
        "Descrição",
        "Categoria",
        "Tipo",
        "Valor",
        "Observação"
    ]
)


# ============================================================
# AGENDAMENTOS FICTÍCIOS
# ============================================================

nomes = [
    "Amanda Oliveira",
    "Juliana Santos",
    "Camila Souza",
    "Mariana Alves",
    "Larissa Lima",
    "Beatriz Costa",
    "Fernanda Rocha",
    "Isabela Martins",
    "Gabriela Ferreira",
    "Rafaela Mendes",
    "Patricia Gomes",
    "Nicole Almeida"
]


servicos_lista = [
    "Unhas Postiças",
    "Alongamento em Gel",
    "Manicure",
    "Pedicure",
    "Sobrancelha",
    "Design de Sobrancelha",
    "Lash Lifting",
    "Extensão de Cílios",
    "Manutenção de Cílios"
]


precos = {
    "Unhas Postiças": 85.00,
    "Alongamento em Gel": 150.00,
    "Manicure": 35.00,
    "Pedicure": 40.00,
    "Sobrancelha": 35.00,
    "Design de Sobrancelha": 55.00,
    "Lash Lifting": 120.00,
    "Extensão de Cílios": 160.00,
    "Manutenção de Cílios": 100.00
}


datas = [
    date(2026, 8, 25),
    date(2026, 8, 26),
    date(2026, 8, 27),
    date(2026, 8, 28),
    date(2026, 8, 29),
    date(2026, 8, 30),
    date(2026, 9, 1),
    date(2026, 9, 2),
    date(2026, 9, 3),
    date(2026, 9, 4),
    date(2026, 9, 5),
    date(2026, 9, 6),
    date(2026, 9, 7),
    date(2026, 9, 8),
    date(2026, 9, 9),
    date(2026, 9, 10),
    date(2026, 9, 11),
    date(2026, 9, 12),
    date(2026, 9, 15),
    date(2026, 9, 16),
    date(2026, 9, 17),
    date(2026, 9, 18)
]


horarios = [
    "08:00",
    "09:30",
    "11:00",
    "13:00",
    "14:30",
    "16:00",
    "17:30"
]


agenda_inicial = []

contador = 0


for d in datas:

    quantidade = 6 if d.weekday() < 5 else 4

    for i in range(quantidade):

        nome = nomes[
            contador % len(nomes)
        ]

        servico = servicos_lista[
            (contador * 2) % len(servicos_lista)
        ]

        horario = horarios[i]

        if d < date(2026, 9, 11):

            status = "Concluído"

        elif d == date(2026, 9, 11):

            status = [
                "Confirmado",
                "Confirmado",
                "Pendente",
                "Confirmado",
                "Pendente",
                "Confirmado"
            ][i]

        else:

            status = "Confirmado"

        agenda_inicial.append(
            [
                d,
                horario,
                nome,
                servico,
                precos[servico],
                status
            ]
        )

        contador += 1


agenda_inicial = pd.DataFrame(
    agenda_inicial,
    columns=[
        "Data",
        "Horário",
        "Cliente",
        "Serviço",
        "Valor",
        "Status"
    ]
)


# ============================================================
# FUNÇÕES
# ============================================================

def dinheiro(valor):

    try:
        valor = float(valor)

    except (ValueError, TypeError):

        valor = 0.0

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def saudacao():

    agora = datetime.now(
        ZoneInfo("America/Maceio")
    )

    hora = agora.hour

    if hora < 12:
        return "Bom dia"

    if hora < 18:
        return "Boa tarde"

    return "Boa noite"


def titulo_pagina(titulo, subtitulo):

    st.markdown(
        f"""
        <div class="custom-page-header">
            <div class="eyebrow">AURA BEAUTY STUDIO</div>
            <div class="page-heading">{titulo}</div>
            <div class="page-description">{subtitulo}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def secao(titulo):

    st.markdown(
        f"""
        <div class="section-title">
            {titulo}
        </div>
        """,
        unsafe_allow_html=True
    )


def garantir_colunas_clientes(df):

    df = df.copy()

    colunas = [
        "Cliente",
        "Telefone",
        "Última Visita",
        "Visitas",
        "Total Gasto"
    ]

    for coluna in colunas:

        if coluna not in df.columns:

            if coluna == "Visitas":
                df[coluna] = 0

            elif coluna == "Total Gasto":
                df[coluna] = 0.0

            else:
                df[coluna] = ""

    df["Visitas"] = pd.to_numeric(
        df["Visitas"],
        errors="coerce"
    ).fillna(0)

    df["Total Gasto"] = pd.to_numeric(
        df["Total Gasto"],
        errors="coerce"
    ).fillna(0)

    return df[colunas]


def garantir_colunas_agenda(df):

    df = df.copy()

    colunas = [
        "Data",
        "Horário",
        "Cliente",
        "Serviço",
        "Valor",
        "Status"
    ]

    for coluna in colunas:

        if coluna not in df.columns:

            if coluna == "Valor":
                df[coluna] = 0.0

            else:
                df[coluna] = ""

    df["Valor"] = pd.to_numeric(
        df["Valor"],
        errors="coerce"
    ).fillna(0)

    return df[colunas]


def garantir_colunas_gastos(df):

    df = df.copy()

    colunas = [
        "Data",
        "Descrição",
        "Categoria",
        "Tipo",
        "Valor",
        "Observação"
    ]

    for coluna in colunas:

        if coluna not in df.columns:

            if coluna == "Valor":
                df[coluna] = 0.0

            else:
                df[coluna] = ""

    df["Valor"] = pd.to_numeric(
        df["Valor"],
        errors="coerce"
    ).fillna(0)

    return df[colunas]


def obter_visitas_cliente(df):

    if df.empty:

        return pd.DataFrame(
            columns=[
                "Cliente",
                "Visitas",
                "Gasto"
            ]
        )

    dados = df[
        df["Status"] == "Concluído"
    ].copy()

    if dados.empty:

        return pd.DataFrame(
            columns=[
                "Cliente",
                "Visitas",
                "Gasto"
            ]
        )

    dados["Valor"] = pd.to_numeric(
        dados["Valor"],
        errors="coerce"
    ).fillna(0)

    resultado = (
        dados
        .groupby("Cliente")
        .agg(
            Visitas=("Cliente", "count"),
            Gasto=("Valor", "sum")
        )
        .reset_index()
    )

    return resultado


def status_texto(status):

    if status == "Confirmado":
        return "🟢 Confirmado"

    if status == "Pendente":
        return "🟡 Pendente"

    if status == "Concluído":
        return "🟣 Concluído"

    if status == "Cancelado":
        return "🔴 Cancelado"

    return status


# ============================================================
# SESSION STATE
# ============================================================

if "servicos" not in st.session_state:

    st.session_state.servicos = (
        servicos_iniciais.copy()
    )

else:

    servicos_atual = (
        st.session_state.servicos
    )

    if not isinstance(
        servicos_atual,
        pd.DataFrame
    ):

        st.session_state.servicos = (
            servicos_iniciais.copy()
        )

    else:

        colunas_servicos = [
            "Serviço",
            "Categoria",
            "Preço",
            "Duração"
        ]

        estrutura_valida = all(
            coluna in servicos_atual.columns
            for coluna in colunas_servicos
        )

        if not estrutura_valida:

            st.session_state.servicos = (
                servicos_iniciais.copy()
            )

        else:

            st.session_state.servicos = (
                servicos_atual[
                    colunas_servicos
                ].copy()
            )


if "clientes" not in st.session_state:

    st.session_state.clientes = (
        clientes_iniciais.copy()
    )

else:

    clientes_atual = (
        st.session_state.clientes
    )

    if not isinstance(
        clientes_atual,
        pd.DataFrame
    ):

        st.session_state.clientes = (
            clientes_iniciais.copy()
        )

    else:

        clientes_atual = (
            garantir_colunas_clientes(
                clientes_atual
            )
        )

        st.session_state.clientes = (
            clientes_atual
        )


if "agenda" not in st.session_state:

    st.session_state.agenda = (
        agenda_inicial.copy()
    )

else:

    agenda_atual = (
        st.session_state.agenda
    )

    if not isinstance(
        agenda_atual,
        pd.DataFrame
    ):

        st.session_state.agenda = (
            agenda_inicial.copy()
        )

    else:

        agenda_atual = (
            garantir_colunas_agenda(
                agenda_atual
            )
        )

        st.session_state.agenda = (
            agenda_atual
        )


if "gastos" not in st.session_state:

    st.session_state.gastos = (
        gastos_iniciais.copy()
    )

else:

    gastos_atual = (
        st.session_state.gastos
    )

    if not isinstance(
        gastos_atual,
        pd.DataFrame
    ):

        st.session_state.gastos = (
            gastos_iniciais.copy()
        )

    else:

        gastos_atual = (
            garantir_colunas_gastos(
                gastos_atual
            )
        )

        st.session_state.gastos = (
            gastos_atual
        )


# ============================================================
# MENU SUPERIOR
# ============================================================

topbar_col1, topbar_col2 = st.columns(
    [1.1, 5],
    vertical_alignment="center"
)

with topbar_col1:

    st.markdown(
        """
        <div class="topbar-brand">

            <div class="topbar-logo">
                A
            </div>

            <div>
                <div class="topbar-brand-name">
                    Aura
                </div>

                <div class="topbar-brand-subtitle">
                    Beauty Studio
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with topbar_col2:

    pagina = st.radio(
        "Navegação",
        [
            "⌂  Visão geral",
            "▣  Agenda",
            "＋  Novo agendamento",
            "♡  Clientes",
            "✦  Serviços",
            "R$  Financeiro",
            "↗  Gastos",
            "♧  Fidelização"
        ],
        horizontal=True,
        label_visibility="collapsed"
    )

pagina = (
    pagina
    .replace("⌂  ", "")
    .replace("▣  ", "")
    .replace("＋  ", "")
    .replace("♡  ", "")
    .replace("✦  ", "")
    .replace("R$  ", "")
    .replace("↗  ", "")
    .replace("♧  ", "")
)


# ============================================================
# VISÃO GERAL
# ============================================================

if pagina == "Visão geral":

    st.markdown(
        f"""
        <div class="welcome-header">
            <div class="eyebrow">DASHBOARD</div>
            <div class="welcome-title">
                {saudacao()}, Lilly.
            </div>
            <div class="welcome-description">
                Aqui está um resumo do desempenho do seu studio.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    agenda = garantir_colunas_agenda(
        st.session_state.agenda
    )

    concluidos = agenda[
        agenda["Status"] == "Concluído"
    ].copy()

    faturamento = concluidos["Valor"].sum()

    quantidade_visitas = len(
        concluidos
    )

    ticket = (
        faturamento / quantidade_visitas
        if quantidade_visitas > 0
        else 0
    )

    clientes_ativos = (
        concluidos["Cliente"].nunique()
    )

    data_hoje = date(
        2026,
        9,
        11
    )

    agendamentos_hoje = agenda[
        agenda["Data"] == data_hoje
    ]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Faturamento",
            dinheiro(faturamento)
        )

        st.caption(
            "Serviços concluídos"
        )

    with c2:

        st.metric(
            "Atendimentos",
            quantidade_visitas
        )

        st.caption(
            "Atendimentos realizados"
        )

    with c3:

        st.metric(
            "Ticket médio",
            dinheiro(ticket)
        )

        st.caption(
            "Por atendimento"
        )

    with c4:

        st.metric(
            "Hoje",
            len(agendamentos_hoje)
        )

        st.caption(
            "Agendamentos"
        )

    secao(
        "Agenda de hoje"
    )

    if agendamentos_hoje.empty:

        st.info(
            "Nenhum agendamento para hoje."
        )

    else:

        col1, col2 = st.columns(
            [1.5, 1]
        )

        with col1:

            for _, row in (
                agendamentos_hoje
                .sort_values("Horário")
                .head(5)
                .iterrows()
            ):

                with st.container(
                    border=True
                ):

                    horario_col, dados_col, status_col = st.columns(
                        [0.8, 2.5, 1]
                    )

                    with horario_col:

                        st.markdown(
                            f"""
                            <div class="agenda-time">
                                {row['Horário']}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with dados_col:

                        st.markdown(
                            f"""
                            <div class="agenda-client">
                                {row['Cliente']}
                            </div>
                            <div class="agenda-service">
                                {row['Serviço']} · {dinheiro(row['Valor'])}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with status_col:

                        st.write(
                            status_texto(
                                row["Status"]
                            )
                        )

        with col2:

            faturamento_hoje = (
                agendamentos_hoje[
                    agendamentos_hoje["Status"]
                    != "Cancelado"
                ]["Valor"].sum()
            )

            confirmados = len(
                agendamentos_hoje[
                    agendamentos_hoje["Status"]
                    == "Confirmado"
                ]
            )

            pendentes = len(
                agendamentos_hoje[
                    agendamentos_hoje["Status"]
                    == "Pendente"
                ]
            )

            with st.container(
                border=True
            ):

                st.markdown(
                    "### Resumo do dia"
                )

                st.metric(
                    "Faturamento previsto",
                    dinheiro(
                        faturamento_hoje
                    )
                )

                st.write(
                    f"**{confirmados}** confirmados"
                )

                st.write(
                    f"**{pendentes}** pendentes"
                )

    secao(
        "Desempenho"
    )

    col1, col2 = st.columns(
        [1.4, 1]
    )

    with col1:

        diario = (
            concluidos
            .groupby("Data")["Valor"]
            .sum()
            .reset_index()
        )

        if not diario.empty:

            diario["Data"] = pd.to_datetime(
                diario["Data"]
            )

            with st.container(
                border=True
            ):

                st.markdown(
                    "**Faturamento por dia**"
                )

                st.line_chart(
                    diario.set_index("Data")[
                        "Valor"
                    ],
                    height=280
                )

        else:

            st.info(
                "Ainda não existem dados de faturamento."
            )

    with col2:

        ranking_servicos = (
            concluidos
            .groupby("Serviço")
            .agg(
                Atendimentos=(
                    "Serviço",
                    "count"
                ),
                Faturamento=(
                    "Valor",
                    "sum"
                )
            )
            .sort_values(
                "Faturamento",
                ascending=False
            )
        )

        with st.container(
            border=True
        ):

            st.markdown(
                "**Serviços que mais faturam**"
            )

            if ranking_servicos.empty:

                st.info(
                    "Sem dados."
                )

            else:

                tabela = (
                    ranking_servicos
                    .reset_index()
                    .copy()
                )

                tabela["Faturamento"] = (
                    tabela["Faturamento"]
                    .apply(dinheiro)
                )

                st.dataframe(
                    tabela,
                    use_container_width=True,
                    hide_index=True,
                    height=280
                )

    secao(
        "Insights"
    )

    ranking_servicos = (
        concluidos
        .groupby("Serviço")
        .agg(
            Atendimentos=(
                "Serviço",
                "count"
            ),
            Faturamento=(
                "Valor",
                "sum"
            )
        )
        .sort_values(
            "Faturamento",
            ascending=False
        )
    )

    if not ranking_servicos.empty:

        servico_top = (
            ranking_servicos.index[0]
        )

        faturamento_top = (
            ranking_servicos.iloc[0][
                "Faturamento"
            ]
        )

        cliente_top = (
            concluidos
            .groupby("Cliente")["Valor"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        melhor_cliente = (
            cliente_top.index[0]
        )

        st.success(
            f"**Serviço destaque:** "
            f"{servico_top} lidera o faturamento "
            f"com {dinheiro(faturamento_top)}."
        )

        st.info(
            f"**Cliente de maior valor:** "
            f"{melhor_cliente} é a cliente que "
            f"mais gastou no studio."
        )

        st.info(
            f"**Ticket médio:** "
            f"cada atendimento gera aproximadamente "
            f"{dinheiro(ticket)}."
        )

        st.warning(
            "**Oportunidade comercial:** "
            "oferecer combinações de serviços pode "
            "aumentar o valor de cada atendimento."
        )


# ============================================================
# AGENDA
# ============================================================

elif pagina == "Agenda":

    titulo_pagina(
        "Agenda",
        "Visualize todos os atendimentos do studio."
    )

    agenda = garantir_colunas_agenda(
        st.session_state.agenda
    )

    data_selecionada = st.date_input(
        "Escolha o dia",
        value=date(2026, 9, 11)
    )

    agenda_dia = (
        agenda[
            agenda["Data"] == data_selecionada
        ]
        .sort_values("Horário")
        .copy()
    )

    valor_previsto = (
        agenda_dia[
            agenda_dia["Status"]
            != "Cancelado"
        ]["Valor"].sum()
    )

    confirmados_dia = len(
        agenda_dia[
            agenda_dia["Status"]
            == "Confirmado"
        ]
    )

    pendentes_dia = len(
        agenda_dia[
            agenda_dia["Status"]
            == "Pendente"
        ]
    )

    concluidos_dia = len(
        agenda_dia[
            agenda_dia["Status"]
            == "Concluído"
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Agendamentos",
        len(agenda_dia)
    )

    c2.metric(
        "Confirmados",
        confirmados_dia
    )

    c3.metric(
        "Pendentes",
        pendentes_dia
    )

    c4.metric(
        "Valor previsto",
        dinheiro(valor_previsto)
    )

    secao(
        data_selecionada.strftime(
            "%d/%m/%Y"
        )
    )

    if agenda_dia.empty:

        st.info(
            "Nenhum agendamento para este dia."
        )

    else:

        for _, row in agenda_dia.iterrows():

            with st.container(
                border=True
            ):

                col1, col2, col3 = st.columns(
                    [1, 3, 1]
                )

                with col1:

                    st.markdown(
                        f"""
                        <div class="agenda-time">
                            {row['Horário']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="agenda-client">
                            {row['Cliente']}
                        </div>
                        <div class="agenda-service">
                            {row['Serviço']} · {dinheiro(row['Valor'])}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col3:

                    st.write(
                        status_texto(
                            row["Status"]
                        )
                    )


# ============================================================
# NOVO AGENDAMENTO
# ============================================================

elif pagina == "Novo agendamento":

    titulo_pagina(
        "Novo agendamento",
        "Agende um novo atendimento para sua cliente."
    )

    col1, col2 = st.columns(2)

    with col1:

        nome = st.text_input(
            "Nome da cliente"
        )

        telefone = st.text_input(
            "WhatsApp"
        )

        data_agendamento = st.date_input(
            "Data",
            value=date(2026, 9, 15)
        )

    with col2:

        servico = st.selectbox(
            "Serviço",
            st.session_state.servicos[
                "Serviço"
            ].tolist()
        )

        horario = st.selectbox(
            "Horário",
            [
                "08:00",
                "09:30",
                "11:00",
                "13:00",
                "14:30",
                "16:00",
                "17:30",
                "19:00"
            ]
        )

        status = st.selectbox(
            "Status",
            [
                "Confirmado",
                "Pendente"
            ]
        )

    servico_info = (
        st.session_state.servicos[
            st.session_state.servicos[
                "Serviço"
            ] == servico
        ]
    )

    if not servico_info.empty:

        servico_info = (
            servico_info.iloc[0]
        )

        with st.container(
            border=True
        ):

            st.markdown(
                "### Resumo do atendimento"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    "**Serviço**"
                )

                st.write(
                    servico
                )

            with col2:

                st.write(
                    "**Duração**"
                )

                st.write(
                    f"{servico_info['Duração']} minutos"
                )

            with col3:

                st.write(
                    "**Valor**"
                )

                st.write(
                    dinheiro(
                        servico_info["Preço"]
                    )
                )

    st.write("")

    if st.button(
        "Confirmar agendamento",
        type="primary",
        use_container_width=True
    ):

        if not nome.strip():

            st.error(
                "Informe o nome da cliente."
            )

        else:

            novo = pd.DataFrame(
                [
                    [
                        data_agendamento,
                        horario,
                        nome.strip(),
                        servico,
                        float(
                            servico_info["Preço"]
                        ),
                        status
                    ]
                ],
                columns=[
                    "Data",
                    "Horário",
                    "Cliente",
                    "Serviço",
                    "Valor",
                    "Status"
                ]
            )

            st.session_state.agenda = pd.concat(
                [
                    st.session_state.agenda,
                    novo
                ],
                ignore_index=True
            )

            clientes = (
                garantir_colunas_clientes(
                    st.session_state.clientes
                )
            )

            cliente_existente = (
                nome.strip()
                in clientes["Cliente"].values
            )

            if not cliente_existente:

                novo_cliente = pd.DataFrame(
                    [
                        [
                            nome.strip(),
                            telefone,
                            data_agendamento.strftime(
                                "%d/%m/%Y"
                            ),
                            0,
                            0.00
                        ]
                    ],
                    columns=[
                        "Cliente",
                        "Telefone",
                        "Última Visita",
                        "Visitas",
                        "Total Gasto"
                    ]
                )

                st.session_state.clientes = (
                    pd.concat(
                        [
                            clientes,
                            novo_cliente
                        ],
                        ignore_index=True
                    )
                )

            st.success(
                f"Agendamento de "
                f"{nome.strip()} criado com sucesso."
            )


# ============================================================
# CLIENTES
# ============================================================

elif pagina == "Clientes":

    titulo_pagina(
        "Clientes",
        "Conheça melhor quem frequenta o Aura Beauty Studio."
    )

    clientes = garantir_colunas_clientes(
        st.session_state.clientes
    )

    st.session_state.clientes = clientes

    total_clientes = len(
        clientes
    )

    clientes_recorrentes = len(
        clientes[
            clientes["Visitas"] >= 5
        ]
    )

    gasto_medio = (
        clientes["Total Gasto"].mean()
        if not clientes.empty
        else 0
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Clientes cadastradas",
        total_clientes
    )

    c2.metric(
        "Clientes recorrentes",
        clientes_recorrentes
    )

    c3.metric(
        "Gasto médio por cliente",
        dinheiro(gasto_medio)
    )

    secao(
        "Ranking de clientes"
    )

    ranking = (
        clientes
        .sort_values(
            "Total Gasto",
            ascending=False
        )
        .copy()
    )

    ranking_exibicao = ranking.copy()

    ranking_exibicao[
        "Total Gasto"
    ] = (
        ranking_exibicao[
            "Total Gasto"
        ]
        .apply(dinheiro)
    )

    st.dataframe(
        ranking_exibicao,
        use_container_width=True,
        hide_index=True
    )

    secao(
        "Adicionar cliente"
    )

    c1, c2 = st.columns(2)

    with c1:

        novo_nome = st.text_input(
            "Nome",
            key="novo_cliente_nome"
        )

    with c2:

        novo_telefone = st.text_input(
            "WhatsApp",
            key="novo_cliente_telefone"
        )

    if st.button(
        "Cadastrar cliente",
        type="primary"
    ):

        if not novo_nome.strip():

            st.error(
                "Informe o nome da cliente."
            )

        elif (
            novo_nome.strip()
            in clientes["Cliente"].values
        ):

            st.warning(
                "Essa cliente já está cadastrada."
            )

        else:

            novo_cliente = pd.DataFrame(
                [
                    [
                        novo_nome.strip(),
                        novo_telefone,
                        date.today().strftime(
                            "%d/%m/%Y"
                        ),
                        0,
                        0.00
                    ]
                ],
                columns=[
                    "Cliente",
                    "Telefone",
                    "Última Visita",
                    "Visitas",
                    "Total Gasto"
                ]
            )

            st.session_state.clientes = (
                pd.concat(
                    [
                        clientes,
                        novo_cliente
                    ],
                    ignore_index=True
                )
            )

            st.success(
                "Cliente cadastrada com sucesso."
            )


# ============================================================
# SERVIÇOS
# ============================================================

elif pagina == "Serviços":

    titulo_pagina(
        "Serviços",
        "Catálogo de serviços oferecidos pelo Aura Beauty Studio."
    )

    servicos = (
        st.session_state.servicos
    )

    categorias = (
        servicos[
            "Categoria"
        ]
        .dropna()
        .unique()
    )

    for categoria in categorias:

        secao(
            categoria
        )

        dados = servicos[
            servicos["Categoria"]
            == categoria
        ]

        colunas = st.columns(3)

        for i, (_, row) in enumerate(
            dados.iterrows()
        ):

            with colunas[
                i % 3
            ]:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"""
                        <div class="service-category">
                            {row['Categoria'].upper()}
                        </div>

                        <div class="service-name">
                            {row['Serviço']}
                        </div>

                        <div class="small-muted">
                            Aproximadamente {row['Duração']} minutos
                        </div>

                        <div class="service-price">
                            {dinheiro(row['Preço'])}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# ============================================================
# FINANCEIRO
# ============================================================

elif pagina == "Financeiro":

    titulo_pagina(
        "Financeiro",
        "Acompanhe o faturamento, os gastos e o lucro do studio."
    )

    agenda = garantir_colunas_agenda(
        st.session_state.agenda
    )

    gastos = garantir_colunas_gastos(
        st.session_state.gastos
    )

    concluidos = (
        agenda[
            agenda["Status"]
            == "Concluído"
        ]
        .copy()
    )

    faturamento = (
        concluidos["Valor"].sum()
    )

    total_gastos = (
        gastos["Valor"].sum()
    )

    lucro = (
        faturamento
        -
        total_gastos
    )

    margem_lucro = (
        (lucro / faturamento) * 100
        if faturamento > 0
        else 0
    )

    quantidade = len(
        concluidos
    )

    ticket = (
        faturamento / quantidade
        if quantidade > 0
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Faturamento",
        dinheiro(faturamento)
    )

    c2.metric(
        "Gastos",
        dinheiro(total_gastos)
    )

    c3.metric(
        "Lucro líquido",
        dinheiro(lucro)
    )

    c4.metric(
        "Margem de lucro",
        f"{margem_lucro:.1f}%"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Atendimentos",
            quantidade
        )

    with c2:

        st.metric(
            "Ticket médio",
            dinheiro(ticket)
        )

    if faturamento > 0:

        if lucro > 0:

            st.success(
                f"O studio faturou "
                f"{dinheiro(faturamento)}, teve "
                f"{dinheiro(total_gastos)} em saídas "
                f"e apresentou lucro de "
                f"{dinheiro(lucro)}."
            )

        elif lucro < 0:

            st.error(
                f"As despesas estão maiores que o "
                f"faturamento. O resultado atual é "
                f"de {dinheiro(lucro)}."
            )

        else:

            st.warning(
                "O faturamento foi exatamente igual "
                "aos gastos registrados."
            )

    if not concluidos.empty:

        secao(
            "Faturamento por serviço"
        )

        financeiro_servico = (
            concluidos
            .groupby("Serviço")
            .agg(
                Atendimentos=(
                    "Serviço",
                    "count"
                ),
                Faturamento=(
                    "Valor",
                    "sum"
                )
            )
            .sort_values(
                "Faturamento",
                ascending=False
            )
        )

        col1, col2 = st.columns(
            [1.2, 1]
        )

        with col1:

            st.bar_chart(
                financeiro_servico[
                    "Faturamento"
                ],
                height=350
            )

        with col2:

            tabela = (
                financeiro_servico
                .reset_index()
                .copy()
            )

            tabela["Ticket Médio"] = (
                tabela["Faturamento"]
                /
                tabela["Atendimentos"]
            )

            tabela["Faturamento"] = (
                tabela["Faturamento"]
                .apply(dinheiro)
            )

            tabela["Ticket Médio"] = (
                tabela["Ticket Médio"]
                .apply(dinheiro)
            )

            st.dataframe(
                tabela,
                use_container_width=True,
                height=350,
                hide_index=True
            )

        secao(
            "Faturamento por dia"
        )

        por_dia = (
            concluidos
            .groupby("Data")["Valor"]
            .sum()
            .sort_index()
        )

        st.bar_chart(
            por_dia,
            height=300
        )

        secao(
            "Participação por categoria"
        )

        categorias_financeiro = (
            concluidos
            .merge(
                st.session_state.servicos[
                    [
                        "Serviço",
                        "Categoria"
                    ]
                ],
                on="Serviço",
                how="left"
            )
            .groupby("Categoria")["Valor"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        st.bar_chart(
            categorias_financeiro,
            height=280
        )

    secao(
        "Resumo financeiro"
    )

    resumo_financeiro = pd.DataFrame(
        [
            [
                "Faturamento",
                faturamento
            ],
            [
                "Gastos",
                total_gastos
            ],
            [
                "Lucro líquido",
                lucro
            ]
        ],
        columns=[
            "Indicador",
            "Valor"
        ]
    )

    resumo_financeiro["Valor"] = (
        resumo_financeiro["Valor"]
        .apply(dinheiro)
    )

    st.dataframe(
        resumo_financeiro,
        use_container_width=True,
        hide_index=True
    )

    secao(
        "Gastos por categoria"
    )

    gastos_categoria = (
        gastos
        .groupby("Categoria")["Valor"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    if not gastos_categoria.empty:

        st.bar_chart(
            gastos_categoria,
            height=300
        )


# ============================================================
# GASTOS
# ============================================================

elif pagina == "Gastos":

    titulo_pagina(
        "Gastos",
        "Registre despesas e investimentos realizados pelo studio."
    )

    gastos = garantir_colunas_gastos(
        st.session_state.gastos
    )

    st.session_state.gastos = gastos

    total_gastos = gastos[
        gastos["Tipo"] == "Gasto"
    ]["Valor"].sum()

    total_investimentos = gastos[
        gastos["Tipo"] == "Investimento"
    ]["Valor"].sum()

    total_saidas = gastos[
        "Valor"
    ].sum()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Gastos",
        dinheiro(total_gastos)
    )

    c2.metric(
        "Investimentos",
        dinheiro(total_investimentos)
    )

    c3.metric(
        "Total de saídas",
        dinheiro(total_saidas)
    )

    secao(
        "Registrar novo gasto"
    )

    col1, col2 = st.columns(2)

    with col1:

        data_gasto = st.date_input(
            "Data",
            value=date(2026, 9, 11),
            key="data_novo_gasto"
        )

        descricao_gasto = st.text_input(
            "Descrição",
            key="descricao_novo_gasto"
        )

        categoria_gasto = st.selectbox(
            "Categoria",
            [
                "Materiais",
                "Despesas fixas",
                "Marketing",
                "Equipamentos",
                "Manutenção",
                "Outros"
            ],
            key="categoria_novo_gasto"
        )

    with col2:

        tipo_gasto = st.selectbox(
            "Tipo",
            [
                "Gasto",
                "Investimento"
            ],
            key="tipo_novo_gasto"
        )

        valor_gasto = st.number_input(
            "Valor",
            min_value=0.0,
            step=10.0,
            format="%.2f",
            key="valor_novo_gasto"
        )

        observacao_gasto = st.text_input(
            "Observação",
            key="observacao_novo_gasto"
        )

    if st.button(
        "Registrar gasto",
        type="primary",
        use_container_width=True
    ):

        if not descricao_gasto.strip():

            st.error(
                "Informe a descrição do gasto."
            )

        elif valor_gasto <= 0:

            st.error(
                "Informe um valor maior que zero."
            )

        else:

            novo_gasto = pd.DataFrame(
                [
                    [
                        data_gasto,
                        descricao_gasto.strip(),
                        categoria_gasto,
                        tipo_gasto,
                        float(valor_gasto),
                        observacao_gasto.strip()
                    ]
                ],
                columns=[
                    "Data",
                    "Descrição",
                    "Categoria",
                    "Tipo",
                    "Valor",
                    "Observação"
                ]
            )

            st.session_state.gastos = pd.concat(
                [
                    st.session_state.gastos,
                    novo_gasto
                ],
                ignore_index=True
            )

            st.success(
                "Gasto registrado com sucesso."
            )

    secao(
        "Histórico de gastos"
    )

    if gastos.empty:

        st.info(
            "Ainda não existem gastos registrados."
        )

    else:

        tabela_gastos = (
            gastos
            .sort_values(
                "Data",
                ascending=False
            )
            .copy()
        )

        tabela_gastos["Valor"] = (
            tabela_gastos["Valor"]
            .apply(dinheiro)
        )

        st.dataframe(
            tabela_gastos,
            use_container_width=True,
            hide_index=True
        )

    secao(
        "Gastos por categoria"
    )

    gastos_categoria = (
        gastos
        .groupby("Categoria")["Valor"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    if not gastos_categoria.empty:

        st.bar_chart(
            gastos_categoria,
            height=300
        )


# ============================================================
# FIDELIZAÇÃO
# ============================================================

elif pagina == "Fidelização":

    titulo_pagina(
        "Fidelização",
        "Entenda o comportamento das clientes e descubra oportunidades de relacionamento."
    )

    agenda = (
        garantir_colunas_agenda(
            st.session_state.agenda
        )
    )

    concluidos = (
        agenda[
            agenda["Status"]
            == "Concluído"
        ]
        .copy()
    )

    if concluidos.empty:

        st.info(
            "Ainda não existem dados suficientes para gerar os indicadores de fidelização."
        )

    else:

        concluidos["Valor"] = (
            pd.to_numeric(
                concluidos["Valor"],
                errors="coerce"
            )
            .fillna(0)
        )

        visitas = (
            obter_visitas_cliente(
                concluidos
            )
        )

        if visitas.empty:

            st.info(
                "Ainda não existem dados suficientes para gerar os indicadores."
            )

        else:

            # ------------------------------------------------
            # INDICADORES
            # ------------------------------------------------

            cliente_mais_frequente = (
                visitas
                .sort_values(
                    [
                        "Visitas",
                        "Gasto"
                    ],
                    ascending=False
                )
                .iloc[0]["Cliente"]
            )

            cliente_maior_gasto = (
                visitas
                .sort_values(
                    "Gasto",
                    ascending=False
                )
                .iloc[0]["Cliente"]
            )

            clientes_recorrentes = len(
                visitas[
                    visitas["Visitas"] >= 3
                ]
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Mais visitas",
                cliente_mais_frequente
            )

            c2.metric(
                "Maior gasto",
                cliente_maior_gasto
            )

            c3.metric(
                "Clientes recorrentes",
                clientes_recorrentes
            )

            # ------------------------------------------------
            # CLIENTES MAIS FIÉIS
            # ------------------------------------------------

            secao(
                "Clientes mais fiéis"
            )

            ranking_visitas = (
                visitas
                .sort_values(
                    [
                        "Visitas",
                        "Gasto"
                    ],
                    ascending=False
                )
                .copy()
            )

            ranking_visitas["Gasto"] = (
                ranking_visitas["Gasto"]
                .apply(dinheiro)
            )

            st.dataframe(
                ranking_visitas[
                    [
                        "Cliente",
                        "Visitas",
                        "Gasto"
                    ]
                ],
                use_container_width=True,
                hide_index=True
            )

            # ------------------------------------------------
            # FREQUÊNCIA DAS CLIENTES
            # ------------------------------------------------

            secao(
                "Frequência das clientes"
            )

            frequencia = pd.cut(
                visitas["Visitas"],
                bins=[
                    0,
                    2,
                    4,
                    7,
                    100
                ],
                labels=[
                    "1–2 visitas",
                    "3–4 visitas",
                    "5–7 visitas",
                    "8+ visitas"
                ]
            )

            distribuicao = (
                frequencia
                .value_counts()
                .sort_index()
            )

            st.bar_chart(
                distribuicao,
                height=300
            )

            # ------------------------------------------------
            # SERVIÇOS POR CLIENTE
            # ------------------------------------------------

            secao(
                "Serviços por cliente"
            )

            servicos_clientes = (
                concluidos
                .groupby(
                    [
                        "Cliente",
                        "Serviço"
                    ]
                )
                .agg(
                    Atendimentos=(
                        "Serviço",
                        "count"
                    ),
                    Gasto=(
                        "Valor",
                        "sum"
                    )
                )
                .reset_index()
            )

            clientes_disponiveis = sorted(
                concluidos[
                    "Cliente"
                ]
                .dropna()
                .unique()
            )

            if clientes_disponiveis:

                cliente_selecionado = (
                    st.selectbox(
                        "Selecione uma cliente",
                        clientes_disponiveis
                    )
                )

                dados_cliente = (
                    servicos_clientes[
                        servicos_clientes[
                            "Cliente"
                        ]
                        == cliente_selecionado
                    ]
                    .sort_values(
                        "Gasto",
                        ascending=False
                    )
                    .copy()
                )

                dados_cliente["Gasto"] = (
                    dados_cliente["Gasto"]
                    .apply(dinheiro)
                )

                st.dataframe(
                    dados_cliente,
                    use_container_width=True,
                    hide_index=True
                )

            # ------------------------------------------------
            # OPORTUNIDADES DE RELACIONAMENTO
            # ------------------------------------------------

            secao(
                "Oportunidades de relacionamento"
            )

            clientes_inativos = (
                garantir_colunas_clientes(
                    st.session_state.clientes
                )
            )

            clientes_inativos["Última"] = (
                pd.to_datetime(
                    clientes_inativos[
                        "Última Visita"
                    ],
                    dayfirst=True,
                    errors="coerce"
                )
            )

            referencia = date(
                2026,
                9,
                11
            )

            clientes_inativos[
                "Dias sem visitar"
            ] = (
                pd.Timestamp(
                    referencia
                )
                -
                clientes_inativos[
                    "Última"
                ]
            ).dt.days

            inativos = (
                clientes_inativos[
                    clientes_inativos[
                        "Dias sem visitar"
                    ] >= 7
                ]
                .copy()
            )

            if not inativos.empty:

                quantidade_inativos = len(
                    inativos
                )

                st.warning(
                    f"**{quantidade_inativos} clientes** "
                    "estão há pelo menos 7 dias sem visitar o studio."
                )

                st.write(
                    "Esse grupo pode receber uma mensagem "
                    "de retorno pelo WhatsApp, uma condição "
                    "especial ou uma sugestão de novo serviço."
                )

                tabela_inativos = (
                    inativos[
                        [
                            "Cliente",
                            "Telefone",
                            "Última Visita",
                            "Dias sem visitar"
                        ]
                    ]
                    .sort_values(
                        "Dias sem visitar",
                        ascending=False
                    )
                )

                st.dataframe(
                    tabela_inativos,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.success(
                    "A maioria das clientes está mantendo "
                    "uma boa frequência de visitas."
                )

            # ------------------------------------------------
            # ESTRATÉGIA DE FIDELIZAÇÃO
            # ------------------------------------------------

            secao(
                "Estratégia de fidelização"
            )

            st.write(
                "Clientes que já realizaram vários serviços "
                "podem receber combinações personalizadas."
            )

            c1, c2 = st.columns(2)

            with c1:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        "### Unhas + sobrancelha"
                    )

                    st.caption(
                        "Combinação indicada para aumentar "
                        "o valor médio do atendimento."
                    )

            with c2:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        "### Cílios + sobrancelha"
                    )

                    st.caption(
                        "Boa oportunidade para oferecer "
                        "um segundo serviço."
                    )

            # ------------------------------------------------
            # OPORTUNIDADE DE AUMENTO DE TICKET
            # ------------------------------------------------

            secao(
                "Oportunidade de aumento de ticket"
            )

            st.info(
                "Identificar clientes que fazem apenas um "
                "serviço e apresentar serviços complementares "
                "pode aumentar o valor médio de cada visita."
            )
