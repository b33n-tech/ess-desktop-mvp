import streamlit as st

st.set_page_config(page_title="Boîte à Outils Projets", layout="wide")

st.title("🚀 Boîte à Outils — Ton prochain move")

# --- ONBOARDING (niveau 1) ---
st.sidebar.header("💬 Ton profil")
maturite = st.sidebar.selectbox(
    "Niveau de maturité du projet",
    ["Idéation", "Early stage", "Structuration", "Croissance"]
)

besoin = st.sidebar.selectbox(
    "Ce dont tu as besoin maintenant",
    ["Financer", "Structurer", "Pitcher", "Connecter", "Apprendre"]
)

secteur = st.sidebar.text_input("Secteur / thématique")

st.sidebar.write("✅ Profil mis à jour")

# --- RECOMMANDATION PRINCIPALE ---
st.subheader("⭐ Recommandation principale")

if besoin == "Financer":
    st.success("📌 Opportunité : Candidater à l'appel à projets régional (deadline 15 février).")
    st.button("➡️ Candidater maintenant")
elif besoin == "Structurer":
    st.success("📌 Action clé : Rejoindre un pré-incubateur local pour 3 mois.")
    st.button("➡️ Postuler")
elif besoin == "Pitcher":
    st.success("📌 Action clé : Télécharger le template de pitch deck.")
    st.button("➡️ Télécharger")
elif besoin == "Connecter":
    st.success("📌 Opportunité : Participer au prochain meetup entrepreneurs de ta ville.")
    st.button("➡️ S'inscrire")
elif besoin == "Apprendre":
    st.success("📌 Ressource : Suivre le mini-bootcamp 'valider son marché'.")
    st.button("➡️ Accéder à la formation")

st.write("---")

# --- SUGGESTIONS ---
st.subheader("🔎 Suggestions pour toi")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧭 Pointer vers un mentor sectoriel")
    st.button("Contacter un mentor", key="mentor")

with col2:
    st.info("📄 Exemple de dossier AAP à télécharger")
    st.button("Télécharger modèle", key="modele")

with col3:
    st.info("🎤 Atelier pitch mercredi prochain")
    st.button("S'inscrire atelier", key="atelier")

st.write("---")

# --- EXPLORATION ---
st.subheader("📚 Explorer toutes les ressources")

type_filtre = st.selectbox(
    "Filtrer par type",
    ["Tous", "Financement", "Accompagnement", "Outils", "Événements"]
)

if type_filtre == "Financement":
    st.write("💰 Subvention Région - jusqu'à 10 000€")
    st.write("💰 Initiative locale - prêt d’honneur")
    st.write("💰 Fonds thématique - early stage")
elif type_filtre == "Accompagnement":
    st.write("🧪 Pré-incubateur local")
    st.write("🚀 Accélérateur impact")
    st.write("🧭 Atelier collectif")
elif type_filtre == "Outils":
    st.write("🧰 Modèle budget prévisionnel")
    st.write("🧰 Template pitch deck")
    st.write("🧰 Roadmap 90 jours")
elif type_filtre == "Événements":
    st.write("📅 Meetup entrepreneurs")
    st.write("📅 Conférence innovation sociale")
    st.write("📅 Workshop financement")
else:
    st.write("🔗 Mix de ressources (financement, contenus, événements…)")

st.write("---")

# FOOTER
st.caption("Prototype UX — version alpha")
