import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projet v6", layout="wide")
st.title("🚀 Boîte à Outils Projet — Copilote interactif")

# -------------------------------
# SECTION 1 : Diagnostic ludique
# -------------------------------
st.subheader("🛰️ Étape 1 : Auto-diagnostiquer ton projet")

st.write("Déplace la fusée sur la barre pour indiquer où tu situes ton projet sur la trajectoire de maturité.")

# Simuler la fusée avec un slider
maturite = st.slider("Niveau de maturité (fusée)", 0, 100, 40, step=5)

# Axes secondaires fictifs (optionnel)
financement = st.slider("Besoin en financement", 0, 10, 5)
structuration = st.slider("Besoin en structuration", 0, 10, 5)
impact = st.slider("Besoin en impact / visibilité", 0, 10, 5)

# Générer un profil simplifié
if maturite < 25:
    profil = "Idéation"
elif maturite < 50:
    profil = "Early stage"
elif maturite < 75:
    profil = "Structuration"
else:
    profil = "Croissance"

st.markdown(f"**Profil estimé : {profil}**")
st.write("Axes de priorité : ", f"Financement {financement}/10", f"Structuration {structuration}/10", f"Impact {impact}/10")

st.write("---")

# -------------------------------
# SECTION 2 : Dashboard projet / copilote
# -------------------------------
st.subheader("🗺️ Étape 2 : Trajectoire et next move")

# Progression globale simulée
progress = st.session_state.get("progress", maturite)

st.markdown(f"**Progression actuelle du projet : {progress}%**")

# -------------------------------
# Actions fictives pour le copilote
# -------------------------------
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

# Filtrer actions selon profil (phase)
actions_phase = [a for a in st.session_state.actions if a["phase"] == profil and not a["done"]]

st.subheader("🔥 Next move prioritaire")
if actions_phase:
    # Prioriser selon impact/effort ratio
    actions_phase.sort(key=lambda x: (x["impact"]/x["effort"]), reverse=True)
    next_action = actions_phase[0]
    st.success(f"**{next_action['titre']}** — Impact: {next_action['impact']}, Effort: {next_action['effort']}")
    st.write("Ressources attachées :")
    for res in next_action["ressources"]:
        st.write(f"- {res}")

    if st.button("➡️ Valider action", key=next_action['id']):
        # Mettre à jour l'action comme faite
        for a in st.session_state.actions:
            if a["id"] == next_action["id"]:
                a["done"] = True
        # Mettre à jour la progression
        progress += int(next_action["impact"] * 2)
        st.session_state.progress = min(progress, 100)
        st.experimental_rerun()
else:
    st.info("✅ Toutes les actions de cette phase sont réalisées ! Passe à la prochaine phase.")

st.write("---")

# -------------------------------
# Timeline interactive
# -------------------------------
st.subheader("🗓️ Trajectoire du projet")

for a in st.session_state.actions:
    status = "✅ Réalisée" if a["done"] else "🔲 À faire"
    st.write(f"{a['titre']} | Phase: {a['phase']} | Objectif: {a['objectif']} | {status}")
    if not a["done"]:
        st.write("Ressources associées :")
        for res in a["ressources"]:
            st.write(f"- {res}")

st.write("---")
st.caption("Prototype UX v6 — diagnostic ludique, copilote projet interactif, ressources attachées, progression adaptative")
