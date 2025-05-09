
import streamlit as st

# Données des cartes
CARDS = {
    "Machina": {
        "Légendaires": ["Biocat", "Golaimen"],
        "Rares": ["Angre-cig", "Atomicmush", "Fusox", "Machina_Rare_7", "Bzzzzip",
                "Anuvis", "Encable", "Machina_Rare_8", "Machina_Rare_9", "Machina_Rare_10",
                "Machina_Rare_11", "Machina_Rare_12", "Machina_Rare_13"]
    },
    "Evil": {
        "Légendaires": ["Chichipou", "Yagaström"],
        "Rares": ["Blindufer", "Arébat", "Katacroix", "Perçame", "Bob",
             "Cœurlette", "Sérandge", "Pandevil", "Mouspion", "Électruc",
             "Evil_Rare_11", "Evil_Rare_12", "Evil_Rare_13"]
    },
    "Legends": {
        "Légendaires": ["Superbin", "Serbyrinthe"],
        "Rares": ["Magicone", "Pizzaïdon", "Chegeva-Rat", "Hípopo", "Nainthore",
                "Gazper", "Supertoile", "Legends_Rare_8", "Legends_Rare_9", "Legends_Rare_10",
                "Legends_Rare_11", "Legends_Rare_12", "Legends_Rare_13"]
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
        if st.button(f"Ajouter {card}", key=f"add_leg_{card}"):
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
        if st.button(f"Ajouter {card} ({count}/2)", key=f"add_rare_{card}"):
            if count >= 2:
                st.warning(f"{card} est déjà au max.")
            elif len(deck) >= 15:
                st.error("Deck plein.")
            else:
                deck.append(card)
                st.success(f"{card} ajouté.")

# Affichage du deck
st.subheader(f"Deck actuel ({len(deck)} / 15 cartes)")
to_remove = None
for i, card in enumerate(deck):
    if st.button(f"Retirer {card}", key=f"rm_{i}"):
        to_remove = i
if to_remove is not None:
    deck.pop(to_remove)
    st.experimental_rerun()

# Validation
if st.button("Valider le deck", key="validate"):
    if len(deck) != 15:
        st.error("Le deck doit contenir exactement 15 cartes.")
    else:
        st.success("Deck validé avec succès !")

# Réinitialiser
if st.button("Réinitialiser le deck", key="reset"):
    st.session_state.deck = []
    st.experimental_rerun()
