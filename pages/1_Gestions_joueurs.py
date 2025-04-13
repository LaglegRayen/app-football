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

        st.subheader("1️⃣ informations générale")
        col1, col2, col3 = st.columns(3)

        with col1:
            nom_prenom = st.text_input("Nom et prénom du joueur")
            nom_prenom = nom_prenom.strip()
            categorie = st.selectbox("Catégorie", ['Ecole B', 'Ecole A', 'Minimes B', 'Minimes A', 'Cadets B', 'Cadets A', 'Juniors', 'Seniors B', 'Seniors'    ])
            taille = st.number_input("Taille (cm)", min_value=100, max_value=250, step=1)

        with col2:
            date_naissance = st.date_input("Date de naissance")
            poste_principal = st.selectbox("Poste principal", ["Gardien", "Arrière droit", "Défenseur central droit", "Défenseur central gauche", "Arrière gauche", "Milieu défensif", "Milieu central", "Milieu offensif", "Ailier droit", "Ailier gauche", "Attaquant"])
            poids = st.number_input("Poids (kg)", min_value=30.0, max_value=150.0, step=0.1)

        with col3:
            nationalities = st.selectbox("Sélectionnez nationalité", ["Tunisie"])
            pied_fort = st.selectbox("Pied fort", ["Droit", "Gauche", "Ambidextre"])

        # 2️⃣ informations détaillée
        st.subheader("2️⃣ informations détaillée")
        col1, col2, col3 = st.columns(3)

        with col1:
            matchs_joues = st.number_input("Nombre de matchs joués", min_value=0, step=1)
            tempsjeu = st.number_input("Temps de jeu (minutes)", min_value=0, step=1)
            carton_jaune = st.number_input("Cartons jaunes", min_value=0, step=1)

        with col2:
            titulaire = st.number_input("Nombre de matchs titulaires", min_value=0, step=1)
            buts = st.number_input("Buts marqués", min_value=0, step=1)
            carton_rouge = st.number_input("Cartons rouges", min_value=0, step=1)

        with col3:
            remplacant = st.number_input("Nombre de matchs remplaçant", min_value=0, step=1)
            assists = st.number_input("Passes décisives", min_value=0, step=1)

        # Checkbox to check if the player is injured
        st.markdown("Est blessé")
        est_blesse = st.checkbox("Oui")

        # Display injury-related fields if the player is injured
        if est_blesse: 
            blesse = "Oui"

            # Injury-related fields will only be displayed when the player is injured
            with col1:
                type_blessure = st.selectbox("Type de blessure", ['Musculaire', 'Articulaire', 'Fracture', 'Ligamentaire', 'Tendinite', 'Commotion', 'Autre'])
                severite_blessure = st.selectbox("Sévérité de la blessure", ['Légère', 'Modérée', 'Grave', 'Très grave'])

            with col2:
                date_blessure = st.date_input("Date de blessure")
                description_blessure = st.text_area("Description de la blessure")

            with col3:
                date_retour_prevue = st.date_input("Date de retour prévue")

        else:
            blesse = "Non"
            type_blessure = None
            severite_blessure = None
            date_blessure = None
            description_blessure = None
            date_retour_prevue = None

        # Submit button to insert the player
        if st.form_submit_button("Insérer"):
            if not nom_prenom or not categorie or not taille or not date_naissance or not poste_principal or not poids or not nationalities or not pied_fort:
                st.error("Veuillez remplir les informations générale.")
            else:
                # Call the function to add the player to the database
                # Replace 'queries.ajouter_joueur' with your own insert function
                queries.ajouter_joueur(
                    nom_prenom, categorie, nationalities, poste_principal, pied_fort, taille, poids, date_naissance,
                    matchs_joues, titulaire, remplacant, tempsjeu, buts, assists, carton_jaune, carton_rouge,
                    blesse, type_blessure if est_blesse else None, date_blessure if est_blesse else None,
                    date_retour_prevue if est_blesse else None, severite_blessure if est_blesse else None, description_blessure if est_blesse else None
                )
                st.success(f"Joueur {nom_prenom} inséré avec succès!")





