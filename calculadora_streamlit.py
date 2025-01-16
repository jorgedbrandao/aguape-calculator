import streamlit as st

def calcular_dimensionamento(area, tipo_solo, declividade):
    """
    Cálculo fictício de quantos aspersores e metros de tubo são necessários,
    com ajustes simples por tipo de solo e declividade.
    """
    area_cobertura_por_aspersor = 50.0  # m² cobertos por aspersor (exemplo simples)

    # Base de aspersores
    base_aspersores = area / area_cobertura_por_aspersor

    # Ajuste por tipo de solo
    if tipo_solo.lower() == "arenoso":
        base_aspersores *= 1.10
    elif tipo_solo.lower() == "argiloso":
        base_aspersores *= 0.90

    # Ajuste por declividade
    if declividade > 10:
        base_aspersores *= 1.10
    elif declividade < -10:
        base_aspersores *= 0.90

    aspersores = int(round(base_aspersores))
    metros_tubo = aspersores * 5  # Exemplo: 5 metros de tubo por aspersor

    return aspersores, metros_tubo


def main():
    st.title("Calculadora de Irrigação")

    st.write("Preencha os dados para estimar aspersores e tubulação:")

    # Inputs
    area = st.number_input("Área (m²):", min_value=1.0, max_value=1000000.0, value=1000.0, step=100.0)
    tipo_solo = st.selectbox("Tipo de Solo:", ["Arenoso", "Argiloso", "Misto"])
    declividade = st.slider("Declividade (%):", min_value=-50, max_value=50, value=5)

    if st.button("Calcular"):
        aspersores, tubos = calcular_dimensionamento(area, tipo_solo, declividade)
        st.subheader("Resultado do Cálculo")
        st.write(f"- Aspersores necessários: **{aspersores}**")
        st.write(f"- Metros de tubo (aprox.): **{tubos}** m")

    st.write("---")
    st.info("Feito por Jorginho mt rápido")


if __name__ == "__main__":
    main()
