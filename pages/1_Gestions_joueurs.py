import streamlit as st
import pandas as pd
from database import queries
from datetime import date
import datetime as dt

min_date = date(2000, 1, 1)    
max_date_today = date.today()
max_date = date.today()+dt.timedelta(days=1825) 


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
        matchs_joues = st.number_input("Nombre de matchs joués", min_value=0, step=1)
        titulaire = st.number_input("Nombre de matchs titulaires", min_value=0, step=1)
        remplacant = st.number_input("Nombre de matchs remplaçant", min_value=0, step=1)
        tempsjeu = st.number_input("Temps de jeu (minutes)", min_value=0, step=1)
        buts = st.number_input("Buts marqués", min_value=0, step=1)
        assists = st.number_input("Passes décisives", min_value=0, step=1)
        carton_jaune = st.number_input("Cartons jaunes", min_value=0, step=1)
        carton_rouge = st.number_input("Cartons rouges", min_value=0, step=1)
        est_blesse = st.selectbox("Est blessé", ["Oui", "Non"])
        if est_blesse == "Oui":
            type_blessure = st.selectbox("Type de blessure", ['Musculaire', 'Articulaire', 'Fracture', 'Ligamentaire', 'Tendinite', 'Commotion', 'Autre'])
            date_blessure = st.date_input("Date de blessure", min_value=min_date, max_value=max_date_today)
            date_retour_prevue = st.date_input("Date de retour prévue", min_value=min_date, max_value=max_date)
            severite_blessure = st.selectbox("Sévérité de la blessure", ['Légère', 'Modérée', 'Grave', 'Très grave'])
            description_blessure = st.text_area("Description de la blessure")
        else:
            type_blessure = None
            date_blessure = None
            date_retour_prevue = None
            severite_blessure = None
            description_blessure = None
        
        if st.form_submit_button("Insérer"):
            est_blesse = est_blesse == "Oui"
            # queries.inserer_joueur(nom, prenom, categorie, selection_nationale,
            #     poste_principal, pied_fort, taille, poids, date_naissance,
            #     matchs_joues, titulaire, remplacant, tempsjeu,
            #     buts, assists, carton_jaune, carton_rouge,
            #     est_blessé, type_blessure, date_blessure,
            #     date_retour_prevue, severite_blessure, description_blessure
            #     )
            st.success(f"Joueur {nom} {prenom} inséré avec succès!")

