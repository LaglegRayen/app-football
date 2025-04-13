import streamlit as st
from datetime import date
from database import queries
min_date = date(2000, 1, 1)    
max_date = date.today() 
   
def ajouter_evaluation_sur_periode():
    
    
    st.subheader("Informations du Joueur")
    
    # Informations du joueur
    # Code to create the player selection
    categorie = st.selectbox("Catégorie", ['Ecole B', 'Ecole A', 'Minimes B', 'Minimes A', 'Cadets B', 'Cadets A', 'Juniors', 'Seniors B', 'Senior'])

    # Fetch the player list based on the selected category

    nom_prenom_list = queries.recuperer_joueurs(categorie)

    # Create the 'Nom et Prénom du Joueur' selectbox with the fetched player names
    if nom_prenom_list:
        nom_prenom = st.selectbox("Nom et Prénom du Joueur", list(nom_prenom_list))
    else:
        st.warning("Aucun joueur trouvé pour cette catégorie.")
    
    
    periode_evaluation = st.selectbox("Période du Test", ["Période 1", "Période 2", "Période 3", "Période 4", "Période 5"])
    
    # if nom_prenom:
    #     joueur_id = queries.recuperer_id_joueur(nom_prenom)
    #     if joueur_id:
    #         st.success(f"{nom_prenom} est trouvé")
    #     else:
    #         st.warning("Aucun joueur trouvé avec ce nom et prénom.")

    

    # Evaluation technique
    st.subheader("1️⃣ Évaluation Technique")
    col1, col2, col3 = st.columns(3)

    with col1:

        qualite_premiere_touche = st.number_input("Qualité de la Première Touche (intention, enchainer vers l'avant)", 0, 5)
        sens_tactique_vision = st.number_input("Sens Tactique et Vision", 0, 5)
        adaptation_adversaire = st.number_input("Adaptation à l'Adversaire", 0, 5)
        sens_marquage = st.number_input("Sens du Marquage", 0, 5)
        puissance_frappe = st.number_input("Puissance de Frappe", 0, 5)
        puissance_physique = st.number_input("Puissance Physique", 0, 5)


    with col2:
        qualite_passes = st.number_input("Qualité des Passes", 0, 5)
        vitesse_pensee = st.number_input("Vitesse de Pensée", 0, 5)
        sens_replacement = st.number_input("Sens du Replacement", 0, 5)
        technique_generale = st.number_input("Technique Générale", 0, 5)
        drible_feinte = st.number_input("Dribble et Feinte", 0, 5)
        rapidite = st.number_input("Rapidité", 0, 5)

    with col3:
        technique_defensive = st.number_input("Technique Défensive", 0, 5)
        anticipation = st.number_input("Anticipation", 0, 5)
        sens_demarquage = st.number_input("Sens du Démarquage", 0, 5)
        jeu_tete = st.number_input("Jeu de Tête", 0, 5)
        technique_au_poste = st.number_input("Technique au Poste", 0, 5)
        


    # Evaluation tactique
    st.subheader("2️⃣ Évaluation Tactique")
    col1, col2, col3 = st.columns(3)

    with col1:
        intelligence_de_jeu = st.number_input("Intelligence de Jeu", 0, 5)
        jouer_dos_adversaires = st.number_input("Jouer Dos aux Adversaires", 0, 5)

    with col2:
        disponibilite = st.number_input("Disponibilité", 0, 5)
        changer_rythme = st.number_input("Changer de Rythme", 0, 5)

    with col3:
        jouer_vers_avant = st.number_input("Jouer vers l'Avant", 0, 5)
    
    

    # Evaluation comportementale
    st.subheader("3️⃣ Évaluation Comportementale")
    col1, col2, col3 = st.columns(3)

    with col1:
        assiduite = st.number_input("Assiduité", 0, 5)
        calme_maitrise_soi = st.number_input("Calme et Maîtrise de Soi", 0, 5)
        amabilite = st.number_input("Amabilité", 0, 5)

    with col2:
        motivation_volonte = st.number_input("Motivation et Volonté", 0, 5)
        combativite = st.number_input("Combativité", 0, 5)
    
    with col3:
        confiance_prise_risque = st.number_input("Confiance et Prise de Risque", 0, 5)
        sportivite = st.number_input("Sportivité", 0, 5)
    


    
    #Test athletique
    st.subheader("4️⃣ Test Athlétique")
    col1, col2, col3 = st.columns(3)

    with col1:
        detente_horizontale = st.number_input("Détente Horizontale (en mètres)", min_value=0.0, step=0.1)
        vitesse_10m = st.number_input("Vitesse sur 10m (en secondes)", min_value=0.0, step=0.1)
        aerobie_vameval_vo2max = st.number_input("Aérobie VAMEVAL VO2max", min_value=0.0, step=0.1)
        yoyo_pal = st.number_input("Palier YOYO atteint", min_value=0, step=1)

    with col2:
        detente_verticale = st.number_input("Détente Verticale (en cm)", min_value=0.0, step=0.1)
        vitesse_20m = st.number_input("Vitesse sur 20m (en secondes)", min_value=0.0, step=0.1)
        vma_kmh = st.number_input("VMA (Vitesse Maximale Aérobie) en km/h", min_value=0.0, step=0.1)

    with col3:
        vitesse_thalf_test = st.number_input("Vitesse T-Half Test (en secondes)", min_value=0.0, step=0.1)
        vitesse_30m = st.number_input("Vitesse sur 30m (en secondes)", min_value=0.0, step=0.1)
        vma_ms = st.number_input("VMA (Vitesse Maximale Aérobie) en m/s", min_value=0.0, step=0.1)
    

    

    #Test morphologique
    st.subheader("5️⃣ Test Morphologique")

    col1, col2, col3 = st.columns(3)
    with col1:
        poids = st.number_input("Poids (en kg)", key = "poids_test_morphologique", min_value=0.0, step=0.1)

    with col2:
        taille = st.number_input("Taille (en cm)", min_value=0.0,key = "taille_test_morphologique", step=0.1)

    with col3:
        masse_grasse = st.number_input("Masse Grasse (en %)", key = "masse_grasse_test_morphologique", min_value=0.0, step=0.1,max_value=100.0)

    #Test medical
    st.subheader("6️⃣ Test Médical")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        taille = st.number_input("Taille (en cm)",key = "taille_test_medical", min_value=0.0, step=0.1)
        examen_general = st.number_input("Examen Général")
        examen_orl = st.number_input("Examen ORL", 0, 5)
        commentaires = st.text_area("Commentaires" ,key = "Commentaires_test_medical")

    with col2:
        poids = st.number_input("Poids (en kg)", key = "poids_test_medical", min_value=0.0, step=0.1)
        examen_orthopedique = st.number_input("Examen Orthopédique", 0, 5)
        examen_dermatologique = st.number_input("Examen Dermatologique", 0, 5)

    with col3:
        masse_grasse = st.number_input("Masse Grasse (en %)", key = "masse_grasse_test_medical", min_value=0.0, step=0.1, max_value=100.0)
        examen_dentaire = st.number_input("Examen Dentaire", 0, 5)
        examen_psychologique = st.number_input("Examen Psychologique", 0, 5)
    
    
    
    #Suivi nutritionnel
    st.subheader("7️⃣ Suivi Nutritionnel")
    col1, col2, col3 = st.columns(3)    
    with col1:
        poids_depart = st.number_input("Poids de Départ (en kg)", min_value=0.0, step=0.1)
        details_objectif = st.text_area("Détails de l'Objectif")
        date_deuxieme_suivi = st.date_input("Date du Deuxième Suivi", min_value=min_date, max_value=max_date)
        eval_deuxieme_suivi = st.text_input("Évaluation du Deuxième Suivi")
        satisfaction = st.number_input("Satisfaction", 0 ,5)

    with col2:
        taille = st.number_input("Taille (en cm)",key = "taille_suivi_nutritionnel", min_value=0.0, step=0.1)
        regime_specifique = st.text_area("Régime Spécifique")
        date_troisieme_suivi = st.date_input("Date du Troisième Suivi", min_value=min_date, max_value=max_date)
        eval_troisieme_suivi = st.text_input("Évaluation du Troisième Suivi")
        commentaires = st.text_area("Commentaires", key = "commentaires_suivi_nutrionnel")

    with col3:
        objectif = st.selectbox("Objectif", ['Perte poids', 'Prise masse', 'Maintien', 'Optimisation performance', 'Récomposition corporelle'])
        date_premier_suivi = st.date_input("Date du Premier Suivi", min_value=min_date, max_value=max_date)
        eval_premier_suivi = st.text_input("Évaluation du Premier Suivi")
        poids_actuel = st.number_input("Poids Actuel (en kg)", min_value=0.0, step=0.1)
    

    # submit button
    if st.button("Soumettre Évaluation"):
        pass
        
        # id_evaluation_technique = queries.ajouter_evaluation_technique(id_joueur,evaluation_date, qualite_premiere_touche,
        #     qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
        #     anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage,
        #     technique_generale, jeu_tete, puissance_frappe, drible_feinte,
        #     technique_au_poste, puissance_physique, rapidite)
        
        # id_evaluation_tactique = queries.ajouter_evaluation_tactique(id_joueur, evaluation_date, intelligence_de_jeu, disponibilite, jouer_vers_avant,
        #     jouer_dos_adversaires, changer_rythme)
        
        # id_evaluation_comportementale = queries.ajouter_evaluation_comportementale(id_joueur, evaluation_date, 
        #     assiduite, motivation_volonte, confiance_prise_risque,    
        #     calme_maitrise_soi, combativite, sportivite, amabilite)

        # id_test_athletique = queries.ajouter_test_athletique(id_joueur, categorie, evaluation_date, periode_evaluation, 
        #     detente_horizontale, detente_verticale, vitesse_thalf_test, vitesse_10m,
        #     vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal)
        
        # id_test_morphologique = queries.ajouter_test_morphologique(id_joueur, evaluation_date, periode_evaluation, poids, taille, masse_grasse)

        # id_test_medical = queries.ajouter_test_medical(id_joueur, categorie, evaluation_date, periode_evaluation, taille, 
        #     poids, masse_grasse, examen_general, examen_orthopedique, examen_dentaire,
        #     examen_orl, examen_dermatologique, examen_psychologique, commentaires)
        
    
        # id_suivi_nutritionnel = queries.ajouter_suivi_nutritionnel(id_joueur, groupe, evaluation_date, periode_evaluation, 
        #     age, poids_depart, taille, objectif, details_objectif, regime_specifique, 
        #     date_premier_suivi, date_deuxieme_suivi, date_troisieme_suivi, eval_premier_suivi, 
        #     eval_deuxieme_suivi , eval_troisieme_suivi, poids_actuel, 
        #     satisfaction, commentaires)                

        
        # queries.ajouter_evaluation_sur_periode(
        #     id_joueur,
        #     periode_evaluation,
        #     evaluation_date,
        #     id_evaluation_technique,
        #     id_evaluation_tactique,
        #     id_evaluation_comportementale,
        #     id_test_athletique,
        #     id_test_morphologique,
        #     id_test_medical,
        #     id_suivi_nutritionnel

        # )
        
        
        # st.success("Évaluation ajoutée avec succès!") 






