import streamlit as st
from datetime import date
from database import queries
min_date = date(2000, 1, 1)    
max_date = date.today() 
   
def ajouter_evaluation_sur_periode():
    
    
    st.subheader("Informations du Joueur")
    
    joueur_id = None
    age = None
    groupe = None
    categorie = st.selectbox("Catégorie", ['Ecole B', 'Ecole A', 'Minime B', 'Minime A', 'Cadet B', 'Cadet A', 'Junior', 'Seniors B', 'Senior'])

    nom_prenom_list = queries.recuperer_joueurs(categorie)

    if nom_prenom_list:
        nom_prenom = st.selectbox("Nom et Prénom du Joueur", list(nom_prenom_list), key = "nom_prenom_evaluation_periode")
        if nom_prenom:
            joueur_id = queries.recuperer_id_joueur(nom_prenom)
            age = queries.recuperer_age(joueur_id) #necessaire pour l'insertion du suivi nutritionnel
    else:
        st.warning("Aucun joueur trouvé pour cette catégorie.")

    
    
    periode_evaluation = st.selectbox("Période du Test", ["Période 1", "Période 2", "Période 3", "Période 4", "Période 5"])
    evaluation_date = st.date_input("Date de l'Évaluation", min_value=min_date, max_value=max_date)
    

    
    if evaluation_date and joueur_id:
        with st.form("form_evaluation_sur_periode"):
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
            
            moyenne_technique = (qualite_premiere_touche + qualite_passes + technique_defensive + sens_tactique_vision + vitesse_pensee +
                                 sens_replacement + adaptation_adversaire + sens_demarquage + sens_marquage +puissance_frappe +
                                    technique_generale + jeu_tete + puissance_physique + drible_feinte + rapidite+
                                    anticipation+technique_au_poste)/17 


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
            
            moyenne_tactique = (intelligence_de_jeu + disponibilite + jouer_vers_avant + changer_rythme + jouer_dos_adversaires)/5
            

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
            
            moyenne_comportementale = (assiduite + calme_maitrise_soi + amabilite + motivation_volonte + combativite +
                                        confiance_prise_risque + sportivite)/7


            
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
            if st.form_submit_button("Soumettre Évaluation"):
                
                
                id_evaluation_technique = queries.ajouter_evaluation_technique(joueur_id,evaluation_date, qualite_premiere_touche,
                    qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
                    anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage,
                    technique_generale, jeu_tete, puissance_frappe, drible_feinte,
                    technique_au_poste, puissance_physique, rapidite, moyenne_technique)
                
                id_evaluation_tactique = queries.ajouter_evaluation_tactique(joueur_id, evaluation_date, intelligence_de_jeu, disponibilite, jouer_vers_avant,
                    jouer_dos_adversaires, changer_rythme, moyenne_tactique)
                
                id_evaluation_comportementale = queries.ajouter_evaluation_comportementale(joueur_id, evaluation_date, 
                    assiduite, motivation_volonte, confiance_prise_risque,    
                    calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)

                id_test_athletique = queries.ajouter_test_athletique(joueur_id, categorie, evaluation_date, periode_evaluation, 
                    detente_horizontale, detente_verticale, vitesse_thalf_test, vitesse_10m,
                    vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal)
                
                id_test_morphologique = queries.ajouter_test_morphologique(joueur_id, evaluation_date, periode_evaluation, poids, taille, masse_grasse)

                id_test_medical = queries.ajouter_test_medical(joueur_id, categorie, evaluation_date, periode_evaluation, taille, 
                    poids, masse_grasse, examen_general, examen_orthopedique, examen_dentaire,
                    examen_orl, examen_dermatologique, examen_psychologique, commentaires)
                
            
                id_suivi_nutritionnel = queries.ajouter_suivi_nutritionnel(joueur_id, groupe, evaluation_date, periode_evaluation, 
                    age, poids_depart, taille, objectif, details_objectif, regime_specifique, 
                    date_premier_suivi, date_deuxieme_suivi, date_troisieme_suivi, eval_premier_suivi, 
                    eval_deuxieme_suivi , eval_troisieme_suivi, poids_actuel, 
                    satisfaction, commentaires)                

                moyenne_sur_periode = (moyenne_technique + moyenne_tactique + moyenne_comportementale)/3
                queries.ajouter_evaluation_sur_periode(
                    joueur_id,
                    periode_evaluation,
                    evaluation_date,
                    id_evaluation_technique,
                    id_evaluation_tactique,
                    id_evaluation_comportementale,
                    id_test_athletique,
                    id_test_morphologique,
                    id_test_medical,
                    id_suivi_nutritionnel,
                    moyenne_sur_periode

                )
                
                
                st.success("Évaluation ajoutée avec succès!")



