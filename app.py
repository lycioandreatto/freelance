import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

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

st.markdown("""
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
    --pink-soft: #F9EEF0;
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

section[data-testid="stSidebar"] .stRadio label {
    padding: 8px 10px;
    border-radius: 10px;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 500 !important;
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

.titulo {
    font-family: 'Playfair Display', serif;
    font-size: 39px;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 5px;
}

.subtitulo {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 28px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    margin-top: 22px;
    margin-bottom: 15px;
}

.card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 16px;
}

.card-title {
    color: var(--muted);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
}

.card-value {
    font-size: 27px;
    font-weight: 600;
    color: var(--text);
}

.card-small {
    font-size: 12px;
    color: var(--muted);
    margin-top: 5px;
}

.orange-card {
    background: var(--orange);
    color: white;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 16px;
}

.orange-card .card-title,
.orange-card .card-value,
.orange-card .card-small {
    color: white !important;
}

.insight {
    background: var(--soft-orange);
    border-left: 4px solid var(--orange);
    border-radius: 12px;
    padding: 15px 18px;
    margin-bottom: 10px;
    color: var(--text);
}

.agendamento {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 17px;
    margin-bottom: 10px;
}

.agendamento-hora {
    font-size: 20px;
    font-weight: 600;
    color: var(--orange);
}

.agendamento-cliente {
    font-weight: 600;
    font-size: 15px;
}

.agendamento-servico {
    color: var(--muted);
    font-size: 13px;
    margin-top: 4px;
}

.status-confirmado {
    background: #EAF6F0;
    color: #34785A;
    border-radius: 20px;
    padding: 5px 11px;
    font-size: 11px;
    display: inline-block;
}

.status-pendente {
    background: #FFF2E5;
    color: #B96319;
    border-radius: 20px;
    padding: 5px 11px;
    font-size: 11px;
    display: inline-block;
}

.status-concluido {
    background: #F0EDF8;
    color: #68578C;
    border-radius: 20px;
    padding: 5px 11px;
    font-size: 11px;
    display: inline-block;
}

.status-cancelado {
    background: #F9EAEA;
    color: #A54B4B;
    border-radius: 20px;
    padding: 5px 11px;
    font-size: 11px;
    display: inline-block;
}

.servico-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 20px;
    height: 100%;
}

.servico-nome {
    font-family: 'Playfair Display', serif;
    font-size: 21px;
}

.servico-cat {
    color: var(--orange);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
}

.servico-preco {
    font-size: 20px;
    font-weight: 600;
    margin-top: 12px;
}

.cliente-destaque {
    background: linear-gradient(135deg, #FFF4ED, #FFFFFF);
    border: 1px solid #F4DDD0;
    border-radius: 18px;
    padding: 20px;
}

.metric-positive {
    color: var(--green);
    font-size: 12px;
}

.ranking-number {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    color: var(--orange);
}

.profile-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 22px;
}

.profile-name {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    margin-bottom: 4px;
}

.profile-info {
    color: var(--muted);
    font-size: 13px;
}

.progress-bg {
    background: #EEE9E6;
    border-radius: 10px;
    height: 7px;
    width: 100%;
    margin-top: 8px;
}

.progress-fill {
    background: var(--orange);
    border-radius: 10px;
    height: 7px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid var(--border);
    padding: 15px;
    border-radius: 15px;
}

button {
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# DADOS INICIAIS
# ============================================================

servicos_iniciais = pd.DataFrame([
    ["Unhas Postiças", "Unhas", 85.00, 90],
    ["Alongamento em Gel", "Unhas", 150.00, 120],
    ["Manicure", "Unhas", 35.00, 45],
    ["Pedicure", "Unhas", 40.00, 50],
    ["Sobrancelha", "Sobrancelhas", 35.00, 30],
    ["Design de Sobrancelha", "Sobrancelhas", 55.00, 45],
    ["Lash Lifting", "Cílios", 120.00, 75],
    ["Extensão de Cílios", "Cílios", 160.00, 120],
    ["Manutenção de Cílios", "Cílios", 100.00, 90],
], columns=[
    "Serviço",
    "Categoria",
    "Preço",
    "Duração"
])

clientes_iniciais = pd.DataFrame([
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
], columns=[
    "Cliente",
    "Telefone",
    "Última Visita",
    "Visitas",
    "Total Gasto"
])

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
    date(2026, 9, 18),
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

        nome = nomes[contador % len(nomes)]

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

        agenda_inicial.append([
            d,
            horario,
            nome,
            servico,
            precos[servico],
            status
        ])

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
# SESSION STATE
# ============================================================

# IMPORTANTE:
# Sempre reconstruímos a estrutura caso o Streamlit Cloud
# tenha mantido dados antigos de uma versão anterior do app.

if "servicos" not in st.session_state:
    st.session_state.servicos = servicos_iniciais.copy()

else:
    servicos_atual = st.session_state.servicos

    for coluna in servicos_iniciais.columns:

        if coluna not in servicos_atual.columns:
            st.session_state.servicos[coluna] = servicos_iniciais[coluna].values[
                :len(servicos_atual)
            ]

    if len(servicos_atual) != len(servicos_iniciais):
        st.session_state.servicos = servicos_iniciais.copy()


if "clientes" not in st.session_state:
    st.session_state.clientes = clientes_iniciais.copy()

else:

    clientes_atual = st.session_state.clientes

    colunas_clientes = [
        "Cliente",
        "Telefone",
        "Última Visita",
        "Visitas",
        "Total Gasto"
    ]

    # Se a estrutura antiga não tiver as colunas necessárias,
    # substituímos pelos dados corretos.
    estrutura_valida = all(
        coluna in clientes_atual.columns
        for coluna in colunas_clientes
    )

    if not estrutura_valida:

        st.session_state.clientes = clientes_iniciais.copy()

    else:

        st.session_state.clientes = clientes_atual[
            colunas_clientes
        ].copy()


if "agenda" not in st.session_state:
    st.session_state.agenda = agenda_inicial.copy()

else:

    agenda_atual = st.session_state.agenda

    colunas_agenda = [
        "Data",
        "Horário",
        "Cliente",
        "Serviço",
        "Valor",
        "Status"
    ]

    estrutura_agenda_valida = all(
        coluna in agenda_atual.columns
        for coluna in colunas_agenda
    )

    if not estrutura_agenda_valida:
        st.session_state.agenda = agenda_inicial.copy()
    else:
        st.session_state.agenda = agenda_atual[
            colunas_agenda
        ].copy()


# ============================================================
# FUNÇÕES
# ============================================================

def dinheiro(valor):

    return (
        f"R$ {float(valor):,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def saudacao():

    hora = datetime.now().hour

    if hora < 12:
        return "Bom dia"

    elif hora < 18:
        return "Boa tarde"

    return "Boa noite"


def calcular_faturamento(df):

    if df.empty:
        return 0

    return df[
        df["Status"] == "Concluído"
    ]["Valor"].sum()


def calcular_ticket(df):

    concluidos = df[
        df["Status"] == "Concluído"
    ]

    if len(concluidos) == 0:
        return 0

    return concluidos["Valor"].sum() / len(concluidos)


def obter_visitas_cliente(df):

    concluidos = df[
        df["Status"] == "Concluído"
    ]

    if concluidos.empty:

        return pd.DataFrame(
            columns=[
                "Visitas",
                "Gasto"
            ]
        )

    return (
        concluidos
        .groupby("Cliente")
        .agg(
            Visitas=("Cliente", "count"),
            Gasto=("Valor", "sum")
        )
        .sort_values(
            "Gasto",
            ascending=False
        )
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">Aura Beauty</div>
        <div class="brand-sub">Beauty Studio</div>
        """,
        unsafe_allow_html=True
    )

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

    st.markdown("---")

    st.caption("Aura Beauty Studio")
    st.caption("Gestão inteligente do seu studio")