def afficher_statistiques_joueur():
    st.header("Informations du joueur")
    nom = st.text_input("Nom du joueur")
    prenom = st.text_input("Prénom du joueur")
    joueur_id = None
    if nom and prenom:
        joueur_id = queries.recuperer_id_joueur(nom, prenom)
        if joueur_id:
            st.success(f"ID du joueur trouvé: {joueur_id}")
        else:
            st.warning("Aucun joueur trouvé avec ce nom et prénom.")
    
    if joueur_id:
        st.subheader(f"Informations du joueur:")
        informations_joueur = queries.recuperer_informations_joueur(joueur_id)
        if isinstance(informations_joueur, tuple):
            informations_joueur = [informations_joueur]
    
        informations_joueur_df_columns=[
            "Nom", "Prénom", "Catégorie", "Sélection nationale", "Poste principal",
            "Pied fort", "Taille (cm)", "Poids (kg)", "Date de naissance",
            "Matchs joués", "Titulaire", "Remplaçant", "Temps de jeu (minutes)",
            "Buts marqués", "Passes décisives", "Cartons jaunes", "Cartons rouges",
            "Est blessé", "Type de blessure", "Date de blessure",
            "Date de retour prévue", "Sévérité de la blessure", "Description de la blessure"
        ]
        informations_joueur_df = pd.DataFrame(informations_joueur, columns=informations_joueur_df_columns)
        if not informations_joueur_df["Est blessé"].any():
            informations_joueur_df.drop(columns=["Type de blessure", "Date de blessure", "Date de retour prévue", "Sévérité de la blessure", "Description de la blessure"], inplace=True)
        
        informations_joueur_df["Est blessé"] = informations_joueur_df["Est blessé"].replace({1: "Oui", 0: "Non"}) 
        horizontal_df = informations_joueur_df.transpose()
        st.table(horizontal_df)
        st.subheader("Évaluations Techniques, Tactiques et Comportementales")
        evaluations_generales = queries.recuperer_evaluations_generales(joueur_id)


        
        
        evaluations = pd.DataFrame(evaluations_generales, columns=[
            "Type", "Date", "Moyenne Technique", "Moyenne Tactique", "Moyenne Comportementale","Moyenne Générale"
        ])


        evaluations = evaluations.sort_values(by="Date", ascending=True)
        

        styled_evaluations_table = evaluations.style.set_properties(**{'white-space': 'nowrap'})
        st.write(styled_evaluations_table.to_html(index= False), unsafe_allow_html=True)
     


        st.subheader("Tests Athlétiques")
        tests_athletiques = queries.recuperer_tests_athletiques(joueur_id)
        tests_athletiques_df = pd.DataFrame(tests_athletiques, columns=[
            "Periode", "Detente horizontale", "Detente verticale", 
            "Vitesse thalf test", "Vitesse 10m", "Vitesse 20m",
            "Vitesse 30m", "Aerobie vameval vo2max", "VMA km/h", 
            "VMA m/s", "Yoyo pal"
        ])
        styled_tests_athletiques_table = tests_athletiques_df.style.set_properties(**{'white-space': 'nowrap'})
        st.write(styled_tests_athletiques_table.to_html(index= False), unsafe_allow_html=True)
        
        
        st.subheader("Tests Morphologiques")
        tests_morphologiques = queries.recuperer_tests_morphologiques(joueur_id)
        tests_morphologiques_df = pd.DataFrame(tests_morphologiques, columns=[
            "Periode", "Poids", "Taille", "IMC", "Masse grasse",
            "Classification IMC"
        ])
        styled_tests_morphologiques_table = tests_morphologiques_df.style.set_properties(**{'white-space': 'nowrap'})
        st.write(styled_tests_morphologiques_table.to_html(index= False), unsafe_allow_html=True)
        
        
        
        st.subheader("Tests medicaux")
        tests_medicaux = queries.recuperer_tests_medicaux(joueur_id)
        tests_medicaux_df = pd.DataFrame(tests_medicaux, columns=[
            "Periode", "Taille", "Poids", "Masse grasse", "Examen général", 
            "Examen orthopédique", "Examen dentaire", "Examen ORL",  
            "Examen dermatologique", "Examen psychologique", "Commentaires"])
        styled_tests_medicaux_table = tests_medicaux_df.style.set_properties(**{
            'white-space': 'nowrap'})

        st.write(styled_tests_medicaux_table.to_html(index= False), unsafe_allow_html=True)
        
        
        
        st.subheader("Suivi nutritionnel")
        suivi_nutritionnel = queries.recuperer_suivi_nutritionnel(joueur_id)
        suivi_nutritionnel_df = pd.DataFrame(suivi_nutritionnel, columns=[
            "Periode", "Age", "Poids départ", "Taille", "Objectif", "Détails objectif",
           "Régime spécifique", "Date premier suivi", "Date deuxième suivi", 
           "Date troisième suivi", "Évaluation premier suivi","Évaluation deuxième suivi", 
           "Évaluation troisième suivi", "Poids actuel", "Évolution poids", "Satisfaction",
           "Commentaires"

        ])
        styled_suivi_nutritionnel_table = suivi_nutritionnel_df.style.set_properties(**{
            'white-space': 'nowrap'})
        st.write(styled_suivi_nutritionnel_table.to_html(index= False), unsafe_allow_html=True) 
        
        
        
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
    onglet = st.tabs(["Insertion d'un joueur", "statistiques joueur", "Comparer les joueurs"])
    
    with onglet[0]:
        inserer_joueur()
    
    with onglet[1]:
        afficher_statistiques_joueur()
    
    with onglet[2]:
        pass
        # comparer_joueurs()

if __name__ == "__main__":
    main()
    
