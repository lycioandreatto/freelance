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
# CORES / ESTILO
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

.titulo {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 4px;
}

.subtitulo {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 28px;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    color: #FFFFFF;
    margin-bottom: 2px;
}

.brand-sub {
    font-size: 11px;
    color: #BDB3AE !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 28px;
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
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.card-value {
    font-size: 28px;
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
    padding: 24px;
    margin-bottom: 16px;
}

.orange-card .card-title,
.orange-card .card-value,
.orange-card .card-small {
    color: white !important;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    margin-top: 18px;
    margin-bottom: 15px;
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
    padding: 5px 10px;
    font-size: 11px;
    display: inline-block;
}

.status-pendente {
    background: #FFF2E5;
    color: #B96319;
    border-radius: 20px;
    padding: 5px 10px;
    font-size: 11px;
    display: inline-block;
}

.status-concluido {
    background: #F0EDF8;
    color: #68578C;
    border-radius: 20px;
    padding: 5px 10px;
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
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
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

button {
    border-radius: 10px !important;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid var(--border);
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# DADOS FICTÍCIOS
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
], columns=["Serviço", "Categoria", "Preço", "Duração"])

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
], columns=["Cliente", "Telefone", "Última Visita", "Visitas", "Total Gasto"])

# ============================================================
# GERAR AGENDAMENTOS FICTÍCIOS
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

agenda_inicial = []

