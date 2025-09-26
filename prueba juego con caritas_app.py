import streamlit as st

# -----------------------------
# Configuración inicial
# -----------------------------
st.set_page_config(page_title="Trivia Financiera", page_icon="💰", layout="centered")

# -----------------------------
# Base de preguntas
# -----------------------------
preguntas = [
    {
        "pregunta": "¿Qué es más importante al evaluar un préstamo?",
        "opciones": ["El monto prestado", "La tasa de interés y el plazo", "El banco que lo ofrece", "Si es a cuota fija o variable"],
        "respuesta": 1
    },
    {
        "pregunta": "Si tienes dos créditos con la misma tasa pero uno a 12 meses y otro a 36 meses, ¿cuál pagará menos intereses totales?",
        "opciones": ["El de 12 meses", "El de 36 meses", "Ambos pagan lo mismo", "Depende del banco"],
        "respuesta": 0
    },
    {
        "pregunta": "¿Qué significa TAE en finanzas?",
        "opciones": ["Tasa Anual Equivalente", "Tasa Ajustada Especial", "Tipo Anual Estándar", "Total de Ahorros Estimados"],
        "respuesta": 0
    },
    {
        "pregunta": "Si una inversión te ofrece 10% anual y otra 0.8% mensual, ¿cuál es mejor?",
        "opciones": ["La de 10% anual", "La de 0.8% mensual", "Son iguales", "Ninguna"],
        "respuesta": 1
    },
    {
        "pregunta": "¿Qué pasa si aumentas el plazo de un crédito?",
        "opciones": ["Bajan las cuotas pero suben los intereses totales", "Suben las cuotas y bajan los intereses", "Todo se mantiene igual", "Se elimina la deuda"],
        "respuesta": 0
    },
    {
        "pregunta": "¿Cuál es la principal ventaja del ahorro programado?",
        "opciones": ["Genera disciplina financiera", "Aumenta el endeudamiento", "Reduce tu puntaje crediticio", "Hace que gastes más"],
        "respuesta": 0
    },
    {
        "pregunta": "Si tienes un crédito al 20% anual y otro al 10% anual, ¿cuál conviene pagar primero?",
        "opciones": ["El de 20%", "El de 10%", "Da igual", "El más pequeño"],
        "respuesta": 0
    },
    {
        "pregunta": "¿Qué es diversificar en inversiones?",
        "opciones": ["Poner todo en un mismo activo", "Repartir en distintos activos", "Invertir solo en acciones", "Ahorrar en efectivo"],
        "respuesta": 1
    },
    {
        "pregunta": "¿Cuál es el indicador más usado para medir la inflación?",
        "opciones": ["PIB", "IPC", "Dólar", "Tasa de interés"],
        "respuesta": 1
    },
    {
        "pregunta": "Si ahorras $1,000,000 al 12% anual compuesto, ¿qué pasa al final del año?",
        "opciones": ["Tendrás $1,120,000", "Tendrás $1,120,000 más intereses", "Tendrás $1,120,000 exactos", "El dinero se devalúa"],
        "respuesta": 0
    }
]

# -----------------------------
# Estados iniciales
# -----------------------------
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "respondido" not in st.session_state:
    st.session_state.respondido = False

# -----------------------------
# Pantalla de inicio
# -----------------------------
if st.session_state.nombre == "":
    st.title("💰 Trivia Financiera")
    st.subheader("Pon a prueba tus conocimientos en finanzas personales y créditos.")
    nombre = st.text_input("Ingresa tu nombre para comenzar:")
    if st.button("Iniciar") and nombre.strip() != "":
        st.session_state.nombre = nombre
    st.stop()

# -----------------------------
# Mostrar progreso
# -----------------------------
indice = st.session_state.indice
puntaje = st.session_state.puntaje
total = len(preguntas)

st.progress(indice / total)

# -----------------------------
# Preguntas
# -----------------------------
if indice < total:
    pregunta = preguntas[indice]
    st.subheader(f"Pregunta {indice+1} de {total}")
    st.write(pregunta["pregunta"])
    opcion = st.radio("Selecciona una respuesta:", pregunta["opciones"], key=f"pregunta_{indice}")

    # Si aún no ha respondido esta pregunta
    if not st.session_state.respondido:
        if st.button("Responder", key=f"btn_{indice}"):
            st.session_state.respondido = True
            if pregunta["opciones"].index(opcion) == pregunta["respuesta"]:
                st.success("✅ ¡Correcto! 😃")
                st.session_state.puntaje += 1
            else:
                st.error(f"❌ Incorrecto 😢. La respuesta correcta es: {pregunta['opciones'][pregunta['respuesta']]}")

            # Puntaje acumulado
            st.info(f"📊 Puntaje actual: {st.session_state.puntaje} de {st.session_state.indice + 1}")

    # Si ya respondió, mostrar botón para pasar a la siguiente
    else:
        if st.button("➡️ Siguiente pregunta"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.rerun()

# -----------------------------
# Resultado final
# -----------------------------
else:
    st.markdown(f"## 🏆 Resultados de **{st.session_state.nombre}** 🏆")
    porcentaje = int((puntaje / total) * 100)
    st.markdown(f"### 📊 Puntaje final: **{puntaje}/{total}** ({porcentaje}%)")

    if porcentaje >= 80:
        st.success("🎉 Felicitaciones, ganaste. ¡Nivel experto en finanzas! 🟢 😎")
    elif porcentaje >= 60:
        st.warning("🙂 Sigue estudiando, vas por buen camino. 🟡 📘")
    else:
        st.error("📚 Debes reforzar tus conocimientos financieros. 🔴 😢")

    if st.button("🔄 Jugar de nuevo"):
        st.session_state.nombre = ""
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.respondido = False
        st.rerun()