def ajouter_evaluation_sur_match():
    st.subheader("Informations du Joueur")

    joueur_id = None
    date_match = None
    categorie = st.selectbox("Catégorie", ['Ecole B', 'Ecole A', 'Minimes B', 'Minimes A', 'Cadets B', 'Cadets A', 'Junior', 'Seniors B', 'Senior'], key ="categorie_evaluation_match")

    nom_prenom_list = queries.recuperer_joueurs(categorie)

    if nom_prenom_list:
        nom_prenom = st.selectbox("Nom et Prénom du Joueur", list(nom_prenom_list), key = "nom_prenom_evaluation_match")
        if nom_prenom:
            joueur_id = queries.recuperer_id_joueur(nom_prenom)
    if not joueur_id:
        st.warning("Aucun joueur trouvé pour cette categorie.")

    
    if joueur_id:
        Match = st.text_input("Match")
        Match = Match.upper()
        date_match = None
        if Match in queries.recuperer_matchs():
            date_list = [Date for Date in queries.recuperer_dates(Match)]
            date_match = st.selectbox("Date du Match", date_list)
            id_match = queries.recuperer_id_match(Match,date_match)
        else: 
            st.warning("Aucun match trouvé. Veuillez vérifier le nom du match.")
    

    if date_match:
        with st.form("form_evaluation_sur_match"):
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
            moyenne_technique = (qualite_premiere_touche + qualite_passes + technique_defensive + sens_tactique_vision + vitesse_pensee +
                                 sens_replacement + adaptation_adversaire + sens_demarquage + sens_marquage +puissance_frappe +
                                    technique_generale + jeu_tete + puissance_physique + drible_feinte + rapidite+
                                    anticipation+technique_au_poste)/17


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
                
            moyenne_tactique = (intelligence_de_jeu + disponibilite + jouer_vers_avant + changer_rythme + jouer_dos_adversaires)/5
            

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
            moyenne_comportementale = (assiduite + calme_maitrise_soi + amabilite + motivation_volonte + combativite +
                                        confiance_prise_risque + sportivite)/7


                
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
                    technique_au_poste, puissance_physique, rapidite, moyenne_technique)


                id_evaluation_tactique = queries.ajouter_evaluation_tactique(joueur_id, date_match, intelligence_de_jeu, disponibilite, jouer_vers_avant,
                    jouer_dos_adversaires, changer_rythme, moyenne_tactique)

                id_evaluation_comportementale = queries.ajouter_evaluation_comportementale(joueur_id, date_match, 
                    assiduite, motivation_volonte, confiance_prise_risque,    
                    calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)
                
                moyenne_evaluation_match = (moyenne_technique + moyenne_tactique + moyenne_comportementale)/3
                
                queries.ajouter_evaluation_sur_match(
                    joueur_id,
                    id_match,
                    id_evaluation_technique,
                    id_evaluation_tactique,
                    id_evaluation_comportementale,
                    moyenne_evaluation_match,
                    f"evaluations-matchs-vids/evaluation-{nom_prenom}-{Match}-{date_match}.mp4"
                    )
                
                
                 

                st.success("Évaluation ajoutée avec succès!")