def afficher_statistiques_joueur():
    st.header("Informations du joueur")
    nom_prenom = st.text_input("Nom et prénom du joueur")
    joueur_id = None
    if nom_prenom:
        joueur_id = queries.recuperer_id_joueur(nom_prenom)
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
            "Nom Prénom", "Catégorie", "Sélection nationale", "Poste principal",
            "Pied fort", "Taille (cm)", "Poids (kg)", "Date de naissance",
            "Matchs joués", "Titulaire", "Remplaçant", "Temps de jeu (minutes)",
            "Buts marqués", "Passes décisives", "Cartons jaunes", "Cartons rouges",
            "Est blesse", "Type de blessure", "Date de blessure",
            "Date de retour prévue", "Sévérité de la blessure", "Description de la blessure"
        ]
        informations_joueur_df = pd.DataFrame(informations_joueur, columns=informations_joueur_df_columns)
        if not informations_joueur_df["Est blesse"].any():
            informations_joueur_df.drop(columns=["Type de blessure", "Date de blessure", "Date de retour prévue", "Sévérité de la blessure", "Description de la blessure"], inplace=True)
        
        informations_joueur_df["Est blesse"] = informations_joueur_df["Est blesse"].replace({1: "Oui", 0: "Non"}) 
        horizontal_df = informations_joueur_df.transpose()
        st.dataframe(horizontal_df, use_container_width=True)
        
        
        tab = st.tabs(["Évaluations sur periode", "Évaluations par matchs"])
        with tab[0]:
            
            st.subheader("Évaluations generales: ")
            evaluations_generales_sur_periode = queries.recuperer_evaluations_periode(joueur_id)
            evaluations_sur_periode = pd.DataFrame(evaluations_generales_sur_periode, columns=[
                "Date", "Moyenne Technique", "Moyenne Tactique", "Moyenne Comportementale","Moyenne Générale"
            ])

            evaluations_sur_periode = evaluations_sur_periode.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_sur_periode, use_container_width=True)
            
            
            
            
            st.subheader("Évaluations techniques: ")
            evaluations_techniques_sur_periode = queries.recuperer_evaluations_techniques_sur_periode(joueur_id)
            evaluations_techniques = pd.DataFrame(evaluations_techniques_sur_periode, columns=[
                "Date","qualite premiere touche", "qualite passes", "technique defensive",
                "sens tactique vision", "vitesse pensee", "anticipation", "adaptation adversaire", 
                "sens replacement", "sens demarquage", "sens marquage", "technique generale", "jeu tete", 
                "puissance frappe", "drible feinte", "technique au poste", "puissance physique", "rapidite",
                "Moyenne"])

            evaluations_techniques = evaluations_techniques.astype(str)
            evaluations_techniques = evaluations_techniques.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_techniques, use_container_width=True)
            
            
            
            st.subheader("Évaluations tactiques: ")
            evaluations_tactiques_sur_periode = queries.recuperer_evaluations_tactiques_sur_periode(joueur_id)
            evaluations_tactiques = pd.DataFrame(evaluations_tactiques_sur_periode, columns=[
                "Date","intelligence de jeu", "disponibilite", "jouer vers avant", 
                "jouer dos adversaires", "changer rythme", "Moyenne"])
            
            evaluations_tactiques = evaluations_tactiques.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_tactiques, use_container_width=True)
            
            
            st.subheader("Évaluations comportementales: ")
            evaluations_comportementales_sur_periode = queries.recuperer_evaluations_comportementales_sur_periode(joueur_id)
            evaluations_comportementales = pd.DataFrame(evaluations_comportementales_sur_periode, columns=[
                "Date", "assiduite", "motivation volonte", "confiance prise risque", 
                "calme maitrise soi", "combativite", "sportivite", "amabilite", "Moyenne"])
            evaluations_comportementales = evaluations_comportementales.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_comportementales, use_container_width=True)


            st.subheader("Tests Athlétiques")
            tests_athletiques = queries.recuperer_tests_athletiques(joueur_id)
            tests_athletiques_df = pd.DataFrame(tests_athletiques, columns=[
                "Periode", "Detente horizontale", "Detente verticale", 
                "Vitesse thalf test", "Vitesse 10m", "Vitesse 20m",
                "Vitesse 30m", "Aerobie vameval vo2max", "VMA km/h", 
                "VMA m/s", "Yoyo pal"
            ])
            st.dataframe(tests_athletiques_df, use_container_width=True)
            
            
            st.subheader("Tests Morphologiques")
            tests_morphologiques = queries.recuperer_tests_morphologiques(joueur_id)
            tests_morphologiques_df = pd.DataFrame(tests_morphologiques, columns=[
                "Periode", "Poids", "Taille", "IMC", "Masse grasse",
                "Classification IMC"
            ])
            st.dataframe(tests_morphologiques_df, use_container_width=True)
            
            
            
            st.subheader("Tests medicaux")
            tests_medicaux = queries.recuperer_tests_medicaux(joueur_id)
            tests_medicaux_df = pd.DataFrame(tests_medicaux, columns=[
                "Periode", "Taille", "Poids", "Masse grasse", "Examen général", 
                "Examen orthopédique", "Examen dentaire", "Examen ORL",  
                "Examen dermatologique", "Examen psychologique", "Commentaires"])
            
            st.dataframe(tests_medicaux_df, use_container_width=True)
            
            
            
            st.subheader("Suivi nutritionnel")
            suivi_nutritionnel = queries.recuperer_suivi_nutritionnel(joueur_id)
            suivi_nutritionnel_df = pd.DataFrame(suivi_nutritionnel, columns=[
                "Periode", "Age", "Poids départ", "Taille", "Objectif", "Détails objectif",
            "Régime spécifique", "Date premier suivi", "Date deuxième suivi", 
            "Date troisième suivi", "Évaluation premier suivi","Évaluation deuxième suivi", 
            "Évaluation troisième suivi", "Poids actuel", "Évolution poids", "Satisfaction",
            "Commentaires"

            ])
            st.dataframe(suivi_nutritionnel_df, use_container_width=True)
        
        with tab[1]:
            st.subheader("Évaluations generales: ")
            evaluations_generales_sur_match = queries.recuperer_evaluations_match(joueur_id)
            evaluations_sur_match = pd.DataFrame(evaluations_generales_sur_match, columns=[
                "Date", "Moyenne Technique", "Moyenne Tactique", "Moyenne Comportementale","Moyenne Générale"
            ])

            evaluations_sur_match = evaluations_sur_match.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_sur_match, use_container_width=True)
            
            
            
            
            st.subheader("Évaluations techniques: ")
            evaluations_techniques_sur_match = queries.recuperer_evaluations_techniques_sur_match(joueur_id)
            evaluations_techniques = pd.DataFrame(evaluations_techniques_sur_match, columns=[
                "Date","qualite premiere touche", "qualite passes", "technique defensive",
                "sens tactique vision", "vitesse pensee", "anticipation", "adaptation adversaire", 
                "sens replacement", "sens demarquage", "sens marquage", "technique generale", "jeu tete", 
                "puissance frappe", "drible feinte", "technique au_poste", "puissance physique", "rapidite",
                "Moyenne"])

            evaluations_techniques = evaluations_techniques.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_techniques, use_container_width=True)
            
            
            
            st.subheader("Évaluations tactiques: ")
            evaluations_tactiques_sur_match = queries.recuperer_evaluations_tactiques_sur_match(joueur_id)
            evaluations_tactiques = pd.DataFrame(evaluations_tactiques_sur_match, columns=[
                "Date","intelligence de jeu", "disponibilite", "jouer vers avant", 
                "jouer dos adversaires", "changer rythme", "Moyenne"])
            
            evaluations_tactiques = evaluations_tactiques.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_tactiques, use_container_width=True)
            
            
            st.subheader("Évaluations comportementales: ")
            evaluations_comportementales_sur_match = queries.recuperer_evaluations_comportementales_sur_match(joueur_id)
            evaluations_comportementales = pd.DataFrame(evaluations_comportementales_sur_match, columns=[
                "Date", "assiduite", "motivation volonte", "confiance prise risque", 
                "calme maitrise soi", "combativite", "sportivite", "amabilite", "Moyenne"])
            evaluations_comportementales = evaluations_comportementales.sort_values(by="Date", ascending=True)
            st.dataframe(evaluations_comportementales, use_container_width=True)

            numero_match = st.number_input("video du match numero ", min_value=0, max_value=evaluations_sur_match.shape[0])
            if st.button("Afficher la vidéo"):
                # print("evaluations-matchs-vids/evaluation-{}-{}-{}mp4".format(nom_prenom, str(queries.recuperer_adversaire(nom_prenom,evaluations_sur_match.iloc[numero_match]["Date"])),str(evaluations_sur_match.iloc[numero_match-1]["Date"])))
                st.video("evaluations-matchs-vids/evaluation-{}-{}-{}.mp4".format(nom_prenom, str(queries.recuperer_adversaire(nom_prenom,evaluations_sur_match.iloc[numero_match]["Date"])),str(evaluations_sur_match.iloc[numero_match-1]["Date"].date())))
        
        
        
        
        
        
        
        
        
        
        
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
        st.dataframe(tableau_comparaison, use_container_width=True)

        for joueur_id, evaluations in donnees_joueurs.items():
            st.write(f"### Détails pour le joueur ID {joueur_id}")
            st.write(evaluations)


