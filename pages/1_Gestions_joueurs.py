import streamlit as st
import pandas as pd
from database import queries


def inserer_joueur():
    st.header("Insertion d'un joueur")
    with st.form("form_insertion_joueur"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        categorie = st.selectbox("Catégorie", ["Junior", "Senior"])
        selection_nationale = st.text_input("Sélection nationale")
        poste_principal = st.selectbox("Poste principal", ["Gardien", "Défenseur", "Milieu", "Attaquant", "Latéral", "Pivot"])
        pied_fort = st.selectbox("Pied fort", ["Droit", "Gauche", "Ambidextre"])
        taille = st.number_input("Taille (cm)", min_value=100, max_value=250, step=1)
        poids = st.number_input("Poids (kg)", min_value=30.0, max_value=150.0, step=0.1)
        date_naissance = st.date_input("Date de naissance")
        
        if st.form_submit_button("Insérer"):
            queries.inserer_joueur(nom, prenom, categorie, selection_nationale, poste_principal, pied_fort, taille, poids, date_naissance)
            st.success(f"Joueur {nom} {prenom} inséré avec succès!")

def afficher_informations_joueurs():
    st.header("Informations des joueurs")
    joueur_id = st.selectbox("Sélectionnez un joueur", options=queries.get_all_player_ids())
    
    if joueur_id:
        evaluations = queries.get_player_evaluations(joueur_id)
        st.subheader(f"Évaluations du joueur ID {joueur_id}")
        st.write(evaluations)

def comparer_joueurs():
    st.header("Comparer les joueurs")
    joueurs_selectionnes = st.multiselect("Sélectionnez jusqu'à 3 joueurs", options=queries.get_all_player_ids(), max_selections=3)
    
    if st.button("Comparer"):
        if len(joueurs_selectionnes) < 2:
            st.warning("Veuillez sélectionner au moins 2 joueurs pour comparer leurs statistiques.")
            return
        
        donnees_joueurs = {joueur_id: queries.get_player_evaluations(joueur_id) for joueur_id in joueurs_selectionnes}
        st.subheader("Comparaison des statistiques")
        
        tableau_comparaison = pd.DataFrame({
            "ID Joueur": joueurs_selectionnes,
            "Moyenne Technique": [data['moyenne_technique'] for data in donnees_joueurs.values()],
            "Moyenne Tactique": [data['moyenne_tactique'] for data in donnees_joueurs.values()],
            "Moyenne Comportementale": [data['moyenne_comportementale'] for data in donnees_joueurs.values()],
            "Moyenne Générale": [data['moyenne_generale'] for data in donnees_joueurs.values()],
        })
        st.table(tableau_comparaison)

        for joueur_id, evaluations in donnees_joueurs.items():
            st.write(f"### Détails pour le joueur ID {joueur_id}")
            st.write(evaluations)

def main():
    st.title("Gestion des joueurs")
    
    # Tabs for different functionalities
    onglet = st.tabs(["Insertion d'un joueur", "Afficher les informations des joueurs", "Comparer les joueurs"])
    
    with onglet[0]:
        inserer_joueur()
    
    with onglet[1]:
        afficher_informations_joueurs()
    
    with onglet[2]:
        comparer_joueurs()

if __name__ == "__main__":
    main()