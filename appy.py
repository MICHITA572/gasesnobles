# gasesnobles
import streamlit as st

# Constante universal de los gases en L·atm/mol·K
R = 0.0821

st.title("🔬 Calculadora de Gases Ideales")
st.markdown("Resuelve la ecuación de los gases ideales: **PV = nRT**")

# Selección de la variable a calcular
variable = st.selectbox(
    "¿Qué variable quieres calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

# Entradas dinámicas según la variable seleccionada
if variable == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es: {P:.3f} atm")

elif variable == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es: {V:.3f} L")

elif variable == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    n = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es: {T:.3f} K")

elif variable == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.01)
    V = st.number_input("Volumen (L)", min_value=0.01)
    T = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es: {n:.3f} mol")
