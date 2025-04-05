import pymysql
from components import utils

#fonction d'insertion
def ajouter_joueur():
    pass

def ajouter_match(): 
    pass

def ajouter_evaluation_technique(id_joueur,evaluation_date, qualite_premiere_touche, 
    qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee, 
    anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, 
    sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte, 
    technique_au_poste, puissance_physique, rapidite):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        moy = (qualite_premiere_touche + qualite_passes + technique_defensive + sens_tactique_vision + vitesse_pensee + anticipation + adaptation_adversaire + sens_replacement + sens_demarquage + sens_marquage + technique_generale + jeu_tete + puissance_frappe + drible_feinte + technique_au_poste + puissance_physique + rapidite) / 17
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
        technique_au_poste, puissance_physique, rapidite,moy))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation technique ajoutée avec succès!")
        
        
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation technique: {e}")

    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    
    return id if id else None
  
def ajouter_evaluation_tactique(id_joueur, evaluation_date, 
    intelligence_de_jeu, disponibilite, jouer_vers_avant,
    jouer_dos_adversaires, changer_rythme):
    
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        moy = (intelligence_de_jeu + disponibilite + jouer_vers_avant + jouer_dos_adversaires + changer_rythme) / 5
        query = """
        INSERT INTO evaluation_tactique (id_joueur, evaluation_date, intelligence_de_jeu, disponibilite, jouer_vers_avant,
        jouer_dos_adversaires, changer_rythme, moyenne_tactique)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (id_joueur, evaluation_date, intelligence_de_jeu, disponibilite, jouer_vers_avant,
        jouer_dos_adversaires, changer_rythme, moy))
        db.commit()
        
        id = cursor.lastrowid
        print("Évaluation tactique ajoutée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation tactique: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id if id else None      
        
def ajouter_evaluation_comportementale(id_joueur, evaluation_date, assiduite, 
    motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite,
    sportivite, amabilite):
    
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        moy = (assiduite + motivation_volonte + confiance_prise_risque + calme_maitrise_soi + combativite + sportivite + amabilite) / 7
        query = """
        INSERT INTO evaluation_comportementale (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque,
        calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque,
        calme_maitrise_soi, combativite, sportivite, amabilite, moy))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation comportementale ajoutée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation comportementale: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id if id else None      
        
def ajouter_test_athletique(id_joueur, categorie, date_test, periode_test, 
    detente_horizontale, detente_verticale, vitesse_thalf_test, vitesse_10m,
    vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du test athlétique: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
    return id if id else None

def ajouter_test_morphologique(id_joueur, date_test, periode_test, poids, taille, masse_grasse):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        INSERT INTO test_morphologique (id_joueur, date_test, periode_test, poids, taille, masse_grasse)
        VALUES (%s,%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, date_test, periode_test, poids, taille, masse_grasse))
        db.commit()
        id = cursor.lastrowid
        print("Test morphologique ajouté avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du test morphologique: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id if id else None
        
def ajouter_test_medical(id_joueur, categorie, date_test, periode_test, taille, 
    poids, masse_grasse, examen_general, examen_orthopedique, examen_dentaire,
    examen_orl, examen_dermatologique, examen_psychologique, commentaires):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        INSERT INTO test_medical (id_joueur, categorie, date_test, periode_test, taille, poids, masse_grasse,
        examen_general, examen_orthopedique, examen_dentaire, examen_orl, examen_dermatologique,
        examen_psychologique, commentaires)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
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
    return id if id else None    
    
def ajouter_suivi_nutritionnel(id_joueur, groupe, date_creation, periode_test, 
    age, poids_depart, taille, objectif, details_objectif, regime_specifique, 
    date_premier_suivi, date_deuxieme_suivi, date_troisieme_suivi, eval_premier_suivi, 
    eval_deuxieme_suivi , eval_troisieme_suivi, poids_actuel, 
    satisfaction, commentaires):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion du suivi nutritionnel: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id if id else None

def ajouter_evaluation_sur_periode(id_joueur, periode, evaluation_date, id_evaluation_technique,
    id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, 
    id_test_morphologique, id_test_medical, id_suivi_nutritionnel, id_suivi_psychologique,
    id_test_physique):
    
        try:
            db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
            )
            cursor = db.cursor()
            query = """
            INSERT INTO evaluation_generale_periode (id_joueur, periode, evaluation_date, id_evaluation_technique,
            id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, 
            id_test_morphologique, id_test_medical, id_suivi_nutritionnel, id_suivi_psychologique,
            id_test_physique) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """
            cursor.execute(query, (id_joueur, periode, evaluation_date, id_evaluation_technique,
            id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, 
            id_test_morphologique, id_test_medical, id_suivi_nutritionnel, id_suivi_psychologique,
            id_test_physique))
            db.commit()
            id = cursor.lastrowid
            print("Évaluation ajoutée avec succès!")
        except pymysql.Error as e:
            print(f"Erreur lors de l'insertion de l'évaluation: {e}")
        finally:
            if 'db' in locals():
                cursor.close()
                db.close()
        return id if id else None
            
