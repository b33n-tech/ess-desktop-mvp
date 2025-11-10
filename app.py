import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projet v7", layout="wide")
st.title("🚀 Boîte à Outils Projet — Diagnostic par trajectoire")

# -------------------------------
# SECTION 1 : Fusée et trajectoire
# -------------------------------
st.subheader("🛰️ Étape 1 : Indique ton besoin actuel")

st.write("Clique sur la trajectoire pour indiquer où ton projet a besoin d’avancer. Chaque position déclenche un conseil ou next move adapté.")

# Définir des points fictifs sur la trajectoire
trajectory_points = [
    {"x": 10, "y": 50, "description": "Tu es en phase d’idéation : clarifie ton idée et explore ton marché."},
    {"x": 30, "y": 60, "description": "Early stage : commence à structurer ton projet et à identifier tes ressources."},
    {"x": 50, "y": 70, "description": "Structuration : formalise ton offre et prépare les premières demandes de financement."},
    {"x": 70, "y": 80, "description": "Croissance : teste ton marché, gagne en visibilité, et sécurise les financements."},
    {"x": 90, "y": 90, "description": "Expansion : consolide ton modèle et prépare ton passage à grande échelle."}
]

# Slider simulant le déplacement de la fusée le long de la trajectoire X
fusée_position = st.slider("Déplace la fusée le long de la trajectoire", 0, 100, 10, step=5)

# Identifier le point le plus proche
closest_point = min(trajectory_points, key=lambda p: abs(p["x"] - fusée_position))

# Afficher description / next move
st.success(f"📍 {closest_point['description']}")

st.write("---")

# -------------------------------
# SECTION 2 : Actions et ressources
# -------------------------------
st.subheader("🗺️ Étape 2 : Next moves et ressources")

# Exemple de next moves fictifs selon la position de la fusée
next_moves = {
    10: ["Atelier exploration idée", "Guide interviews utilisateurs"],
    30: ["Télécharger template business model", "Contact mentor local"],
    50: ["Préparer dossier AAP", "Workshop structuration projet"],
    70: ["Participer à pitch event", "Plan communication & visibilité"],
    90: ["Accéder à financement croissance", "Mentorat stratégie expansion"]
}

# Afficher next moves correspondant au point le plus proche
moves = next_moves.get(closest_point["x"], [])
st.write("💡 Next moves suggérés :")
for m in moves:
    st.write(f"- {m}")

# -------------------------------
# SECTION 3 : Dashboard de suivi simplifié
# -------------------------------
st.subheader("📊 Progression projet (simulée)")

progress_sim = closest_point["x"]
st.progress(progress_sim)

st.caption("Prototype UX v7 — fusée déplaçable selon le besoin exprimé, next moves contextualisés, expérience user-centric sans sliders multiples.")