# ============================================================
# VISÃO GERAL
# ============================================================

if pagina == "Visão geral":

    st.markdown(
        f'<div class="titulo">{saudacao()}, Lilly.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Aqui está um resumo do desempenho do seu studio.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    concluidos = agenda[
        agenda["Status"] == "Concluído"
    ]

    faturamento = concluidos["Valor"].sum()

    quantidade_visitas = len(concluidos)

    ticket = (
        faturamento / quantidade_visitas
        if quantidade_visitas > 0
        else 0
    )

    clientes_ativos = concluidos[
        "Cliente"
    ].nunique()

    agendamentos_hoje = agenda[
        agenda["Data"] == date(2026, 9, 11)
    ]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            f"""
            <div class="orange-card">
                <div class="card-title">Faturamento</div>
                <div class="card-value">{dinheiro(faturamento)}</div>
                <div class="card-small">serviços concluídos</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">Atendimentos</div>
                <div class="card-value">{quantidade_visitas}</div>
                <div class="metric-positive">clientes atendidas</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">Ticket médio</div>
                <div class="card-value">{dinheiro(ticket)}</div>
                <div class="card-small">por atendimento</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">Hoje</div>
                <div class="card-value">{len(agendamentos_hoje)}</div>
                <div class="card-small">agendamentos</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # AGENDA DO DIA
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Agenda de hoje</div>',
        unsafe_allow_html=True
    )

    agenda_hoje = agenda[
        agenda["Data"] == date(2026, 9, 11)
    ].sort_values("Horário")

    if agenda_hoje.empty:

        st.info("Nenhum agendamento para hoje.")

    else:

        col1, col2 = st.columns([1.5, 1])

        with col1:

            for _, row in agenda_hoje.head(5).iterrows():

                if row["Status"] == "Confirmado":

                    status_html = (
                        '<span class="status-confirmado">'
                        'Confirmado'
                        '</span>'
                    )

                elif row["Status"] == "Pendente":

                    status_html = (
                        '<span class="status-pendente">'
                        'Pendente'
                        '</span>'
                    )

                elif row["Status"] == "Concluído":

                    status_html = (
                        '<span class="status-concluido">'
                        'Concluído'
                        '</span>'
                    )

                else:

                    status_html = (
                        '<span class="status-cancelado">'
                        'Cancelado'
                        '</span>'
                    )

                st.markdown(
                    f"""
                    <div class="agendamento">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <div class="agendamento-hora">
                                    {row["Horário"]}
                                </div>

                                <div class="agendamento-cliente">
                                    {row["Cliente"]}
                                </div>

                                <div class="agendamento-servico">
                                    {row["Serviço"]} · {dinheiro(row["Valor"])}
                                </div>
                            </div>

                            <div>
                                {status_html}
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with col2:

            faturamento_hoje = (
                agenda_hoje[
                    agenda_hoje["Status"] != "Cancelado"
                ]["Valor"].sum()
            )

            confirmados = len(
                agenda_hoje[
                    agenda_hoje["Status"] == "Confirmado"
                ]
            )

            pendentes = len(
                agenda_hoje[
                    agenda_hoje["Status"] == "Pendente"
                ]
            )

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">
                        Resumo do dia
                    </div>

                    <div style="font-size:25px; font-weight:600;">
                        {dinheiro(faturamento_hoje)}
                    </div>

                    <div class="card-small">
                        faturamento previsto
                    </div>

                    <br>

                    <div>
                        <strong>{confirmados}</strong>
                        confirmados
                    </div>

                    <div>
                        <strong>{pendentes}</strong>
                        pendentes
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # --------------------------------------------------------
    # DESEMPENHO
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Desempenho</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.4, 1])

    with col1:

        diario = (
            concluidos
            .groupby("Data")["Valor"]
            .sum()
            .reset_index()
        )

        diario["Data"] = pd.to_datetime(
            diario["Data"]
        )

        st.markdown(
            '<div class="card"><div class="card-title">Faturamento por dia</div>',
            unsafe_allow_html=True
        )

        st.line_chart(
            diario.set_index("Data")["Valor"],
            height=280
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        ranking_servicos = (
            concluidos
            .groupby("Serviço")
            .agg(
                Atendimentos=("Serviço", "count"),
                Faturamento=("Valor", "sum")
            )
            .sort_values(
                "Faturamento",
                ascending=False
            )
        )

        st.markdown(
            '<div class="card"><div class="card-title">Serviços que mais faturam</div>',
            unsafe_allow_html=True
        )

        st.dataframe(
            ranking_servicos,
            use_container_width=True,
            height=280
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # INSIGHTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Insights</div>',
        unsafe_allow_html=True
    )

    ranking_servicos = (
        concluidos
        .groupby("Serviço")
        .agg(
            Atendimentos=("Serviço", "count"),
            Faturamento=("Valor", "sum")
        )
        .sort_values(
            "Faturamento",
            ascending=False
        )
    )

    if not ranking_servicos.empty:

        servico_top = ranking_servicos.index[0]

        faturamento_top = ranking_servicos.iloc[0]["Faturamento"]

        cliente_top = (
            concluidos
            .groupby("Cliente")["Valor"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        melhor_cliente = cliente_top.index[0]

        st.markdown(
            f"""
            <div class="insight">
                <strong>Serviço destaque:</strong>
                {servico_top} lidera o faturamento com
                {dinheiro(faturamento_top)}.
            </div>

            <div class="insight">
                <strong>Cliente de maior valor:</strong>
                {melhor_cliente} é a cliente que mais gastou
                no studio.
            </div>

            <div class="insight">
                <strong>Ticket médio:</strong>
                cada atendimento gera aproximadamente
                {dinheiro(ticket)}.
            </div>

            <div class="insight">
                <strong>Oportunidade comercial:</strong>
                oferecer combinações de serviços pode aumentar
                o valor de cada atendimento.
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# AGENDA
# ============================================================

elif pagina == "Agenda":

    st.markdown(
        '<div class="titulo">Agenda</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Visualize todos os atendimentos do studio.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    data_selecionada = st.date_input(
        "Escolha o dia",
        value=date(2026, 9, 11)
    )

    agenda_dia = agenda[
        agenda["Data"] == data_selecionada
    ].sort_values("Horário")

    valor_previsto = agenda_dia[
        agenda_dia["Status"] != "Cancelado"
    ]["Valor"].sum()

    concluidos_dia = len(
        agenda_dia[
            agenda_dia["Status"] == "Concluído"
        ]
    )

    confirmados_dia = len(
        agenda_dia[
            agenda_dia["Status"] == "Confirmado"
        ]
    )

    pendentes_dia = len(
        agenda_dia[
            agenda_dia["Status"] == "Pendente"
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

    st.markdown(
        f'<div class="section-title">{data_selecionada.strftime("%d/%m/%Y")}</div>',
        unsafe_allow_html=True
    )

    if agenda_dia.empty:

        st.info(
            "Nenhum agendamento para este dia."
        )

    else:

        for _, row in agenda_dia.iterrows():

            if row["Status"] == "Confirmado":

                status_html = (
                    '<span class="status-confirmado">'
                    'Confirmado'
                    '</span>'
                )

            elif row["Status"] == "Pendente":

                status_html = (
                    '<span class="status-pendente">'
                    'Pendente'
                    '</span>'
                )

            elif row["Status"] == "Concluído":

                status_html = (
                    '<span class="status-concluido">'
                    'Concluído'
                    '</span>'
                )

            else:

                status_html = (
                    '<span class="status-cancelado">'
                    'Cancelado'
                    '</span>'
                )

            st.markdown(
                f"""
                <div class="agendamento">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                    ">

                        <div>

                            <div class="agendamento-hora">
                                {row["Horário"]}
                            </div>

                            <div class="agendamento-cliente">
                                {row["Cliente"]}
                            </div>

                            <div class="agendamento-servico">
                                {row["Serviço"]}
                                ·
                                {dinheiro(row["Valor"])}
                            </div>

                        </div>

                        <div>
                            {status_html}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

# ============================================================
# NOVO AGENDAMENTO
# ============================================================

elif pagina == "Novo agendamento":

    st.markdown(
        '<div class="titulo">Novo agendamento</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Agende um novo atendimento para sua cliente.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        nome = st.text_input(
            "Nome da cliente"
        )

        telefone = st.text_input(
            "WhatsApp"
        )

        data = st.date_input(
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

    servico_info = st.session_state.servicos[
        st.session_state.servicos["Serviço"] == servico
    ]

    if not servico_info.empty:

        servico_info = servico_info.iloc[0]

        st.markdown(
            f"""
            <div class="cliente-destaque">

                <div class="card-title">
                    Resumo do atendimento
                </div>

                <strong>{servico}</strong>

                <br>

                Duração aproximada:
                {servico_info["Duração"]} minutos

                <br>

                Valor:
                <strong>
                    {dinheiro(servico_info["Preço"])}
                </strong>

            </div>
            """,
            unsafe_allow_html=True
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

            novo = pd.DataFrame([[
                data,
                horario,
                nome.strip(),
                servico,
                float(servico_info["Preço"]),
                status
            ]], columns=[
                "Data",
                "Horário",
                "Cliente",
                "Serviço",
                "Valor",
                "Status"
            ])

            st.session_state.agenda = pd.concat(
                [
                    st.session_state.agenda,
                    novo
                ],
                ignore_index=True
            )

            clientes = st.session_state.clientes.copy()

            if nome.strip() not in clientes[
                "Cliente"
            ].values:

                novo_cliente = pd.DataFrame([[
                    nome.strip(),
                    telefone,
                    data.strftime("%d/%m/%Y"),
                    0,
                    0.00
                ]], columns=[
                    "Cliente",
                    "Telefone",
                    "Última Visita",
                    "Visitas",
                    "Total Gasto"
                ])

                st.session_state.clientes = pd.concat(
                    [
                        clientes,
                        novo_cliente
                    ],
                    ignore_index=True
                )

            st.success(
                f"Agendamento de {nome.strip()} criado com sucesso."
            )

# ============================================================
# CLIENTES
# ============================================================

elif pagina == "Clientes":

    st.markdown(
        '<div class="titulo">Clientes</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Conheça melhor quem frequenta o Aura Beauty Studio.</div>',
        unsafe_allow_html=True
    )

    clientes = st.session_state.clientes.copy()

    # Garantia adicional contra KeyError
    colunas_necessarias = [
        "Cliente",
        "Telefone",
        "Última Visita",
        "Visitas",
        "Total Gasto"
    ]

    for coluna in colunas_necessarias:

        if coluna not in clientes.columns:

            if coluna == "Visitas":
                clientes[coluna] = 0

            elif coluna == "Total Gasto":
                clientes[coluna] = 0.0

            else:
                clientes[coluna] = ""

    clientes["Visitas"] = pd.to_numeric(
        clientes["Visitas"],
        errors="coerce"
    ).fillna(0)

    clientes["Total Gasto"] = pd.to_numeric(
        clientes["Total Gasto"],
        errors="coerce"
    ).fillna(0)

    st.session_state.clientes = clientes

    total_clientes = len(clientes)

    clientes_recorrentes = len(
        clientes[
            clientes["Visitas"] >= 5
        ]
    )

    gasto_medio = (
        clientes["Total Gasto"].mean()
        if len(clientes) > 0
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

    st.markdown(
        '<div class="section-title">Ranking de clientes</div>',
        unsafe_allow_html=True
    )

    ranking = clientes.sort_values(
        "Total Gasto",
        ascending=False
    ).copy()

    ranking_exibicao = ranking.copy()

    ranking_exibicao[
        "Total Gasto"
    ] = ranking_exibicao[
        "Total Gasto"
    ].apply(dinheiro)

    st.dataframe(
        ranking_exibicao,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Adicionar cliente</div>',
        unsafe_allow_html=True
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

        elif novo_nome.strip() in clientes[
            "Cliente"
        ].values:

            st.warning(
                "Essa cliente já está cadastrada."
            )

        else:

            novo_cliente = pd.DataFrame([[
                novo_nome.strip(),
                novo_telefone,
                date.today().strftime("%d/%m/%Y"),
                0,
                0.00
            ]], columns=[
                "Cliente",
                "Telefone",
                "Última Visita",
                "Visitas",
                "Total Gasto"
            ])

            st.session_state.clientes = pd.concat(
                [
                    clientes,
                    novo_cliente
                ],
                ignore_index=True
            )

            st.success(
                "Cliente cadastrada com sucesso."
            )

# ============================================================
# SERVIÇOS
# ============================================================

elif pagina == "Serviços":

    st.markdown(
        '<div class="titulo">Serviços</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Catálogo de serviços oferecidos pelo Aura Beauty Studio.</div>',
        unsafe_allow_html=True
    )

    servicos = st.session_state.servicos

    categorias = servicos[
        "Categoria"
    ].unique()

    for categoria in categorias:

        st.markdown(
            f'<div class="section-title">{categoria}</div>',
            unsafe_allow_html=True
        )

        dados = servicos[
            servicos["Categoria"] == categoria
        ]

        colunas = st.columns(3)

        for i, (_, row) in enumerate(
            dados.iterrows()
        ):

            with colunas[
                i % 3
            ]:

                st.markdown(
                    f"""
                    <div class="servico-card">

                        <div class="servico-cat">
                            {row["Categoria"]}
                        </div>

                        <div class="servico-nome">
                            {row["Serviço"]}
                        </div>

                        <div class="card-small">
                            Aproximadamente
                            {row["Duração"]} minutos
                        </div>

                        <div class="servico-preco">
                            {dinheiro(row["Preço"])}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ============================================================
# FINANCEIRO
# ============================================================

elif pagina == "Financeiro":

    st.markdown(
        '<div class="titulo">Financeiro</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Acompanhe o faturamento e o desempenho financeiro do studio.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    concluidos = agenda[
        agenda["Status"] == "Concluído"
    ].copy()

    if concluidos.empty:

        st.info(
            "Ainda não existem atendimentos concluídos."
        )

    else:

        faturamento = concluidos["Valor"].sum()

        quantidade = len(concluidos)

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

        st.markdown(
            '<div class="section-title">Faturamento por serviço</div>',
            unsafe_allow_html=True
        )

        financeiro_servico = (
            concluidos
            .groupby("Serviço")
            .agg(
                Atendimentos=("Serviço", "count"),
                Faturamento=("Valor", "sum")
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

            tabela = financeiro_servico.copy()

            tabela[
                "Ticket Médio"
            ] = (
                tabela["Faturamento"]
                /
                tabela["Atendimentos"]
            )

            tabela[
                "Faturamento"
            ] = tabela[
                "Faturamento"
            ].apply(dinheiro)

            tabela[
                "Ticket Médio"
            ] = tabela[
                "Ticket Médio"
            ].apply(dinheiro)

            st.dataframe(
                tabela,
                use_container_width=True,
                height=350
            )

        st.markdown(
            '<div class="section-title">Faturamento por dia</div>',
            unsafe_allow_html=True
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

        st.markdown(
            '<div class="section-title">Participação por categoria</div>',
            unsafe_allow_html=True
        )

        categorias_financeiro = (
            concluidos
            .merge(
                st.session_state.servicos[
                    ["Serviço", "Categoria"]
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

    st.markdown(
        '<div class="titulo">Fidelização</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitulo">Entenda o comportamento das clientes e descubra oportunidades de relacionamento.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda.copy()

    # --------------------------------------------------------
    # GARANTIA DAS COLUNAS DA AGENDA
    # --------------------------------------------------------

    colunas_agenda = [
        "Data",
        "Horário",
        "Cliente",
        "Serviço",
        "Valor",
        "Status"
    ]

    for coluna in colunas_agenda:

        if coluna not in agenda.columns:

            if coluna == "Valor":
                agenda[coluna] = 0.0

            else:
                agenda[coluna] = ""

    # --------------------------------------------------------
    # ATENDIMENTOS CONCLUÍDOS
    # --------------------------------------------------------

    concluidos = agenda[
        agenda["Status"] == "Concluído"
    ].copy()

    if concluidos.empty:

        st.info(
            "Ainda não existem dados suficientes para gerar os indicadores de fidelização."
        )

    else:

        # ----------------------------------------------------
        # GARANTE QUE VALOR SEJA NUMÉRICO
        # ----------------------------------------------------

        concluidos["Valor"] = pd.to_numeric(
            concluidos["Valor"],
            errors="coerce"
        ).fillna(0)

        # ----------------------------------------------------
        # VISITAS POR CLIENTE
        # ----------------------------------------------------

        visitas = obter_visitas_cliente(
            concluidos
        )

        if visitas.empty:

            st.info(
                "Ainda não existem dados suficientes para gerar os indicadores."
            )

        else:

            # ------------------------------------------------
            # CLIENTE MAIS FREQUENTE
            # ------------------------------------------------

            cliente_mais_frequente = (
                visitas["Visitas"]
                .sort_values(
                    ascending=False
                )
                .index[0]
            )

            # ------------------------------------------------
            # CLIENTE COM MAIOR GASTO
            # ------------------------------------------------

            cliente_maior_gasto = (
                visitas["Gasto"]
                .sort_values(
                    ascending=False
                )
                .index[0]
            )

            # ------------------------------------------------
            # INDICADORES PRINCIPAIS
            # ------------------------------------------------

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
                len(
                    visitas[
                        visitas["Visitas"] >= 3
                    ]
                )
            )

            # ------------------------------------------------
            # CLIENTES MAIS FIÉIS
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">Clientes mais fiéis</div>',
                unsafe_allow_html=True
            )

            ranking_visitas = (
                visitas
                .sort_values(
                    ["Visitas", "Gasto"],
                    ascending=False
                )
                .copy()
            )

            ranking_visitas["Gasto"] = (
                ranking_visitas["Gasto"]
                .apply(dinheiro)
            )

            st.dataframe(
                ranking_visitas,
                use_container_width=True,
                hide_index=True
            )

            # ------------------------------------------------
            # FREQUÊNCIA DAS CLIENTES
            # ------------------------------------------------

            st.markdown(
                '<div class="section-title">Frequência das clientes</div>',
                unsafe_allow_html=True
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

            st.markdown(
                '<div class="section-title">Serviços por cliente</div>',
                unsafe_allow_html=True
            )

            servicos_clientes = (
                concluidos
                .groupby(
                    ["Cliente", "Serviço"]
                )
                .agg(
                    Atendimentos=("Serviço", "count"),
                    Gasto=("Valor", "sum")
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

                cliente_selecionado = st.selectbox(
                    "Selecione uma cliente",
                    clientes_disponiveis
                )

                dados_cliente = (
                    servicos_clientes[
                        servicos_clientes["Cliente"]
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

            st.markdown(
                '<div class="section-title">Oportunidades de relacionamento</div>',
                unsafe_allow_html=True
            )

            clientes_inativos = (
                st.session_state.clientes
                .copy()
            )

            # ------------------------------------------------
            # GARANTE AS COLUNAS DOS CLIENTES
            # ------------------------------------------------

            colunas_clientes = [
                "Cliente",
                "Telefone",
                "Última Visita",
                "Visitas",
                "Total Gasto"
            ]

            for coluna in colunas_clientes:

                if coluna not in clientes_inativos.columns:

                    if coluna == "Visitas":
                        clientes_inativos[coluna] = 0

                    elif coluna == "Total Gasto":
                        clientes_inativos[coluna] = 0.0

                    else:
                        clientes_inativos[coluna] = ""

            # ------------------------------------------------
            # CONVERSÃO DA DATA DA ÚLTIMA VISITA
            # ------------------------------------------------

            clientes_inativos["Última"] = pd.to_datetime(
                clientes_inativos["Última Visita"],
                dayfirst=True,
                errors="coerce"
            )

            # ------------------------------------------------
            # DATA DE REFERÊNCIA DO DEMO
            # ------------------------------------------------

            referencia = date(
                2026,
                9,
                11
            )

            clientes_inativos["Dias sem visitar"] = (
                pd.Timestamp(
                    referencia
                )
                -
                clientes_inativos["Última"]
            ).dt.days

            # ------------------------------------------------
            # CLIENTES QUE ESTÃO HÁ 7+ DIAS SEM VISITAR
            # ------------------------------------------------

            inativos = clientes_inativos[
                clientes_inativos["Dias sem visitar"] >= 7
            ].copy()

            # ------------------------------------------------
            # OPORTUNIDADE DE RETORNO
            # ------------------------------------------------

            if not inativos.empty:

                quantidade_inativos = len(
                    inativos
                )

                st.markdown(
                    "### Oportunidade de relacionamento"
                )

                st.markdown(
                    f"**{quantidade_inativos} clientes** estão há pelo menos 7 dias sem visitar o studio."
                )

                st.write(
                    "Esse grupo pode receber uma mensagem de retorno pelo WhatsApp, "
                    "uma condição especial ou uma sugestão de novo serviço."
                )

            else:

                st.markdown(
                    "### Boa frequência"
                )

                st.write(
                    "A maioria das clientes está mantendo uma boa frequência de visitas."
                )

            # ------------------------------------------------
            # ESTRATÉGIA DE FIDELIZAÇÃO
            # ------------------------------------------------

            st.markdown(
                "### Estratégia de fidelização"
            )

            st.write(
                "Clientes que já realizaram vários serviços podem receber "
                "combinações personalizadas, como:"
            )

            st.markdown(
                "**Unhas + sobrancelha**"
            )

            st.markdown(
                "ou"
            )

            st.markdown(
                "**Cílios + sobrancelha**"
            )

            # ------------------------------------------------
            # OPORTUNIDADE DE AUMENTO DE TICKET
            # ------------------------------------------------

            st.markdown(
                "### Oportunidade de aumento de ticket"
            )

            st.write(
                "Identificar clientes que fazem apenas um serviço e apresentar "
                "serviços complementares pode aumentar o valor médio de cada visita."
            )



