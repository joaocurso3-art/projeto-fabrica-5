import streamlit as st
import matplotlib.pyplot as plt

st.title("🌍 Crescimento Populacional — País A vs País B")

pop_a = st.number_input("População inicial do País A", value=80000, step=1000)
taxa_a = st.number_input("Taxa de crescimento anual do País A (%)", value=3.0, step=0.1)
pop_b = st.number_input("População inicial do País B", value=200000, step=1000)
taxa_b = st.number_input("Taxa de crescimento anual do País B (%)", value=1.5, step=0.1)

if st.button("Calcular"):
    if taxa_a <= taxa_b and pop_a < pop_b:
        st.warning("O País A nunca alcançará o País B com essas taxas.")
    else:
        a, b = pop_a, pop_b
        anos = 0
        lista_a = [a]
        lista_b = [b]
        anos_lista = [0]

        while a < b:
            a += a * (taxa_a / 100)
            b += b * (taxa_b / 100)
            anos += 1
            lista_a.append(a)
            lista_b.append(b)
            anos_lista.append(anos)

        st.success(f"Após {anos} anos, A alcança/ultrapassa B.")
        st.write(f"- País A: {int(a):,} habitantes")
        st.write(f"- País B: {int(b):,} habitantes")

        fig, ax = plt.subplots(figsize=(8,5))
        ax.plot(anos_lista, lista_a, label="País A", color="green", marker='o')
        ax.plot(anos_lista, lista_b, label="País B", color="red", marker='o')
        ax.fill_between(anos_lista, lista_a, lista_b, where=[pa>=pb for pa,pb in zip(lista_a, lista_b)],
                        facecolor='green', alpha=0.2, interpolate=True, label="A ultrapassa B")
        ax.set_xlabel("Anos")
        ax.set_ylabel("População")
        ax.set_title("Evolução da População de País A e País B")
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend()
        st.pyplot(fig)
