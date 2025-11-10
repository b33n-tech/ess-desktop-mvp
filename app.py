import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projet v8", layout="wide")
st.title("🚀 Copilote Projet — User-centric")

# -------------------------------
# Étape 1 : Où j'en suis
# -------------------------------
st.subheader("1️⃣ Où en est ton projet ?")

st.write("Déplace la fusée le long de la trajectoire pour indiquer ton niveau actuel de maturité.")

# Trajectoire fictive
trajectory_points = [
    {"x": 10, "label": "Je clarifie mon idée"},
    {"x": 30, "label": "Je structure mon projet"},
    {"x": 50, "label": "Je cherche des financements"},
    {"x": 70, "label": "Je teste et développe mon marché"},
    {"x": 90, "label": "Je prépare l'expansion"}
]

fusée_position = st.slider("Position de la fusée", 0, 100, 10, step=5)

# Identifier le point le plus proche
closest_point = min(trajectory_points, key=lambda p: abs(p["x"] - fusée_position))
st.info(f"Tu te situes ici : {closest_point['label']}")

st.write("---")

# -------------------------------
# Étape 2 : Ce que je veux
# -------------------------------
st.subheader("2️⃣ Ce que tu veux atteindre")

options_objectif = ["Valider mon idée", "Structurer mon projet", "Financer mon projet", "Tester mon marché", "Préparer l'expansion"]
objectif = st.selectbox("Sélectionne ton objectif actuel :", options_objectif)
st.write(f"Objectif choisi : **{objectif}**")

st.write("---")

# -------------------------------
# Étape 3 : Mon besoin
# -------------------------------
st.subheader("3️⃣ Mon besoin pour avancer")

options_besoin = ["Guides et templates", "Mentorat", "Ateliers / formations", "Financement", "Visibilité / communication"]
besoin = st.selectbox("Quel est ton besoin principal ?", options_besoin)
st.write(f"Besoin sélectionné : **{besoin}**")

st.write("---")

# -------------------------------
# Étape 4 : Next moves et ressources
# -------------------------------
st.subheader("4️⃣ Next moves suggérés")

# Mapping fictif pour next moves selon position et besoin
next_moves_map = {
    (10, "Guides et templates"): ["Télécharger guide business model", "Checklist interviews utilisateurs"],
    (10, "Mentorat"): ["Contacter un mentor idéation"],
    (30, "Ateliers / formations"): ["Participer à atelier structuration", "Workshop Pitch"],
    (30, "Financement"): ["Identifier sources AAP locales"],
    (50, "Financement"): ["Préparer dossier AAP alimentation à impact", "Postuler à subventions"],
    (50, "Visibilité / communication"): ["Plan communication initial", "Créer page projet sur plateforme"],
    (70, "Mentorat"): ["Trouver mentor marché cible"],
    (70, "Visibilité / communication"): ["Participer à événement sectoriel", "Networking guide"],
    (90, "Financement"): ["Accéder à financement croissance", "Rencontrer investisseurs"],
    (90, "Mentorat"): ["Mentorat stratégie expansion"]
}

# Récupérer next moves en fonction du point le plus proche et du besoin
next_moves = next_moves_map.get((closest_point["x"], besoin), ["Actions génériques à considérer"])
st.write("💡 Voici ce que tu peux faire pour avancer :")
for m in next_moves:
    st.write(f"- {m}")

st.write("---")

# -------------------------------
# Progression visuelle simplifiée
# -------------------------------
st.subheader("📊 Trajectoire / progression visuelle")
st.progress(fusée_position)

st.caption("Prototype UX v8 — user-centric, centrée sur le projet, simple et pragmatique, pas de diagnostic métier forcé.")
