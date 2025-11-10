import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projet v3", layout="wide")

st.title("🚀 Dashboard Projet — Construis ta trajectoire")

# --- SECTION 1: Profil du projet ---
st.subheader("📌 État du projet")

phase = st.selectbox(
    "Phase actuelle du projet",
    ["Idéation", "Early stage", "Structuration", "Croissance"]
)

objectif = st.text_input("Objectif principal du moment", "Clarifier mon offre")

progress = st.slider("Progrès actuel (%)", 0, 100, 40)

st.markdown(f"**Objectif du jour**: {objectif} | **Progrès**: {progress}%")

st.write("---")

# --- SECTION 2: Définition des actions possibles ---
# Chaque action a : titre, phase, objectif, impact, effort
all_actions = [
    {"titre": "Atelier validation idée", "phase": "Idéation", "objectif": "Tester marché", "impact": 5, "effort": 2},
    {"titre": "Télécharger template business model", "phase": "Idéation", "objectif": "Structurer offre", "impact": 4, "effort": 1},
    {"titre": "Pré-incubateur local", "phase": "Early stage", "objectif": "Structurer", "impact": 5, "effort": 3},
    {"titre": "Contacter mentor secteur", "phase": "Early stage", "objectif": "Structurer", "impact": 4, "effort": 2},
    {"titre": "Postuler AAP alimentation à impact", "phase": "Structuration", "objectif": "Financer", "impact": 5, "effort": 3},
    {"titre": "Participer à workshop pitching", "phase": "Structuration", "objectif": "Pitcher", "impact": 4, "effort": 2},
    {"titre": "Participer à événement sectoriel", "phase": "Croissance", "objectif": "Visibilité", "impact": 4, "effort": 2},
]

# --- SECTION 3: Calcul du next move ---
st.subheader("🔥 Next move prioritaire")

# Filtrer par phase
actions_phase = [a for a in all_actions if a["phase"] == phase]

if actions_phase:
    # Prioriser selon impact/effort ratio
    actions_phase.sort(key=lambda x: (x["impact"]/x["effort"]), reverse=True)
    next_action = actions_phase[0]
    st.success(f"**{next_action['titre']}** — Impact: {next_action['impact']}, Effort: {next_action['effort']}")
    st.button("➡️ Valider action", key=next_action['titre'])
else:
    st.info("✅ Pas d'action prioritaire pour cette phase")

st.write("---")

# --- SECTION 4: Timeline / Roadmap ---
st.subheader("🗓️ Trajectoire du projet")

for a in all_actions:
    status = "🔲 À faire"
    st.write(f"{a['titre']} | Phase: {a['phase']} | Objectif: {a['objectif']} | {status}")

st.write("---")
st.caption("Prototype UX v3 — centrée projet, copilote sans IA")
