import pymysql
from components import utils
from database import db_connection
import streamlit as st

def supprimer_joueur(joueur_id):
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        tables_to_clear = [
            "evaluation_sur_match",
            "evaluation_sur_periode",
            "evaluation_technique",
            "evaluation_tactique",
            "evaluation_comportementale",
            "test_athletique",
            "test_morphologique",
            "test_medical",
            "suivi_nutritionnel"

        ]
        
        for table in tables_to_clear:
            query = f"DELETE FROM {table} WHERE id_joueur = %s"
            cursor.execute(query, (joueur_id,))
        query = "DELETE FROM joueur WHERE id = %s"
        cursor.execute(query, (joueur_id,))
        db.commit()
        print("Joueur supprimé avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de la suppression du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()


def ajouter_evaluation_technique(id_joueur,evaluation_date, qualite_premiere_touche, 
    qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee, 
    anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, 
    sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte, 
    technique_au_poste, puissance_physique, rapidite, moyenne_technique):
    id = None
    try:
        
        db =db_connection.create_connection()
        cursor = db.cursor()

        query = """
        INSERT INTO evaluation_technique (id_joueur,evaluation_date, qualite_premiere_touche, 
        qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
        anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, 
        sens_marquage,technique_generale, jeu_tete, puissance_frappe, drible_feinte, 
        technique_au_poste, puissance_physique, rapidite,moyenne_technique)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        
        cursor.execute(query, (id_joueur,evaluation_date, qualite_premiere_touche,
        qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
        anticipation, adaptation_adversaire, sens_replacement, sens_demarquage,
        sens_marquage,technique_generale, jeu_tete, puissance_frappe, drible_feinte,
        technique_au_poste, puissance_physique, rapidite,moyenne_technique))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation technique ajoutée avec succès!")
        return id
        
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation technique: {e}")

    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
 
def ajouter_evaluation_tactique(id_joueur, evaluation_date, 
    intelligence_de_jeu, disponibilite, jouer_vers_avant,
    jouer_dos_adversaires, changer_rythme, moyenne_tactique):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        
        query = """
        INSERT INTO evaluation_tactique (id_joueur, evaluation_date, intelligence_de_jeu, disponibilite, jouer_vers_avant,
        jouer_dos_adversaires, changer_rythme, moyenne_tactique)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (id_joueur, evaluation_date, intelligence_de_jeu, disponibilite, jouer_vers_avant,
        jouer_dos_adversaires, changer_rythme,moyenne_tactique))
        db.commit()
        
        id = cursor.lastrowid
        print("Évaluation tactique ajoutée avec succès!")
        return id
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation tactique: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()    
        