datas = [
    date(2026, 9, 8),
    date(2026, 9, 9),
    date(2026, 9, 10),
    date(2026, 9, 11),
    date(2026, 9, 12),
    date(2026, 9, 13),
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

contador = 0

for d in datas:
    quantidade = 5 if d.weekday() < 5 else 4

    for i in range(quantidade):
        nome = nomes[contador % len(nomes)]
        servico = servicos_lista[(contador * 2) % len(servicos_lista)]
        horario = horarios[i]

        if d < date(2026, 9, 11):
            status = "Concluído"
        elif d == date(2026, 9, 11):
            status = ["Confirmado", "Confirmado", "Pendente", "Confirmado", "Pendente"][i]
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

if "servicos" not in st.session_state:
    st.session_state.servicos = servicos_iniciais.copy()

if "clientes" not in st.session_state:
    st.session_state.clientes = clientes_iniciais.copy()

if "agenda" not in st.session_state:
    st.session_state.agenda = agenda_inicial.copy()

# ============================================================
# FUNÇÕES
# ============================================================

def dinheiro(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def total_faturamento(df):
    return df[df["Status"] == "Concluído"]["Valor"].sum()


def visitas_por_cliente(df):
    return (
        df[df["Status"] == "Concluído"]
        .groupby("Cliente")
        .agg(
            Visitas=("Cliente", "count"),
            Gasto=("Valor", "sum")
        )
        .sort_values("Gasto", ascending=False)
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

    st.markdown('<div class="titulo">Bom dia, Aura.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Aqui está um resumo do desempenho do seu studio.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    concluidos = agenda[agenda["Status"] == "Concluído"]

    faturamento = concluidos["Valor"].sum()
    quantidade_visitas = len(concluidos)
    ticket = faturamento / quantidade_visitas if quantidade_visitas else 0
    clientes_ativos = concluidos["Cliente"].nunique()

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
                <div class="metric-positive">↑ clientes atendidas</div>
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
                <div class="card-title">Clientes</div>
                <div class="card-value">{clientes_ativos}</div>
                <div class="card-small">clientes atendidas</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Movimento do studio</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.6, 1])

    with col1:

        diario = (
            concluidos
            .groupby("Data")["Valor"]
            .sum()
            .reset_index()
        )

        diario["Data"] = pd.to_datetime(diario["Data"])

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
            .sort_values("Faturamento", ascending=False)
        )

        st.markdown(
            '<div class="card"><div class="card-title">Serviços mais procurados</div>',
            unsafe_allow_html=True
        )

        st.dataframe(
            ranking_servicos,
            use_container_width=True,
            height=280
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Insights do studio</div>', unsafe_allow_html=True)

    if not ranking_servicos.empty:

        servico_top = ranking_servicos.index[0]
        faturamento_top = ranking_servicos.iloc[0]["Faturamento"]

        cliente_top = (
            concluidos
            .groupby("Cliente")["Valor"]
            .sum()
            .sort_values(ascending=False)
        )

        melhor_cliente = cliente_top.index[0]

        st.markdown(
            f"""
            <div class="insight">
                <strong>Serviço destaque:</strong> {servico_top} é o serviço que mais gera faturamento,
                com {dinheiro(faturamento_top)} no período analisado.
            </div>

            <div class="insight">
                <strong>Cliente de maior valor:</strong> {melhor_cliente} é a cliente que mais gastou no studio.
            </div>

            <div class="insight">
                <strong>Ticket médio:</strong> cada atendimento gera aproximadamente {dinheiro(ticket)}.
                Uma boa estratégia é oferecer combinações de serviços para aumentar esse valor.
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# AGENDA
# ============================================================

elif pagina == "Agenda":

    st.markdown('<div class="titulo">Agenda</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Visualize todos os atendimentos do studio.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    data_selecionada = st.date_input(
        "Escolha o dia",
        value=date(2026, 9, 11)
    )

    agenda_dia = agenda[agenda["Data"] == data_selecionada].sort_values("Horário")

    total_dia = agenda_dia["Valor"].sum()
    concluidos_dia = len(
        agenda_dia[agenda_dia["Status"] == "Concluído"]
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Agendamentos",
        len(agenda_dia)
    )

    c2.metric(
        "Concluídos",
        concluidos_dia
    )

    c3.metric(
        "Valor previsto",
        dinheiro(total_dia)
    )

    st.markdown(
        f'<div class="section-title">{data_selecionada.strftime("%d/%m/%Y")}</div>',
        unsafe_allow_html=True
    )

    if agenda_dia.empty:

        st.info("Nenhum agendamento para este dia.")

    else:

        for _, row in agenda_dia.iterrows():

            if row["Status"] == "Confirmado":
                status_html = '<span class="status-confirmado">Confirmado</span>'
            elif row["Status"] == "Pendente":
                status_html = '<span class="status-pendente">Pendente</span>'
            else:
                status_html = '<span class="status-concluido">Concluído</span>'

            st.markdown(
                f"""
                <div class="agendamento">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div class="agendamento-hora">{row["Horário"]}</div>
                            <div class="agendamento-cliente">{row["Cliente"]}</div>
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

# ============================================================
# NOVO AGENDAMENTO
# ============================================================

elif pagina == "Novo agendamento":

    st.markdown('<div class="titulo">Novo agendamento</div>', unsafe_allow_html=True)
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
            st.session_state.servicos["Serviço"].tolist()
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
            ["Confirmado", "Pendente"]
        )

    servico_info = st.session_state.servicos[
        st.session_state.servicos["Serviço"] == servico
    ].iloc[0]

    st.markdown(
        f"""
        <div class="cliente-destaque">
            <div class="card-title">Resumo do atendimento</div>
            <strong>{servico}</strong><br>
            Duração aproximada: {servico_info["Duração"]} minutos<br>
            Valor: <strong>{dinheiro(servico_info["Preço"])}</strong>
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

        if not nome:
            st.error("Informe o nome da cliente.")

        else:

            novo = pd.DataFrame([[
                data,
                horario,
                nome,
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
                [st.session_state.agenda, novo],
                ignore_index=True
            )

            clientes = st.session_state.clientes

            if nome not in clientes["Cliente"].values:

                novo_cliente = pd.DataFrame([[
                    nome,
                    telefone,
                    data.strftime("%d/%m/%Y"),
                    0,
                    0.00
                ]], columns=clientes.columns)

                st.session_state.clientes = pd.concat(
                    [clientes, novo_cliente],
                    ignore_index=True
                )

            st.success(
                f"Agendamento de {nome} criado com sucesso."
            )

# ============================================================
# CLIENTES
# ============================================================

elif pagina == "Clientes":

    st.markdown('<div class="titulo">Clientes</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Conheça melhor quem frequenta o Aura Beauty Studio.</div>',
        unsafe_allow_html=True
    )

    clientes = st.session_state.clientes

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Clientes cadastradas",
        len(clientes)
    )

    c2.metric(
        "Clientes recorrentes",
        len(clientes[clientes["Visitas"] >= 5])
    )

    c3.metric(
        "Valor médio por cliente",
        dinheiro(clientes["Total Gasto"].mean())
    )

    st.markdown(
        '<div class="section-title">Ranking de clientes</div>',
        unsafe_allow_html=True
    )

    ranking = clientes.sort_values(
        "Total Gasto",
        ascending=False
    ).copy()

    ranking["Total Gasto"] = ranking["Total Gasto"].apply(dinheiro)

    st.dataframe(
        ranking,
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

        if novo_nome:

            novo_cliente = pd.DataFrame([[
                novo_nome,
                novo_telefone,
                date.today().strftime("%d/%m/%Y"),
                0,
                0.00
            ]], columns=clientes.columns)

            st.session_state.clientes = pd.concat(
                [clientes, novo_cliente],
                ignore_index=True
            )

            st.success("Cliente cadastrada com sucesso.")

        else:
            st.error("Informe o nome da cliente.")

# ============================================================
# SERVIÇOS
# ============================================================

elif pagina == "Serviços":

    st.markdown('<div class="titulo">Serviços</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Catálogo de serviços oferecidos pelo Aura Beauty Studio.</div>',
        unsafe_allow_html=True
    )

    servicos = st.session_state.servicos

    categorias = servicos["Categoria"].unique()

    for categoria in categorias:

        st.markdown(
            f'<div class="section-title">{categoria}</div>',
            unsafe_allow_html=True
        )

        dados = servicos[
            servicos["Categoria"] == categoria
        ]

        colunas = st.columns(3)

        for i, (_, row) in enumerate(dados.iterrows()):

            with colunas[i % 3]:

                st.markdown(
                    f"""
                    <div class="servico-card">
                        <div class="servico-cat">{row["Categoria"]}</div>
                        <div class="servico-nome">{row["Serviço"]}</div>
                        <div class="card-small">
                            Aproximadamente {row["Duração"]} minutos
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

    st.markdown('<div class="titulo">Financeiro</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Acompanhe o faturamento e o desempenho dos serviços.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    concluidos = agenda[
        agenda["Status"] == "Concluído"
    ].copy()

    if concluidos.empty:

        st.info("Ainda não existem atendimentos concluídos.")

    else:

        faturamento = concluidos["Valor"].sum()
        quantidade = len(concluidos)
        ticket = faturamento / quantidade

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Faturamento total",
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
            .sort_values("Faturamento", ascending=False)
        )

        col1, col2 = st.columns([1.2, 1])

        with col1:

            st.bar_chart(
                financeiro_servico["Faturamento"],
                height=350
            )

        with col2:

            tabela = financeiro_servico.copy()

            tabela["Ticket Médio"] = (
                tabela["Faturamento"] /
                tabela["Atendimentos"]
            )

            tabela["Faturamento"] = tabela["Faturamento"].apply(dinheiro)
            tabela["Ticket Médio"] = tabela["Ticket Médio"].apply(dinheiro)

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

# ============================================================
# FIDELIZAÇÃO
# ============================================================

elif pagina == "Fidelização":

    st.markdown('<div class="titulo">Fidelização</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitulo">Entenda o comportamento das clientes e descubra quem mais valoriza o studio.</div>',
        unsafe_allow_html=True
    )

    agenda = st.session_state.agenda

    concluidos = agenda[
        agenda["Status"] == "Concluído"
    ].copy()

    if concluidos.empty:

        st.info("Ainda não existem dados suficientes.")

    else:

        visitas = visitas_por_cliente(concluidos)

        cliente_fiel = visitas.sort_values(
            "Visitas",
            ascending=False
        ).index[0]

        maior_gasto = visitas.sort_values(
            "Gasto",
            ascending=False
        ).index[0]

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Cliente com mais visitas",
            cliente_fiel
        )

        c2.metric(
            "Cliente que mais gastou",
            maior_gasto
        )

        c3.metric(
            "Clientes recorrentes",
            len(visitas[visitas["Visitas"] >= 3])
        )

        st.markdown(
            '<div class="section-title">Clientes mais fiéis</div>',
            unsafe_allow_html=True
        )

        ranking_visitas = visitas.sort_values(
            ["Visitas", "Gasto"],
            ascending=False
        )

        st.dataframe(
            ranking_visitas,
            use_container_width=True
        )

        st.markdown(
            '<div class="section-title">Frequência das clientes</div>',
            unsafe_allow_html=True
        )

        frequencia = pd.cut(
            visitas["Visitas"],
            bins=[0, 2, 4, 7, 100],
            labels=[
                "1–2 visitas",
                "3–4 visitas",
                "5–7 visitas",
                "8+ visitas"
            ]
        )

        distribuicao = frequencia.value_counts().sort_index()

        st.bar_chart(
            distribuicao,
            height=300
        )

        st.markdown(
            '<div class="section-title">Oportunidades</div>',
            unsafe_allow_html=True
        )

        clientes_inativos = st.session_state.clientes.copy()

        clientes_inativos["Última"] = pd.to_datetime(
            clientes_inativos["Última Visita"],
            dayfirst=True,
            errors="coerce"
        )

        referencia = clientes_inativos["Última"].max()

        clientes_inativos["Dias sem visitar"] = (
            referencia - clientes_inativos["Última"]
        ).dt.days

        inativos = clientes_inativos[
            clientes_inativos["Dias sem visitar"] >= 7
        ]

        if not inativos.empty:

            st.markdown(
                f"""
                <div class="insight">
                    <strong>{len(inativos)} clientes</strong> estão há pelo menos
                    7 dias sem visitar o studio. Elas podem receber uma mensagem
                    de retorno pelo WhatsApp.
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <div class="insight">
                <strong>Estratégia de fidelização:</strong>
                clientes que já realizaram vários serviços podem receber
                combinações personalizadas, como unhas + sobrancelha ou
                cílios + sobrancelha.
            </div>
            """,
            unsafe_allow_html=True
        )