def ajouter_evaluation_sur_match():
    st.subheader("Informations du Joueur")
    # Informations du joueur
    with st.form("form_evaluation_sur_match"):
        categorie = st.selectbox("Catégorie", ['Ecole B', 'Ecole A', 'Minimes B', 'Minimes A', 'Cadets B', 'Cadets A', 'Juniors', 'Seniors B', 'Senior'])

        # Fetch the player list based on the selected category

        nom_prenom_list = queries.recuperer_joueurs(categorie)

        # Create the 'Nom et Prénom du Joueur' selectbox with the fetched player names
        if nom_prenom_list:
            nom_prenom = st.selectbox("Nom et Prénom du Joueur", list(nom_prenom_list))
        else:
            st.warning("Aucun joueur trouvé pour cette catégorie.")


        Match = st.text_input("Match")
        Match = Match.upper()
        joueur_id = None
        date_match = None
        if nom_prenom:
                joueur_id = queries.recuperer_id_joueur(nom_prenom)
                if joueur_id:
                    st.success(f"ID du joueur trouvé: {joueur_id}")
                else:
                    st.warning("Aucun joueur trouvé avec ce nom et prénom.")
        if Match:
            date_list = [Date for Date in queries.recuperer_dates(Match)]
            date_match = st.selectbox("Date du Match", date_list)
            id_match = queries.recuperer_id_match(Match,date_match)
        
            if id_match:
                st.success(f"ID du match trouvé: {id_match}")
            else:
                st.warning("Aucun match trouvé avec ce nom et cette date.")
        
        
        # Evaluation technique
            st.subheader("1️⃣ Évaluation Technique")
            col1, col2, col3 = st.columns(3)

            with col1:

                qualite_premiere_touche = st.number_input("Qualité de la Première Touche", 0, 5)
                sens_tactique_vision = st.number_input("Sens Tactique et Vision", 0, 5)
                adaptation_adversaire = st.number_input("Adaptation à l'Adversaire", 0, 5)
                sens_marquage = st.number_input("Sens du Marquage", 0, 5)
                puissance_frappe = st.number_input("Puissance de Frappe", 0, 5)
                puissance_physique = st.number_input("Puissance Physique", 0, 5)


            with col2:
                qualite_passes = st.number_input("Qualité des Passes", 0, 5)
                vitesse_pensee = st.number_input("Vitesse de Pensée", 0, 5)
                sens_replacement = st.number_input("Sens du Replacement", 0, 5)
                technique_generale = st.number_input("Technique Générale", 0, 5)
                drible_feinte = st.number_input("Dribble et Feinte", 0, 5)
                rapidite = st.number_input("Rapidité", 0, 5)

            with col3:
                technique_defensive = st.number_input("Technique Défensive", 0, 5)
                anticipation = st.number_input("Anticipation", 0, 5)
                sens_demarquage = st.number_input("Sens du Démarquage", 0, 5)
                jeu_tete = st.number_input("Jeu de Tête", 0, 5)
                technique_au_poste = st.number_input("Technique au Poste", 0, 5)
                


            # Evaluation tactique
            st.subheader("2️⃣ Évaluation Tactique")
            col1, col2, col3 = st.columns(3)

            with col1:
                intelligence_de_jeu = st.number_input("Intelligence de Jeu", 0, 5)
                jouer_dos_adversaires = st.number_input("Jouer Dos aux Adversaires", 0, 5)

            with col2:
                disponibilite = st.number_input("Disponibilité", 0, 5)
                changer_rythme = st.number_input("Changer de Rythme", 0, 5)

            with col3:
                jouer_vers_avant = st.number_input("Jouer vers l'Avant", 0, 5)
            
            

            # Evaluation comportementale
            st.subheader("3️⃣ Évaluation Comportementale")
            col1, col2, col3 = st.columns(3)

            with col1:
                assiduite = st.number_input("Assiduité", 0, 5)
                calme_maitrise_soi = st.number_input("Calme et Maîtrise de Soi", 0, 5)
                amabilite = st.number_input("Amabilité", 0, 5)

            with col2:
                motivation_volonte = st.number_input("Motivation et Volonté", 0, 5)
                combativite = st.number_input("Combativité", 0, 5)
            
            with col3:
                confiance_prise_risque = st.number_input("Confiance et Prise de Risque", 0, 5)
                sportivite = st.number_input("Sportivité", 0, 5)



                
        if st.form_submit_button("Soumettre Évaluation"):
            if not joueur_id:
                st.warning("Veuillez d'abord verifier le nom et le prénom du joueur.")
                return
            
            if not id_match:
                st.warning("Veuillez d'abord verifier le nom et la date du match.")
                return
            
            id_evaluation_technique = queries.ajouter_evaluation_technique(joueur_id,date_match, qualite_premiere_touche,
                qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
                anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage,
                technique_generale, jeu_tete, puissance_frappe, drible_feinte,
                technique_au_poste, puissance_physique, rapidite)
            
        
            id_evaluation_tactique = queries.ajouter_evaluation_tactique(joueur_id, date_match, intelligence_de_jeu, disponibilite, jouer_vers_avant,
                jouer_dos_adversaires, changer_rythme)
            
            id_evaluation_comportementale = queries.ajouter_evaluation_comportementale(joueur_id, date_match, 
                assiduite, motivation_volonte, confiance_prise_risque,    
                calme_maitrise_soi, combativite, sportivite, amabilite)
            queries.ajouter_evaluation_sur_match(
                joueur_id,
                id_match,
                id_evaluation_technique,
                id_evaluation_tactique,
                id_evaluation_comportementale)
            
            st.success("Évaluation ajoutée avec succès!")




def creer_evaluation():
    st.title("Ajouter une Évaluation")
    tab1,tab2 = st.tabs(["Évaluation par Periode","Évaluation par Match"])
    
    with tab1:
       ajouter_evaluation_sur_periode()
    with tab2:
        ajouter_evaluation_sur_match()
        




if __name__ == "__main__":
    
    creer_evaluation()