def ajouter_evaluation_comportementale(id_joueur, evaluation_date, assiduite, 
    motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite,
    sportivite, amabilite, moyenne_comportementale):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        
        query = """
        INSERT INTO evaluation_comportementale (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque,
        calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque,
        calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation comportementale ajoutée avec succès!")
        return id
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation comportementale: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    
        
def ajouter_test_athletique(id_joueur, categorie, date_test, periode_test, 
    detente_horizontale, detente_verticale, vitesse_thalf_test, vitesse_10m,
    vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO test_athletique (id_joueur, categorie, date_test, periode_test, detente_horizontale, detente_verticale,
        vitesse_thalf_test, vitesse_10m, vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, categorie, date_test, periode_test, detente_horizontale, detente_verticale,
        vitesse_thalf_test, vitesse_10m, vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal))
        db.commit()
        id = cursor.lastrowid
        print("Test athlétique ajouté avec succès!")
        return id
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du test athlétique: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            


def ajouter_test_morphologique(id_joueur, date_test, periode_test, poids, taille, masse_grasse):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO test_morphologique (id_joueur, date_test, periode_test, poids, taille, masse_grasse)
        VALUES (%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, date_test, periode_test, poids, taille, masse_grasse))
        db.commit()
        id = cursor.lastrowid
        print("Test morphologique ajouté avec succès!")
        return id
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du test morphologique: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
        
def ajouter_test_medical(id_joueur, categorie, date_test, periode_test, taille, 
    poids, masse_grasse, examen_general, examen_orthopedique, examen_dentaire,
    examen_orl, examen_dermatologique, examen_psychologique, commentaires):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO test_medical (id_joueur, categorie, date_test, periode_test, taille, poids, masse_grasse,
        examen_general, examen_orthopedique, examen_dentaire, examen_orl, examen_dermatologique,
        examen_psychologique, commentaires)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, categorie, date_test, periode_test, taille, poids, masse_grasse,
        examen_general, examen_orthopedique, examen_dentaire, examen_orl, examen_dermatologique,
        examen_psychologique, commentaires))
        db.commit()
        id = cursor.lastrowid
        print("Test médical ajouté avec succès!")
        
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du test médical: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id


    
def ajouter_suivi_nutritionnel(id_joueur, groupe, date_creation, periode_test, 
    age, poids_depart, taille, objectif, details_objectif, regime_specifique, 
    date_premier_suivi, date_deuxieme_suivi, date_troisieme_suivi, eval_premier_suivi, 
    eval_deuxieme_suivi , eval_troisieme_suivi, poids_actuel, 
    satisfaction, commentaires):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO suivi_nutritionnel (id_joueur, groupe, date_creation, periode_test, age, poids_depart, taille,
        objectif, details_objectif, regime_specifique, date_premier_suivi, date_deuxieme_suivi, date_troisieme_suivi,
        eval_premier_suivi, eval_deuxieme_suivi , eval_troisieme_suivi, poids_actuel,
        satisfaction, commentaires) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, groupe, date_creation, periode_test, age, poids_depart, taille,
        objectif, details_objectif, regime_specifique, date_premier_suivi, date_deuxieme_suivi, date_troisieme_suivi,
        eval_premier_suivi, eval_deuxieme_suivi , eval_troisieme_suivi, poids_actuel,
        satisfaction, commentaires))
        db.commit()
        id = cursor.lastrowid
        print("Suivi nutritionnel ajouté avec succès!")
        return id
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du suivi nutritionnel: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id 


def ajouter_evaluation_sur_periode(id_joueur, periode, evaluation_date, id_evaluation_technique,
    id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, 
    id_test_morphologique, id_test_medical, id_suivi_nutritionnel, moyenne_sur_periode):
    id = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO evaluation_sur_periode (id_joueur, periode, evaluation_date, id_evaluation_technique,
        id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, 
        id_test_morphologique, id_test_medical, id_suivi_nutritionnel, moyenne_generale) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, periode, evaluation_date, id_evaluation_technique,
        id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, 
        id_test_morphologique, id_test_medical, id_suivi_nutritionnel, moyenne_sur_periode))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation ajoutée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation sur periode: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id
            
def ajouter_evaluation_sur_match(id_joueur, id_match, id_evaluation_technique,
    id_evaluation_tactique, id_evaluation_comportementale, moyenne_evaluation_match, videopath):
    id = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        INSERT INTO evaluation_sur_match (id_joueur, id_match, id_evaluation_technique,
        id_evaluation_tactique, id_evaluation_comportementale,moyenne_generale,videopath) VALUES (%s,%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, id_match, id_evaluation_technique,
        id_evaluation_tactique, id_evaluation_comportementale, moyenne_evaluation_match, videopath))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation ajoutée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation sur match: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id      



            
def ajouter_match(date_match, lieu, adversaire, type_match, domicile, score_equipe, score_adversaire, saison):
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()

        query = """
        INSERT INTO matchs (date_match, lieu, adversaire, type_match, domicile, score_equipe, score_adversaire, saison)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (date_match, lieu, adversaire, type_match, domicile, score_equipe, score_adversaire, saison))
        db.commit()
        print("Match inséré avec succès!")
    except pymysql.Error as err:
        print(f"Erreur lors de l'insertion du match: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()            
         
def ajouter_joueur(nom_prenom, categorie, nationalities,
        poste_principal, pied_fort, taille, poids, date_naissance,
        matchs_joues, titulaire, remplacant, tempsjeu,
        buts, assists, carton_jaune, carton_rouge,
        est_blesse, type_blessure, date_blessure,
        date_retour_prevue, severite_blessure, description_blessure):
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()

        query = """
        INSERT INTO joueur (nom_prenom, categorie, nationalities, 
        poste_principal, pied_fort, taille, poids, date_naissance, 
        matchs_joues, titulaire, remplacant, tempsjeu,
        buts, assists, carton_jaune, carton_rouge,
        est_blesse, type_blessure, date_blessure,
        date_retour_prevue, severite_blessure, description_blessure)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (nom_prenom, categorie,
            nationalities, poste_principal,
            pied_fort, taille, poids, date_naissance, matchs_joues, 
            titulaire, remplacant, tempsjeu,
            buts, assists, carton_jaune, carton_rouge,
            est_blesse, type_blessure, date_blessure,
            date_retour_prevue, severite_blessure, description_blessure))
        db.commit()
        print("Joueur inséré avec succès!")
    except pymysql.Error as err:
        print(f"Erreur lors de l'insertion du joueur: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()           



def recuperer_informations_joueur(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT nom_prenom, categorie, selection_nationale,
        poste_principal, pied_fort, taille, poids, date_naissance,
        matchs_joues, titulaire, remplacant, tempsjeu,
        buts, assists, carton_jaune, carton_rouge,
        est_blesse, type_blessure, date_blessure,
        date_retour_prevue, severite_blessure, description_blessure
        FROM joueur
        WHERE id = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchone()
        if not result:
            print("Aucun joueur trouvé avec cet ID.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des informations du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()            
  
def recuperer_age(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT DATEDIFF(CURDATE(), date_naissance) / 365 AS age
        FROM joueur
        WHERE id = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchone()
        if not result:
            print("Aucun joueur trouvé avec cet ID.")
        return result[0] if result else None
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de l'âge du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    
  
  
    
def recuperer_evaluations_periode(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_sur_periode.evaluation_date,
        evaluation_technique.moyenne_technique, evaluation_tactique.moyenne_tactique, 
        evaluation_comportementale.moyenne_comportementale,
        moyenne_generale
        
        FROM evaluation_sur_periode,evaluation_technique , evaluation_tactique,
        evaluation_comportementale
        WHERE evaluation_sur_periode.id_evaluation_technique = evaluation_technique.id
        AND evaluation_sur_periode.id_evaluation_tactique = evaluation_tactique.id
        AND evaluation_sur_periode.id_evaluation_comportementale = evaluation_comportementale.id
        AND evaluation_sur_periode.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()

        if not result:
            print("Aucune évaluation trouvée pour cette période.")
        return result
        
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations sur période: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()          

def recuperer_evaluations_generales(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        CREATE OR REPLACE VIEW evaluation_generale AS
        SELECT 'Periode' AS TYPE,e.evaluation_date AS Date,
        etec.moyenne_technique, etac.moyenne_tactique,
        ec.moyenne_comportementale, e.moyenne_generale
        FROM evaluation_sur_periode e,evaluation_technique etec, evaluation_tactique etac,
        evaluation_comportementale ec
        WHERE e.id_evaluation_technique = etec.id
        AND e.id_evaluation_tactique = etac.id
        AND e.id_evaluation_comportementale = ec.id
        AND e.id_joueur = %s
        UNION ALL
        SELECT 'Match' AS TYPE,m.date_match AS Date,
        etec.moyenne_technique, etac.moyenne_tactique,
        ec.moyenne_comportementale, e.moyenne_generale
        FROM evaluation_sur_match e,evaluation_technique etec , evaluation_tactique etac,
        evaluation_comportementale ec, matchs m
        WHERE e.id_evaluation_technique = etec.id
        AND e.id_evaluation_tactique = etac.id
        AND e.id_evaluation_comportementale = ec.id
        AND e.id_match = m.id
        AND e.id_joueur = %s
        """
        cursor.execute(query, (joueur_id, joueur_id))
        query = """
        SELECT * FROM evaluation_generale
        ORDER BY Date ASC;"""
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        if not result:
            print("Aucune évaluation trouvée pour cette période.")
        return result
    
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations générales: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_evaluations_techniques_sur_periode(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_technique.evaluation_date, qualite_premiere_touche, qualite_passes,
        technique_defensive, sens_tactique_vision, vitesse_pensee,
        anticipation, adaptation_adversaire, sens_replacement, sens_demarquage,
        sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte,
        technique_au_poste, puissance_physique, rapidite, moyenne_technique
        FROM evaluation_technique, evaluation_sur_periode
        WHERE evaluation_sur_periode.id_evaluation_technique = evaluation_technique.id 
        AND evaluation_sur_periode.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation technique trouvée pour ce joueur.")
        return result
    
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations techniques: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_evaluations_tactiques_sur_periode(joueur_id):
    result= None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_tactique.evaluation_date, intelligence_de_jeu, disponibilite,
        jouer_vers_avant, jouer_dos_adversaires, changer_rythme, moyenne_tactique
        FROM evaluation_tactique, evaluation_sur_periode
        WHERE evaluation_sur_periode.id_evaluation_tactique = evaluation_tactique.id 
        AND evaluation_sur_periode.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation tactique trouvée pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations tactiques: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
def recuperer_evaluations_comportementales_sur_periode(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_comportementale.evaluation_date, assiduite, motivation_volonte,
        confiance_prise_risque, calme_maitrise_soi, combativite,
        sportivite, amabilite, moyenne_comportementale
        FROM evaluation_comportementale,evaluation_sur_periode
        
        WHERE evaluation_sur_periode.id_evaluation_comportementale = evaluation_comportementale.id 
        AND evaluation_comportementale.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation comportementale trouvée pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations comportementales: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_evaluations_match(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT matchs.date_match, evaluation_technique.moyenne_technique, evaluation_tactique.moyenne_tactique,
        evaluation_comportementale.moyenne_comportementale, evaluation_sur_match.moyenne_generale
        FROM evaluation_sur_match, evaluation_technique, evaluation_tactique,
        evaluation_comportementale, matchs
        WHERE evaluation_sur_match.id_evaluation_technique = evaluation_technique.id
        AND evaluation_sur_match.id_evaluation_tactique = evaluation_tactique.id
        AND evaluation_sur_match.id_evaluation_comportementale = evaluation_comportementale.id
        AND evaluation_sur_match.id_match = matchs.id
        AND evaluation_sur_match.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation trouvée pour ce match.")
        return result
    
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations sur match: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_evaluations_techniques_sur_match(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_technique.evaluation_date, qualite_premiere_touche, qualite_passes,
        technique_defensive, sens_tactique_vision, vitesse_pensee,
        anticipation, adaptation_adversaire, sens_replacement, sens_demarquage,
        sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte,
        technique_au_poste, puissance_physique, rapidite, moyenne_technique
        FROM evaluation_technique, evaluation_sur_match
        WHERE evaluation_sur_match.id_evaluation_technique = evaluation_technique.id 
        AND evaluation_sur_match.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation technique trouvée pour ce joueur.")
        return result
    
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations techniques: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_evaluations_tactiques_sur_match(joueur_id):
    result= None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_tactique.evaluation_date, intelligence_de_jeu, disponibilite,
        jouer_vers_avant, jouer_dos_adversaires, changer_rythme, moyenne_tactique
        FROM evaluation_tactique, evaluation_sur_match
        WHERE evaluation_sur_match.id_evaluation_tactique = evaluation_tactique.id 
        AND evaluation_sur_match.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation tactique trouvée pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations tactiques: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
def recuperer_evaluations_comportementales_sur_match(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT evaluation_comportementale.evaluation_date, assiduite, motivation_volonte,
        confiance_prise_risque, calme_maitrise_soi, combativite,
        sportivite, amabilite, moyenne_comportementale
        FROM evaluation_comportementale,evaluation_sur_match
        
        WHERE evaluation_sur_match.id_evaluation_comportementale = evaluation_comportementale.id 
        AND evaluation_comportementale.id_joueur = %s
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucune évaluation comportementale trouvée pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations comportementales: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()


def recuperer_tests_athletiques(joueur_id):
    result = None 
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        # query  = """
        # SELECT * FROM test_athletique
        # WHERE test_athletique.id_joueur = %s
        # """
        query = """
        SELECT CONCAT(periode_test, " ", YEAR(date_test)) AS 'Periode',
        detente_horizontale AS 'Détente horizontale',
        detente_verticale AS 'Detente veriticale', vitesse_thalf_test AS 'Vitesse thalf test',
        vitesse_10m AS 'Vitesse 10m', vitesse_20m AS 'Vitesse 20m', 
        vitesse_30m AS 'Vitesse 30m', aerobie_vameval_vo2max AS 'Aerobie vameval vo2max',
        vma_kmh AS 'VMA km/h', vma_ms AS 'VMA m/s', yoyo_pal AS 'Yoyo pal'
        FROM test_athletique
        WHERE id_joueur = %s
        ORDER BY date_test ASC"""

        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucun autre test trouvé pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des autres tests: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_tests_morphologiques(joueur_id):
    result = None 
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query  = """
        SELECT CONCAT(periode_test, " ", YEAR(date_test)) AS 'Periode',
        poids AS 'Poids', taille AS 'Taille', imc AS 'IMC', masse_grasse AS 'Masse grasse',
        classification_imc AS 'Classification IMC'
        FROM test_morphologique
        WHERE id_joueur = %s
        ORDER BY date_test ASC
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucun test morphologique trouvé pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des tests morphologiques: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_tests_medicaux(joueur_id):
    result = None 
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query  = """
        SELECT CONCAT(periode_test, " ", YEAR(date_test)) AS 'Periode',
        taille AS 'Taille', poids AS 'Poids', masse_grasse AS 'Masse grasse',
        examen_general AS 'Examen général', examen_orthopedique AS 'Examen orthopédique',
        examen_dentaire AS 'Examen dentaire', examen_orl AS 'Examen ORL',
        examen_dermatologique AS 'Examen dermatologique', examen_psychologique AS 'Examen psychologique',
        commentaires AS 'Commentaires'
        FROM test_medical
        WHERE id_joueur = %s
        ORDER BY date_test ASC
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucun test médical trouvé pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des tests médicaux: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_suivi_nutritionnel(joueur_id):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query  = """
        SELECT CONCAT(periode_test, " ", YEAR(date_creation)) AS 'Periode',
        age AS 'Age', poids_depart AS 'Poids départ', taille AS 'Taille',
        objectif AS 'Objectif', details_objectif AS 'Détails objectif',
        regime_specifique AS 'Régime spécifique', date_premier_suivi AS 'Date premier suivi',
        date_deuxieme_suivi AS 'Date deuxième suivi', date_troisieme_suivi AS 'Date troisième suivi',
        eval_premier_suivi AS 'Évaluation premier suivi', eval_deuxieme_suivi AS 'Évaluation deuxième suivi',
        eval_troisieme_suivi AS 'Évaluation troisième suivi', poids_actuel AS 'Poids actuel',
        evolution_poids AS 'Évolution poids', satisfaction AS 'Satisfaction', 
        commentaires AS 'Commentaires'
        FROM suivi_nutritionnel
        WHERE id_joueur = %s
        ORDER BY date_creation ASC
        """
        cursor.execute(query, (joueur_id,))
        result = cursor.fetchall()
        if not result:
            print("Aucun suivi nutritionnel trouvé pour ce joueur.")
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération du suivi nutritionnel: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()


def recuperer_adversaire(nom_prenom,evalation_date):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT adversaire
        FROM matchs, joueur, evaluation_sur_match
        WHERE matchs.id = evaluation_sur_match.id_match
        AND joueur.id = evaluation_sur_match.id_joueur AND joueur.nom_prenom = %s AND date_match = %s;
        """
        cursor.execute(query, (nom_prenom, evalation_date))
        result = cursor.fetchone()
        if not result:
            print("Aucun adversaire trouvé avec ce nom et prénom.")
        return result[0] if result else None

    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de l'adversaire: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()




def comparer_joueurs(player_ids):
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT id_joueur, AVG(moyenne_generale) as moyenne_generale
        FROM evaluation_sur_match
        WHERE id_joueur IN (%s)
        GROUP BY id_joueur;
        """
        format_strings = ','.join(['%s'] * len(player_ids))
        cursor.execute(query % format_strings, tuple(player_ids))
        results = cursor.fetchall()
        return results
    except pymysql.Error as e:
        print(f"Erreur lors de la comparaison des joueurs: {e}")
        return []
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
def creer_fonction_moyenne_generale_sur_periode():
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        CREATE FUNCTION moyenne_generale_sur_periode(id_evaluation_technique INT,
                id_evaluation_tactique INT, id_evaluation_comportementale INT)
        RETURNS FLOAT
        DECLARE 
            moyenne_technique FLOAT;
            moyenne_tactique FLOAT;
            moyenne_comportementale FLOAT;
            moyenne_generale FLOAT;
        
        BEGIN
        
            SELECT evaluation_technique.moyenne_technique INTO moyenne_technique FROM evaluation_technique WHERE id_evaluation_technique = evaluation_technique.id_evaluation_technique;
            
            SELECT evaluation_tactique.moyenne_tactique INTO moyenne_tactique FROM evaluation_tactique WHERE id_evaluation_tactique = evaluation_tactique.id_evaluation_tactique;
            
            SELECT evaluation_comportementale.moyenne_comportementale INTO moyenne_comportementale FROM evaluation_comportementale WHERE id_evaluation_comportementale = evaluation_comportementale.id_evaluation_comportementale;
            
            SET moyenne_generale = (moyenne_technique + moyenne_tactique + moyenne_comportementale) / 3;
            
            RETURN moyenne;
        END;
        """
        cursor.execute(query)
        db.commit()
        print("Fonction créée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de la création de la fonction: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
                   
def creer_fonction_moyenne_match():
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        CREATE FUNCTION moyenne_match(id_evaluation_technique INT,
                id_evaluation_tactique INT, id_evaluation_comportementale INT)
        RETURNS FLOAT
        DECLARE 
            moyenne_technique FLOAT;
            moyenne_tactique FLOAT;
            moyenne_comportementale FLOAT;
            moyenne_generale FLOAT;
        
        BEGIN
        
            SELECT evaluation_technique.moyenne_technique INTO moyenne_technique FROM evaluation_technique WHERE id_evaluation_technique = evaluation_technique.id_evaluation_technique;
            
            SELECT evaluation_tactique.moyenne_tactique INTO moyenne_tactique FROM evaluation_tactique WHERE id_evaluation_tactique = evaluation_tactique.id_evaluation_tactique;
            
            SELECT evaluation_comportementale.moyenne_comportementale INTO moyenne_comportementale FROM evaluation_comportementale WHERE id_evaluation_comportementale = evaluation_comportementale.id_evaluation_comportementale;
            
            SET moyenne_generale = (moyenne_technique + moyenne_tactique + moyenne_comportementale) / 3;
            
            RETURN moyenne;
        END;
        """
        cursor.execute(query)
        db.commit()
        print("Fonction créée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de la création de la fonction: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
                        
def recuperer_id_joueur(nom_prenom):
    result = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT id FROM joueur WHERE nom_prenom = %s;
        """
        cursor.execute(query, (nom_prenom,))
        result = cursor.fetchone()
        if not result:
            print("Aucun joueur trouvé avec ce nom et prénom.")
        return result

            

    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de l'id du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    print(result)
    return result[0] if result else None

def update_joueur(joueur_id, updated_data):
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()

        query = """
        UPDATE joueur
        SET nom_prenom = %s, categorie = %s, nationalities = %s, poste_principal = %s,
            pied_fort = %s, taille = %s, poids = %s, date_naissance = %s,
            matchs_joues = %s, titulaire = %s, remplacant = %s, tempsjeu = %s,
            buts = %s, assists = %s, carton_jaune = %s, carton_rouge = %s,
            est_blesse = %s, type_blessure = %s, date_blessure = %s,
            date_retour_prevue = %s, severite_blessure = %s, description_blessure = %s
        WHERE id = %s
        """
        cursor.execute(query, (
            updated_data["Nom Prénom"], updated_data["Catégorie"], updated_data["Sélection nationale"],
            updated_data["Poste principal"], updated_data["Pied fort"], updated_data["Taille (cm)"],
            updated_data["Poids (kg)"], updated_data["Date de naissance"], updated_data["Matchs joués"],
            updated_data["Titulaire"], updated_data["Remplaçant"], updated_data["Temps de jeu (minutes)"],
            updated_data["Buts marqués"], updated_data["Passes décisives"], updated_data["Cartons jaunes"],
            updated_data["Cartons rouges"], updated_data["Est blesse"], updated_data["Type de blessure"],
            updated_data["Date de blessure"], updated_data["Date de retour prévue"],
            updated_data["Sévérité de la blessure"], updated_data["Description de la blessure"], joueur_id
        ))
        db.commit()
        print("Joueur mis à jour avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de la mise à jour du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
            
            
            
        
def recuperer_dates(Match):
    result = None
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT date_match FROM matchs WHERE adversaire = %s;"""
        cursor.execute(query, (utils.clean_string(Match),))
        result = cursor.fetchall()
        if not result:
            print("Aucun match trouve dans cette date")
            return 
        dates = [row[0] for row in result]
        return dates
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des dates: {e}")
    finally:    
        if 'db' in locals():
            cursor.close()
            db.close()
    return dates if dates else None
      
def recuperer_id_match(Match,date_match):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT id FROM matchs WHERE adversaire = %s AND date_match = %s;"""
        cursor.execute(query, (utils.clean_string(Match),date_match))
        result = cursor.fetchone()
        return result[0]
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de l'id du match: {e}")
    finally:    
        if 'db' in locals():
            cursor.close()
            db.close()
    
    



 
 
def selectionner_tous_les_joueurs():
    try:
        db =db_connection.create_connection()
        cursor = db.cursor()
        query = "SELECT * FROM joueur;"
        cursor.execute(query)
        joueurs = cursor.fetchall()
        return joueurs
    except pymysql.Error as err:
        print(f"Erreur lors de la sélection des joueurs: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
                    
def selectionner_tous_les_matchs():
    try:
        db =db_connection.create_connection()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM matchs;"
        cursor.execute(query)
        matchs = cursor.fetchall()
        return matchs
    except pymysql.Error as err:
        print(f"Erreur lors de la sélection des matchs: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()          
            
            
            

def recuperer_joueurs(categorie):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = "SELECT nom_prenom  FROM joueur WHERE categorie like '%{}%';"
        
        cursor.execute(query.format(categorie))
        
        result = cursor.fetchall()

        # Extract names from the fetched tuples and return them as a list
        if not result:
            print("Aucun joueur trouvé pour cette catégorie.")
        return [row[0] for row in result]
    except pymysql.Error as err:
        print(f"Erreur lors de la récupération des joueurs: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_matchs():
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = """
        SELECT adversaire FROM matchs;"""
        cursor.execute(query)
        result = cursor.fetchall()

        if not result:
            print("Aucun match trouvé.")
            return result 
        print([row[0] for row in result])
        return [row[0] for row in result]
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des matchs: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_id_evaluation_periode(joueur_id,periode_evaluation):
    pass


def recuperer_evaluation_par_match(joueur_id, id_match, id_table, choix):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = f"SELECT {id_table} FROM {choix} WHERE id_joueur = %s AND id_match = %s"
        cursor.execute(query, (joueur_id, id_match))
        result = cursor.fetchone()
        if not result:
            print("No evaluation found for this match.")
        else:
            return result[0]  # ✅ return the actual id value
            
    except pymysql.Error as e:
        print(f"Error while fetching evaluation by match: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()


    
def recuperer_table(id, table):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor(pymysql.cursors.DictCursor)  # This allows fetching rows as dictionaries
        query = f"SELECT * FROM {table} WHERE id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()  # This now returns a dictionary
        
        if not result:
            print("Aucune évaluation trouvée avec cet ID.")
        
        return result
        
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de la table: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()




def modifier_eval_par_match_technique(id, table, data, qualite_premiere_touche, qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee,
                            anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage,
                            technique_generale, jeu_tete, puissance_frappe, drible_feinte,
                            technique_au_poste, puissance_physique, rapidite):
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = f"""
        UPDATE {table}
        SET qualite_premiere_touche = %s,
            qualite_passes = %s,
            technique_defensive = %s,
            sens_tactique_vision = %s,
            vitesse_pensee = %s,
            anticipation = %s,
            adaptation_adversaire = %s,
            sens_replacement = %s,
            sens_demarquage = %s,
            sens_marquage = %s,
            technique_generale = %s,
            jeu_tete = %s,
            puissance_frappe = %s,
            drible_feinte = %s,
            technique_au_poste = %s,
            puissance_physique = %s,
            rapidite = %s
        WHERE id = %s;
        """

        cursor.execute(query, (
            qualite_premiere_touche,
            qualite_passes,
            technique_defensive,
            sens_tactique_vision,
            vitesse_pensee,
            anticipation,
            adaptation_adversaire,
            sens_replacement,
            sens_demarquage,
            sens_marquage,
            technique_generale,
            jeu_tete,
            puissance_frappe,
            drible_feinte,
            technique_au_poste,
            puissance_physique,
            rapidite,
            id
        ))
        db.commit()
        st.success("Évaluation technique mise à jour avec succès!")

    except pymysql.Error as err:
        st.error(f"Erreur lors de la mise à jour de l'évaluation technique: {err}")

    finally:
        if 'db' in locals():
            cursor.close()
            db.close()



def modifier_eval_par_match_tactique(id, table, data, intelligence_de_jeu, disponibilite, jouer_vers_avant, jouer_dos_adversaires, changer_rythme):
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = f"""
        UPDATE {table}
        SET intelligence_de_jeu = %s,
            disponibilite = %s,
            jouer_vers_avant = %s,
            jouer_dos_adversaires = %s,
            changer_rythme = %s
        WHERE id = %s;
        """
        cursor.execute(query, (
            intelligence_de_jeu,
            disponibilite,
            jouer_vers_avant,
            jouer_dos_adversaires,
            changer_rythme,
            id
        ))
        db.commit()
        st.success("Évaluation tactique mise à jour avec succès!")

    except pymysql.Error as err:
        st.error(f"Erreur lors de la mise à jour de l'évaluation tactique: {err}")

    finally:
        if 'db' in locals():
            cursor.close()
            db.close()



def modifier_eval_par_match_comportementale(id, table, data, assiduite, motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite, sportivite, amabilite):
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = f"""
        UPDATE {table}
        SET assiduite = %s,
            motivation_volonte = %s,
            confiance_prise_risque = %s,
            calme_maitrise_soi = %s,
            combativite = %s,
            sportivite = %s,
            amabilite = %s
        WHERE id = %s;
        """

        cursor.execute(query, (
            assiduite,
            motivation_volonte,
            confiance_prise_risque,
            calme_maitrise_soi,
            combativite,
            sportivite,
            amabilite,
            id
        ))
        db.commit()
        st.success("Évaluation comportementale mise à jour avec succès!")

    except pymysql.Error as err:
        st.error(f"Erreur lors de la mise à jour de l'évaluation comportementale: {err}")

    finally:
        if 'db' in locals():
            cursor.close()
            db.close()




def recuperer_evaluation_par_periode(joueur_id, periode_evaluation, id_table, choix):
    result = None
    try:
        db = db_connection.create_connection()
        cursor = db.cursor()
        query = f"SELECT {id_table} FROM {choix} WHERE id_joueur = %s AND periode_test = %s"
        cursor.execute(query, (joueur_id, periode_evaluation))
        result = cursor.fetchone()
        if not result:
            print("No evaluation found for this match.")
        else:
            return result[0]  # ✅ return the actual id value
            
    except pymysql.Error as e:
        print(f"Error while fetching evaluation by match: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()