def modification_suppression_joueur():
    st.header("Informations du joueur")
    nom_prenom = st.text_input("Nom et prénom du joueur", key = "nom_prenom_modif")
    joueur_id = None
    if nom_prenom:
        joueur_id = queries.recuperer_id_joueur(nom_prenom)
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
            "Nom Prénom", "Catégorie", "Sélection nationale", "Poste principal",
            "Pied fort", "Taille (cm)", "Poids (kg)", "Date de naissance",
            "Matchs joués", "Titulaire", "Remplaçant", "Temps de jeu (minutes)",
            "Buts marqués", "Passes décisives", "Cartons jaunes", "Cartons rouges",
            "Est blesse", "Type de blessure", "Date de blessure",
            "Date de retour prévue", "Sévérité de la blessure", "Description de la blessure"
        ]
        informations_joueur_df = pd.DataFrame(informations_joueur, columns=informations_joueur_df_columns)
        
        
        informations_joueur_df["Est blesse"] = informations_joueur_df["Est blesse"].replace({1: "Oui", 0: "Non"}) 

        general_info_df = informations_joueur_df[[
        "Nom Prénom", "Catégorie", "Sélection nationale", "Poste principal",
        "Pied fort", "Taille (cm)", "Poids (kg)", "Date de naissance"
        ]]

        stats_df = informations_joueur_df[[
            "Matchs joués", "Titulaire", "Remplaçant", "Temps de jeu (minutes)",
            "Buts marqués", "Passes décisives", "Cartons jaunes", "Cartons rouges"
        ]]

        injury_info_df = informations_joueur_df[[
            "Est blesse", "Type de blessure", "Date de blessure",
            "Date de retour prévue", "Sévérité de la blessure", "Description de la blessure"
        ]]
        
        
        st.markdown("#### Informations Générales")
        edited_general_info_df = st.data_editor(general_info_df, use_container_width=True)

        st.markdown("#### Statistiques")
        edited_stats_df = st.data_editor(stats_df, use_container_width=True)

        st.markdown("#### Informations sur les Blessures")
        edited_injury_info_df = st.data_editor(injury_info_df, use_container_width=True)


        if st.button("Enregistrer les modifications"):

            updated_general_info = edited_general_info_df.iloc[0].to_dict()
            updated_stats = edited_stats_df.iloc[0].to_dict()
            updated_injury_info = edited_injury_info_df.iloc[0].to_dict()


            updated_data = {**updated_general_info, **updated_stats, **updated_injury_info}

            if "Est blesse" in updated_data:
                updated_data["Est blesse"] = 1 if updated_data["Est blesse"] == "Oui" else 0

            queries.update_joueur(joueur_id, updated_data)
            st.success("Les informations du joueur ont été mises à jour avec succès!")

        
        
        
        
        
        
        
        
        
        
        

def main():
    st.title("Gestion des joueurs")
    
    # Tabs for different functionalities
    onglet = st.tabs(["Insertion d'un joueur", "statistiques joueur", "Comparer les joueurs", "modification et suppression"])
    
    with onglet[0]:
        inserer_joueur()
    
    with onglet[1]:
        afficher_statistiques_joueur()
    
    with onglet[2]:
        pass
        # comparer_joueurs()
    with onglet[3]:
        modification_suppression_joueur()

if __name__ == "__main__":
    main()
    