def ajouter_evaluation_sur_match(id_joueur, id_match, id_evaluation_technique,
    id_evaluation_tactique, id_evaluation_comportementale):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        INSERT INTO evaluation_sur_match (id_joueur, id_match, id_evaluation_technique,
        id_evaluation_tactique, id_evaluation_comportementale) VALUES (%s,%s,%s,%s,%s);
        """
        cursor.execute(query, (id_joueur, id_match, id_evaluation_technique,
        id_evaluation_tactique, id_evaluation_comportementale))
        db.commit()
        id = cursor.lastrowid
        print("Évaluation ajoutée avec succès!")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion de l'évaluation: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return id if id else None          
            


def inserer_joueur(nom, prenom, categorie, selection_nationale, poste_principal, pied_fort, taille, poids, date_naissance):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()

        query = """
        INSERT INTO joueur (nom, prenom, categorie, selection_nationale, poste_principal, pied_fort, taille, poids, date_naissance)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (nom, prenom, categorie, selection_nationale, poste_principal, pied_fort, taille, poids, date_naissance))
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

def inserer_match(date_match, lieu, adversaire, type_match, domicile, score_equipe, score_adversaire, saison):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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

            
            
    
          


def recuperer_evaluation_periode(start_date, end_date):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        SELECT * FROM evaluation_generale_periode
        WHERE date_debut >= %s AND date_fin <= %s;
        """
        cursor.execute(query, (start_date, end_date))
        results = cursor.fetchall()
        return results
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations: {e}")
        return []
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def recuperer_evaluations_match(id_match):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        SELECT * FROM evaluation_sur_match
        WHERE id_match = %s;
        """
        cursor.execute(query, (id_match,))
        results = cursor.fetchall()
        return results
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des évaluations de match: {e}")
        return []
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def comparer_joueurs(player_ids):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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
            
def recuperer_joueurs(n, p):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        SELECT id_joueur FROM joueur 
        WHERE nom = n AND prenom = p;
        """
        cursor.execute(query)
        result= cursor.fetchall()
        return result
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
def creer_fonction_moyenne_generale_sur_periode():
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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
                        
def recuperer_id_joueur(nom, prenom):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        SELECT id_joueur FROM joueur WHERE nom = %s AND prenom = %s;
        """
        cursor.execute(query, (nom, prenom))
        result = cursor.fetchone()
        if not result:
            raise utils.joueur_non_existant()
            
    except utils.joueur_non_existant as e:
        print(f"Joueur non trouvé: {e}")
        if db.is_connected():
            cursor.close()
            db.close()
        
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de l'id du joueur: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    return result[0] if result else None
        
def recuperer_dates(Match):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        SELECT date_match FROM match WHERE adversaire = %s;"""
        cursor.execute(query, (utils.clean_string(Match),))
        result = cursor.fetchall()
        dates = [row[0] for row in result]
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération des dates: {e}")
    finally:    
        if 'db' in locals():
            cursor.close()
            db.close()
    return dates if dates else None
      
def recuperer_id_match(Match,date_match):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
        cursor = db.cursor()
        query = """
        SELECT id_match FROM match WHERE adversaire = %s AND date_match = %s;"""
        cursor.execute(query, (utils.clean_string(Match),date_match))
        result = cursor.fetchone()
    except pymysql.Error as e:
        print(f"Erreur lors de la récupération de l'id du match: {e}")
    finally:    
        if 'db' in locals():
            cursor.close()
            db.close()
    return result[0] if result else None
    



 
 
def selectionner_tous_les_joueurs():
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database"  # optional if you want to connect to specific db
        )
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
    
def selectionner_joueur_par_id(id_joueur):
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database" 
        )
        cursor = db.cursor()
        query = "SELECT * FROM joueur WHERE id = %s;"
        cursor.execute(query, (id_joueur,))
        joueur = cursor.fetchone()
        return joueur
    except pymysql.Error as err:
        print(f"Erreur lors de la sélection du joueur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()    
          
          
          
def selectionner_tous_les_matchs():
    try:
        db = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="LAGLEG123",
            database="my_database" 
        )
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
            
            
            
