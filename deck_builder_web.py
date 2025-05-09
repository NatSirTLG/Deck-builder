
import streamlit as st

# Données des cartes
CARDS = {
    "Machina": {
        "Légendaires": ["M-L1", "M-L2"],
        "Rares": [f"M-R{i}" for i in range(1, 14)]
    },
    "Evil": {
        "Légendaires": ["E-L1", "E-L2"],
        "Rares": [f"E-R{i}" for i in range(1, 14)]
    },
    "Legends": {
        "Légendaires": ["L-L1", "L-L2"],
        "Rares": [f"L-R{i}" for i in range(1, 14)]
    }
}

st.set_page_config(page_title="Créateur de Deck", layout="centered")

st.title("Créateur de Deck (15 cartes max)")

# Choix de la famille
famille = st.selectbox("Choisis une famille", list(CARDS.keys()))
leg = CARDS[famille]["Légendaires"]
rares = CARDS[famille]["Rares"]

# Session state pour le deck
if "deck" not in st.session_state:
    st.session_state.deck = []

deck = st.session_state.deck

st.subheader("Cartes disponibles")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Légendaires")
    for card in leg:
        if st.button(f"Ajouter {card}"):
            if card in deck:
                st.warning(f"{card} est déjà dans le deck.")
            elif sum(1 for c in deck if c in leg) >= 2:
                st.error("Tu ne peux avoir que 2 légendaires.")
            elif len(deck) >= 15:
                st.error("Deck plein.")
            else:
                deck.append(card)
                st.success(f"{card} ajouté.")

with col2:
    st.markdown("### Rares")
    for card in rares:
        count = deck.count(card)
        if st.button(f"Ajouter {card} ({count}/2)"):
            if count >= 2:
                st.warning(f"{card} est déjà au max.")
            elif len(deck) >= 15:
                st.error("Deck plein.")
            else:
                deck.append(card)
                st.success(f"{card} ajouté.")

# Affichage du deck
st.subheader(f"Deck actuel ({len(deck)} / 15 cartes)")
for i, card in enumerate(deck):
    if st.button(f"Retirer {card}", key=f"rm_{i}"):
        deck.pop(i)
        st.experimental_rerun()

# Validation
if st.button("Valider le deck"):
    if len(deck) != 15:
        st.error("Le deck doit contenir exactement 15 cartes.")
    else:
        st.success("Deck validé avec succès !")

# Réinitialiser
if st.button("Réinitialiser le deck"):
    st.session_state.deck = []
    st.experimental_rerun()
