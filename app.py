import streamlit as st
import pandas as pd
from datetime import date, datetime


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Aura Beauty Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CORES E ESTILO
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap');

    :root {
        --orange: #F05A28;
        --orange-dark: #D94718;
        --cream: #FFF9F5;
        --background: #F7F4F2;
        --white: #FFFFFF;
        --text: #292624;
        --muted: #817873;
        --border: #EDE5E0;
        --soft-orange: #FFF0E9;
        --green: #3E8B68;
    }

    .stApp {
        background: var(--background);
        color: var(--text);
        font-family: 'DM Sans', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background: #211F1E;
        border-right: 0;
    }

    section[data-testid="stSidebar"] * {
        color: #F9F4F1 !important;
    }

    h1,
    h2,
    h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 500 !important;
        color: var(--text);
    }

    section[data-testid="stSidebar"] .stRadio label {
        padding: 8px 10px;
        border-radius: 10px;
    }

    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid var(--border);
        padding: 15px;
        border-radius: 15px;
    }

    div[data-testid="stMetricValue"] {
        font-family: 'DM Sans', sans-serif;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 39px;
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
        margin-top: 25px;
        margin-bottom: 15px;
        color: var(--text);
    }

    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 29px;
        color: #FFFFFF;
        margin-bottom: 2px;
    }

    .brand-sub {
        font-size: 10px;
        color: #BDB3AE !important;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }

    .small-muted {
        color: var(--muted);
        font-size: 13px;
    }

    .orange-box {
        background: var(--orange);
        color: white;
        border-radius: 16px;
        padding: 20px;
    }

    .orange-box-title {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: white;
        margin-bottom: 8px;
    }

    .orange-box-value {
        font-size: 27px;
        font-weight: 600;
        color: white;
    }

    .orange-box-small {
        font-size: 12px;
        color: white;
        margin-top: 5px;
    }

    .insight-box {
        background: var(--soft-orange);
        border-left: 4px solid var(--orange);
        border-radius: 10px;
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
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 8px;
    }

    .service-price {
        font-size: 20px;
        font-weight: 600;
        margin-top: 10px;
    }

    button {
        border-radius: 10px !important;
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

    hora = datetime.now().hour

    if hora < 12:
        return "Bom dia"

    if hora < 18:
        return "Boa tarde"

    return "Boa noite"


def titulo_pagina(titulo, subtitulo):

    st.markdown(
        f"## {titulo}"
    )

    st.caption(
        subtitulo
    )


def secao(titulo):

    st.markdown(
        f"### {titulo}"
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


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "### Aura Beauty"
    )

    st.caption(
        "BEAUTY STUDIO"
    )

    st.write("")

    pagina = st.radio(
        "Navegação",
        [
            "Visão geral",
            "Agenda",
            "Novo agendamento",
            "Clientes",
            "Serviços",
            "Financeiro",
            "Fidelização"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption(
        "Aura Beauty Studio"
    )

    st.caption(
        "Gestão inteligente do seu studio"
    )


# ============================================================
# VISÃO GERAL
# ============================================================

if pagina == "Visão geral":

    st.markdown(
        f"# {saudacao()}, Lilly."
    )

    st.caption(
        "Aqui está um resumo do desempenho do seu studio."
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
                            f"### {row['Horário']}"
                        )

                    with dados_col:

                        st.markdown(
                            f"**{row['Cliente']}**"
                        )

                        st.caption(
                            f"{row['Serviço']} · "
                            f"{dinheiro(row['Valor'])}"
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
                        f"### {row['Horário']}"
                    )

                with col2:

                    st.markdown(
                        f"**{row['Cliente']}**"
                    )

                    st.caption(
                        f"{row['Serviço']} · "
                        f"{dinheiro(row['Valor'])}"
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

                    st.caption(
                        row["Categoria"]
                        .upper()
                    )

                    st.markdown(
                        f"### {row['Serviço']}"
                    )

                    st.caption(
                        f"Aproximadamente "
                        f"{row['Duração']} minutos"
                    )

                    st.markdown(
                        f"**{dinheiro(row['Preço'])}**"
                    )


# ============================================================
# FINANCEIRO
# ============================================================

elif pagina == "Financeiro":

    titulo_pagina(
        "Financeiro",
        "Acompanhe o faturamento e o desempenho financeiro do studio."
    )

    agenda = garantir_colunas_agenda(
        st.session_state.agenda
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
            "Ainda não existem atendimentos concluídos."
        )

    else:

        faturamento = (
            concluidos["Valor"].sum()
        )

        quantidade = len(
            concluidos
        )

        ticket = (
            faturamento / quantidade
        )

        maior_dia = (
            concluidos
            .groupby("Data")["Valor"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Faturamento",
            dinheiro(faturamento)
        )

        c2.metric(
            "Atendimentos",
            quantidade
        )

        c3.metric(
            "Ticket médio",
            dinheiro(ticket)
        )

        c4.metric(
            "Melhor dia",
            dinheiro(
                maior_dia.iloc[0]
            )
        )

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
