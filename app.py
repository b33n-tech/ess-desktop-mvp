import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projet", layout="wide")

# --- HEADER ---
st.title("🚀 Dashboard Projet — Ton avancée maintenant")

# --- SECTION 1: État du projet ---
st.subheader("📌 Où j'en suis")
maturite = st.selectbox(
    "Phase actuelle du projet",
    ["Idéation", "Early stage", "Structuration", "Croissance"]
)

objectif = st.text_input("Objectif principal du moment", "Clarifier mon offre")

progress = st.slider("Progrès actuel", 0, 100, 40)

st.markdown(f"**Objectif du jour**: {objectif} | **Progrès**: {progress}%")

st.write("---")

# --- SECTION 2: Actions prioritaires ---
st.subheader("🔥 Prochaines actions")
actions = [
    {"titre": "Finaliser mon pitch 2 min", "type": "outil", "cta": "Télécharger modèle"},
    {"titre": "S'inscrire à l'atelier pitching", "type": "événement", "cta": "S'inscrire"},
    {"titre": "Contacter mentor alimentation", "type": "contact", "cta": "Envoyer mail"}
]

for action in actions:
    st.info(f"**{action['titre']}**")
    st.button(action['cta'], key=action['titre'])

st.write("---")

# --- SECTION 3: Opportunités et ressources contextuelles ---
st.subheader("💡 Opportunités pertinentes")
opportunites = [
    {"titre": "Appel à projet 'Alimentation à impact'", "deadline": "30 janvier", "montant": "10k€", "cta": "Déposer"},
    {"titre": "Atelier 'Tester son marché'", "date": "15 novembre", "cta": "S'inscrire"},
    {"titre": "Mentorat secteur alimentation", "cta": "Contacter"}
]

for opp in opportunites:
    if "deadline" in opp:
        st.success(f"**{opp['titre']}** — Deadline: {opp['deadline']} | Montant: {opp['montant']}")
    elif "date" in opp:
        st.success(f"**{opp['titre']}** — Date: {opp['date']}")
    else:
        st.success(f"**{opp['titre']}**")
    st.button(opp['cta'], key=opp['titre'])

st.write("---")

# --- FOOTER ---
st.caption("Prototype UX v2 — centrée sur ton projet et l'action immédiate")
