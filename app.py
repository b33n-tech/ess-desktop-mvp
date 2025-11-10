import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projet v4", layout="wide")

st.title("🚀 Copilote Projet — Ta trajectoire guidée")

# --- SECTION 1: Profil du projet ---
st.subheader("📌 État du projet")

phase = st.selectbox(
    "Phase actuelle du projet",
    ["Idéation", "Early stage", "Structuration", "Croissance"]
)

objectif = st.text_input("Objectif principal du moment", "Clarifier mon offre")

progress = st.session_state.get("progress", 40)

st.markdown(f"**Objectif du jour**: {objectif} | **Progrès**: {progress}%")

st.write("---")

# --- SECTION 2: Définition des actions possibles ---
# Chaque action a : titre, phase, objectif, impact, effort, ressources
if "actions" not in st.session_state:
    st.session_state.actions = [
        {"id": 1, "titre": "Atelier validation idée", "phase": "Idéation", "objectif": "Tester marché", "impact": 5, "effort": 2,
         "ressources": ["Template Business Model", "Guide interview utilisateurs"], "done": False},
        {"id": 2, "titre": "Télécharger template business model", "phase": "Idéation", "objectif": "Structurer offre", "impact": 4, "effort": 1,
         "ressources": ["Business Model Canva"], "done": False},
        {"id": 3, "titre": "Pré-incubateur local", "phase": "Early stage", "objectif": "Structurer", "impact": 5, "effort": 3,
         "ressources": ["Mentorat secteur", "Atelier gestion projet"], "done": False},
        {"id": 4, "titre": "Contacter mentor secteur", "phase": "Early stage", "objectif": "Structurer", "impact": 4, "effort": 2,
         "ressources": ["Liste mentors fictifs"], "done": False},
        {"id": 5, "titre": "Postuler AAP alimentation à impact", "phase": "Structuration", "objectif": "Financer", "impact": 5, "effort": 3,
         "ressources": ["Formulaire candidature", "Exemple dossier"], "done": False},
        {"id": 6, "titre": "Participer à workshop pitching", "phase": "Structuration", "objectif": "Pitcher", "impact": 4, "effort": 2,
         "ressources": ["Slides modèles", "Checklist pitch"], "done": False},
        {"id": 7, "titre": "Participer à événement sectoriel", "phase": "Croissance", "objectif": "Visibilité", "impact": 4, "effort": 2,
         "ressources": ["Networking guide", "Liste participants"], "done": False},
    ]

# --- SECTION 3: Calcul du next move ---
st.subheader("🔥 Next move prioritaire")

# Filtrer par phase et actions non réalisées
actions_phase = [a for a in st.session_state.actions if a["phase"] == phase and not a["done"]]

if actions_phase:
    # Prioriser selon impact/effort ratio
    actions_phase.sort(key=lambda x: (x["impact"]/x["effort"]), reverse=True)
    next_action = actions_phase[0]
    st.success(f"**{next_action['titre']}** — Impact: {next_action['impact']}, Effort: {next_action['effort']}")
    st.write("**Ressources attachées**:")
    for res in next_action["ressources"]:
        st.write(f"- {res}")

    if st.button("➡️ Valider action", key=next_action['id']):
        # Mettre à jour l'action comme faite
        for a in st.session_state.actions:
            if a["id"] == next_action["id"]:
                a["done"] = True
        # Mettre à jour la progression
        progress += int(next_action["impact"] * 2)  # exemple simple
        st.session_state.progress = min(progress, 100)
        st.experimental_rerun()
else:
    st.info("✅ Toutes les actions de cette phase sont réalisées ! Passe à la prochaine phase.")

st.write("---")

# --- SECTION 4: Timeline / Roadmap interactive ---
st.subheader("🗓️ Trajectoire du projet")

for a in st.session_state.actions:
    status = "✅ Réalisée" if a["done"] else "🔲 À faire"
    st.write(f"{a['titre']} | Phase: {a['phase']} | Objectif: {a['objectif']} | {status}")
    if not a["done"]:
        st.write("Ressources associées:")
        for res in a["ressources"]:
            st.write(f"- {res}")

st.write("---")
st.caption("Prototype UX v4 — copilote projet interactif, sans IA, avec trajectoire adaptative et ressources attachées")