def modification_suppression_evaluation():
    st.header("Informations du joueur")
    nom_prenom = st.text_input("Nom et prénom du joueur", key = "nom_prenom_modif")
    joueur_id = None

    if nom_prenom:
        joueur_id = queries.recuperer_id_joueur(nom_prenom)
        if not joueur_id:
            st.warning("Aucun joueur trouvé avec ce nom et prénom.")
            
        choose = st.selectbox("choose the type of evaluation", ["Évaluation par Periode", "Évaluation par Match"], key="choix_evaluation")

        if choose == "Évaluation par Match":
            choix = "evaluation_sur_match"
            Match = st.text_input("Match", key="Match")
            Match = Match.upper()
            date_match = None
        
            if Match:
                date_list = [Date for Date in queries.recuperer_dates(Match)]
                date_match = st.selectbox("Date du Match", date_list, key="Date du Match")
                id_match = queries.recuperer_id_match(Match, date_match)

                if not id_match:
                    st.warning("Aucun match trouvé avec ce nom et cette date.")
                
                choose_eval = st.selectbox("choose the evaluation", ["1️⃣ Évaluation Technique", "2️⃣ Évaluation Tactique", "3️⃣ Évaluation Comportementale"])

                if choose_eval == "1️⃣ Évaluation Technique":
                    table = "evaluation_technique"
                    id_table = "id_evaluation_technique"
                    id_match = queries.recuperer_id_match(Match, date_match)
                    id = queries.recuperer_evaluation_par_match(joueur_id, id_match, id_table, choix)
                    data = queries.recuperer_table(id, table)

                    if data is not None:  # Check if data is not None before using it
                        st.subheader("1️⃣ Évaluation Technique")
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            qualite_premiere_touche = st.number_input("Qualité de la Première Touche", 0, 5, value=data["qualite_premiere_touche"], key="tech_qualite_premiere_touche")
                            sens_tactique_vision = st.number_input("Sens Tactique et Vision", 0, 5, value=data["sens_tactique_vision"], key="tech_sens_tactique_vision")
                            adaptation_adversaire = st.number_input("Adaptation à l'Adversaire", 0, 5, value=data["adaptation_adversaire"], key="tech_adaptation_adversaire")
                            sens_marquage = st.number_input("Sens du Marquage", 0, 5, value=data["sens_marquage"], key="tech_sens_marquage")
                            puissance_frappe = st.number_input("Puissance de Frappe", 0, 5, value=data["puissance_frappe"], key="tech_puissance_frappe")
                            puissance_physique = st.number_input("Puissance Physique", 0, 5, value=data["puissance_physique"], key="tech_puissance_physique")

                        with col2:
                            qualite_passes = st.number_input("Qualité des Passes", 0, 5, value=data["qualite_passes"], key="tech_qualite_passes")
                            vitesse_pensee = st.number_input("Vitesse de Pensée", 0, 5, value=data["vitesse_pensee"], key="tech_vitesse_pensee")
                            sens_replacement = st.number_input("Sens du Replacement", 0, 5, value=data["sens_replacement"], key="tech_sens_replacement")
                            technique_generale = st.number_input("Technique Générale", 0, 5, value=data["technique_generale"], key="tech_technique_generale")
                            drible_feinte = st.number_input("Dribble et Feinte", 0, 5, value=data["drible_feinte"], key="tech_drible_feinte")
                            rapidite = st.number_input("Rapidité", 0, 5, value=data["rapidite"], key="tech_rapidite")

                        with col3:
                            technique_defensive = st.number_input("Technique Défensive", 0, 5, value=data["technique_defensive"], key="tech_technique_defensive")
                            anticipation = st.number_input("Anticipation", 0, 5, value=data["anticipation"], key="tech_anticipation")
                            sens_demarquage = st.number_input("Sens du Démarquage", 0, 5, value=data["sens_demarquage"], key="tech_sens_demarquage")
                            jeu_tete = st.number_input("Jeu de Tête", 0, 5, value=data["jeu_tete"], key="tech_jeu_tete")
                            technique_au_poste = st.number_input("Technique au Poste", 0, 5, value=data["technique_au_poste"], key="tech_technique_au_poste")
                    else:
                        st.warning("Aucune évaluation trouvée pour ce joueur et ce match.")


                elif choose_eval == "2️⃣ Évaluation Tactique":
                    table = "evaluation_tactique"
                    id_table = "id_evaluation_tactique"
                    id_match = queries.recuperer_id_match(Match, date_match)
                    id = queries.recuperer_evaluation_par_match(joueur_id, id_match, id_table, choix)
                    data = queries.recuperer_table(id, table)

                    if data is not None:  # Check if data is not None before using it
                        st.subheader("2️⃣ Évaluation Tactique")
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            intelligence_de_jeu = st.number_input("Intelligence de Jeu", 0, 5, value=data["intelligence_de_jeu"], key="tactique_intelligence_de_jeu")
                            jouer_dos_adversaires = st.number_input("Jouer Dos aux Adversaires", 0, 5, value=data["jouer_dos_adversaires"], key="tactique_jouer_dos_adversaires")

                        with col2:
                            disponibilite = st.number_input("Disponibilité", 0, 5, value=data["disponibilite"], key="tactique_disponibilite")
                            changer_rythme = st.number_input("Changer de Rythme", 0, 5, value=data["changer_rythme"], key="tactique_changer_rythme")

                        with col3:
                            jouer_vers_avant = st.number_input("Jouer vers l'Avant", 0, 5, value=data["jouer_vers_avant"], key="tactique_jouer_vers_avant")
                    else:
                        st.warning("Aucune évaluation trouvée pour ce joueur et ce match.")


                elif choose_eval == "3️⃣ Évaluation Comportementale":
                    table = "evaluation_comportementale"
                    id_table = "id_evaluation_comportementale"
                    id_match = queries.recuperer_id_match(Match, date_match)
                    id = queries.recuperer_evaluation_par_match(joueur_id, id_match, id_table, choix)
                    data = queries.recuperer_table(id, table)

                    if data is not None:  # Check if data is not None before using it
                        st.subheader("3️⃣ Évaluation Comportementale")
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            assiduite = st.number_input("Assiduité", 0, 5, value=data["assiduite"], key="comp_assiduite")
                            calme_maitrise_soi = st.number_input("Calme et Maîtrise de Soi", 0, 5, value=data["calme_maitrise_soi"], key="comp_calme_maitrise_soi")
                            amabilite = st.number_input("Amabilité", 0, 5, value=data["amabilite"], key="comp_amabilite")

                        with col2:
                            motivation_volonte = st.number_input("Motivation et Volonté", 0, 5, value=data["motivation_volonte"], key="comp_motivation_volonte")
                            combativite = st.number_input("Combativité", 0, 5, value=data["combativite"], key="comp_combativite")

                        with col3:
                            confiance_prise_risque = st.number_input("Confiance et Prise de Risque", 0, 5, value=data["confiance_prise_risque"], key="comp_confiance_prise_risque")
                            sportivite = st.number_input("Sportivité", 0, 5, value=data["sportivite"], key="comp_sportivite")
                    else:
                        st.warning("Aucune évaluation trouvée pour ce joueur et ce match.")


                
                if st.button("modifier"):
                    if table == "evaluation_technique":
                        queries.modifier_eval_par_match_technique(id, table, data, qualite_premiere_touche, qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
                            anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage,
                            technique_generale, jeu_tete, puissance_frappe, drible_feinte,
                            technique_au_poste, puissance_physique, rapidite)

                    elif table == "evaluation_tactique":
                        queries.modifier_eval_par_match_tactique(id, table, data, intelligence_de_jeu, disponibilite, jouer_vers_avant, jouer_dos_adversaires, changer_rythme)

                    elif table == "evaluation_comportementale":
                        queries.modifier_eval_par_match_comportementale(id, table, data, assiduite, motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite, sportivite, amabilite)

        
        
        else:
            periode_evaluation = st.selectbox("Période du Test", ["Période 1", "Période 2", "Période 3", "Période 4", "Période 5"], key="periode_evaluation")
            choix = "evaluation_sur_periode"

            if periode_evaluation:
                choose_eval = st.selectbox("choose the evaluation", ["1️⃣ Évaluation Technique", "2️⃣ Évaluation Tactique", "3️⃣ Évaluation Comportementale", "4️⃣ Test Athlétique", "5️⃣ Test Morphologique", "6️⃣ Test Médical", "7️⃣ Suivi Nutritionnel"])
                if choose_eval == "1️⃣ Évaluation Technique":
                    table = "evaluation_technique"
                    id_table = "id_evaluation_technique"
                    id = queries.recuperer_evaluation_par_periode(joueur_id, periode_evaluation, id_table, choix)
                    data = queries.recuperer_table(id, table)

                    if data is not None:
                        st.subheader("1️⃣ Évaluation Technique")
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            qualite_premiere_touche = st.number_input("Qualité de la Première Touche", 0, 5, value=data["qualite_premiere_touche"], key="tech_qualite_premiere_touche")
                            sens_tactique_vision = st.number_input("Sens Tactique et Vision", 0, 5, value=data["sens_tactique_vision"], key="tech_sens_tactique_vision")
                            adaptation_adversaire = st.number_input("Adaptation à l'Adversaire", 0, 5, value=data["adaptation_adversaire"], key="tech_adaptation_adversaire")
                            sens_marquage = st.number_input("Sens du Marquage", 0, 5, value=data["sens_marquage"], key="tech_sens_marquage")
                            puissance_frappe = st.number_input("Puissance de Frappe", 0, 5, value=data["puissance_frappe"], key="tech_puissance_frappe")
                            puissance_physique = st.number_input("Puissance Physique", 0, 5, value=data["puissance_physique"], key="tech_puissance_physique")

                        with col2:
                            qualite_passes = st.number_input("Qualité des Passes", 0, 5, value=data["qualite_passes"], key="tech_qualite_passes")
                            vitesse_pensee = st.number_input("Vitesse de Pensée", 0, 5, value=data["vitesse_pensee"], key="tech_vitesse_pensee")
                            sens_replacement = st.number_input("Sens du Replacement", 0, 5, value=data["sens_replacement"], key="tech_sens_replacement")
                            technique_generale = st.number_input("Technique Générale", 0, 5, value=data["technique_generale"], key="tech_technique_generale")
                            drible_feinte = st.number_input("Dribble et Feinte", 0, 5, value=data["drible_feinte"], key="tech_drible_feinte")
                            rapidite = st.number_input("Rapidité", 0, 5, value=data["rapidite"], key="tech_rapidite")

                        with col3:
                            technique_defensive = st.number_input("Technique Défensive", 0, 5, value=data["technique_defensive"], key="tech_technique_defensive")
                            anticipation = st.number_input("Anticipation", 0, 5, value=data["anticipation"], key="tech_anticipation")
                            sens_demarquage = st.number_input("Sens du Démarquage", 0, 5, value=data["sens_demarquage"], key="tech_sens_demarquage")
                            jeu_tete = st.number_input("Jeu de Tête", 0, 5, value=data["jeu_tete"], key="tech_jeu_tete")
                            technique_au_poste = st.number_input("Technique au Poste", 0, 5, value=data["technique_au_poste"], key="tech_technique_au_poste")
                    else:
                        st.warning("Aucune évaluation trouvée pour ce joueur et cette période.")
                    

                elif choose_eval == "2️⃣ Évaluation Tactique":
                    table = "evaluation_tactique"
                    id_table = "id_evaluation_tactique"
                    id = queries.recuperer_evaluation_par_periode(joueur_id, periode_evaluation, id_table, choix)
                    data = queries.recuperer_table(id, table)

                    if data is not None:  # Check if data is not None before using it
                        st.subheader("2️⃣ Évaluation Tactique")
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            intelligence_de_jeu = st.number_input("Intelligence de Jeu", 0, 5, value=data["intelligence_de_jeu"], key="tactique_intelligence_de_jeu")
                            jouer_dos_adversaires = st.number_input("Jouer Dos aux Adversaires", 0, 5, value=data["jouer_dos_adversaires"], key="tactique_jouer_dos_adversaires")

                        with col2:
                            disponibilite = st.number_input("Disponibilité", 0, 5, value=data["disponibilite"], key="tactique_disponibilite")
                            changer_rythme = st.number_input("Changer de Rythme", 0, 5, value=data["changer_rythme"], key="tactique_changer_rythme")

                        with col3:
                            jouer_vers_avant = st.number_input("Jouer vers l'Avant", 0, 5, value=data["jouer_vers_avant"], key="tactique_jouer_vers_avant")
                    else:
                        st.warning("Aucune évaluation trouvée pour ce joueur et ce match.")

                
                elif choose_eval == "3️⃣ Évaluation Comportementale":
                    table = "evaluation_comportementale"
                    id_table = "id_evaluation_comportementale"
                    id = queries.recuperer_evaluation_par_periode(joueur_id, periode_evaluation, id_table, choix)
                    data = queries.recuperer_table(id, table)

                    if data is not None:  # Check if data is not None before using it
                        st.subheader("3️⃣ Évaluation Comportementale")
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            assiduite = st.number_input("Assiduité", 0, 5, value=data["assiduite"], key="comp_assiduite")
                            calme_maitrise_soi = st.number_input("Calme et Maîtrise de Soi", 0, 5, value=data["calme_maitrise_soi"], key="comp_calme_maitrise_soi")
                            amabilite = st.number_input("Amabilité", 0, 5, value=data["amabilite"], key="comp_amabilite")

                        with col2:
                            motivation_volonte = st.number_input("Motivation et Volonté", 0, 5, value=data["motivation_volonte"], key="comp_motivation_volonte")
                            combativite = st.number_input("Combativité", 0, 5, value=data["combativite"], key="comp_combativite")

                        with col3:
                            confiance_prise_risque = st.number_input("Confiance et Prise de Risque", 0, 5, value=data["confiance_prise_risque"], key="comp_confiance_prise_risque")
                            sportivite = st.number_input("Sportivité", 0, 5, value=data["sportivite"], key="comp_sportivite")
                    else:
                        st.warning("Aucune évaluation trouvée pour ce joueur et ce match.")

                
                if st.button("modifier"):
                    if table == "evaluation_technique":
                        queries.modifier_eval_par_match_technique(id, table, data, qualite_premiere_touche, qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
                            anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage,
                            technique_generale, jeu_tete, puissance_frappe, drible_feinte,
                            technique_au_poste, puissance_physique, rapidite)

                    elif table == "evaluation_tactique":
                        queries.modifier_eval_par_match_tactique(id, table, data, intelligence_de_jeu, disponibilite, jouer_vers_avant, jouer_dos_adversaires, changer_rythme)

                    elif table == "evaluation_comportementale":
                        queries.modifier_eval_par_match_comportementale(id, table, data, assiduite, motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite, sportivite, amabilite)





def creer_evaluation():
    st.title("Ajouter une Évaluation")
    tab1,tab2,tab3 = st.tabs(["Évaluation par Periode","Évaluation par Match","Modification et Suppression"])
    
    with tab1:
       ajouter_evaluation_sur_periode()

    with tab2:
        ajouter_evaluation_sur_match()

    with tab3:
        modification_suppression_evaluation()


if __name__ == "__main__":
    
    creer_evaluation()