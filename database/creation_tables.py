import pymysql



def create_connection():
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = pymysql.connect(
            host="localhost",       # or your host name/IP address
            user="root",          # your MySQL username
            password="2004",
            database="my_database_test"  # optional if you want to connect to specific db
        )
        if connection in locals():
            print("Connection to the database was successful.")
    except pymysql.Error as e:
        print(f"The error '{e}' occurred")
    return connection
# def creer_fonction_moyenne_generale_sur_periode():
#     try:
#         db = pymysql.connect(
#             host="localhost",       # or your host name/IP address
#             user="root",          # your MySQL username
#             password="2004",
#             database="my_database_test"  # optional if you want to connect to specific db
#         )
#         cursor = db.cursor()
#         query = """
#         CREATE FUNCTION moyenne_generale_sur_periode(id_evaluation_technique INT,
#                 id_evaluation_tactique INT, id_evaluation_comportementale INT)
#         RETURNS FLOAT
#         DETERMINISTIC
#         READS SQL DATA
        
#         BEGIN
        
#             RETURN (
#         (SELECT moyenne_technique FROM evaluation_technique WHERE id = id_evaluation_technique) +
#         (SELECT moyenne_tactique FROM evaluation_tactique WHERE id = id_evaluation_tactique) +
#         (SELECT moyenne_comportementale FROM evaluation_comportementale WHERE id = id_evaluation_comportementale)
#     ) / 3;
#         END;
#         """
#         cursor.execute(query)
#         db.commit()
#         print("Fonction créée avec succès!")
#     except pymysql.Error as e:
#         print(f"Erreur lors de la création de la fonction: {e}")
#     finally:
#         if 'db' in locals():
#             cursor.close()
#             db.close()
# def creer_fonction_moyenne_match():
#     try:
#         db = pymysql.connect(
#             host="localhost",       # or your host name/IP address
#             user="root",          # your MySQL username
#             password="2004",
#             database="my_database_test"  # optional if you want to connect to specific db
#         )
#         cursor = db.cursor()
#         query = """
#         CREATE FUNCTION moyenne_match(id_evaluation_technique INT,
#                 id_evaluation_tactique INT, id_evaluation_comportementale INT)
#         RETURNS FLOAT
#         DECLARE 
#             moyenne_technique FLOAT;
#             moyenne_tactique FLOAT;
#             moyenne_comportementale FLOAT;
#             moyenne_generale FLOAT;
        
#         BEGIN
        
#             SELECT evaluation_technique.moyenne_technique INTO moyenne_technique FROM evaluation_technique WHERE id_evaluation_technique = evaluation_technique.id_evaluation_technique;
            
#             SELECT evaluation_tactique.moyenne_tactique INTO moyenne_tactique FROM evaluation_tactique WHERE id_evaluation_tactique = evaluation_tactique.id_evaluation_tactique;
            
#             SELECT evaluation_comportementale.moyenne_comportementale INTO moyenne_comportementale FROM evaluation_comportementale WHERE id_evaluation_comportementale = evaluation_comportementale.id_evaluation_comportementale;
            
#             SET moyenne_generale = (moyenne_technique + moyenne_tactique + moyenne_comportementale) / 3;
            
#             RETURN moyenne;
#         END;
#         """
#         cursor.execute(query)
#         db.commit()
#         print("Fonction créée avec succès!")
#     except pymysql.Error as e:
#         print(f"Erreur lors de la création de la fonction: {e}")
#     finally:
#         if 'db' in locals():
#             cursor.close()
#             db.close()

def creer_table_joueur():
    try:
        db =create_connection()
        cursor = db.cursor()
        req_creation = """
        CREATE TABLE IF NOT EXISTS joueur (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            prenom VARCHAR(100) NOT NULL,
            categorie  ENUM('Junior', 'Senior') ,
            selection_nationale VARCHAR(50),
            poste_principal ENUM('Gardien', 'Défenseur', 'Milieu', 'Attaquant', 'Latéral', 'Pivot') NOT NULL DEFAULT 'Milieu',
                    
            pied_fort ENUM('Droit', 'Gauche', 'Ambidextre'),
            taille INT,
            poids DECIMAL(5,2),
            date_naissance DATE,
            

            -- Statistiques
            matchs_joues INT DEFAULT 0,
            titulaire INT DEFAULT 0,
            remplacant INT DEFAULT 0,
            tempsjeu INT DEFAULT 0,
            buts INT DEFAULT 0,
            assists INT DEFAULT 0,
            carton_jaune INT DEFAULT 0,
            carton_rouge INT DEFAULT 0,
            
            
             -- Gestion des blessures
            est_blesse BOOLEAN DEFAULT FALSE,
            type_blessure ENUM(
                'Musculaire', 
                'Articulaire', 
                'Fracture', 
                'Ligamentaire', 
                'Tendinite', 
                'Commotion', 
                'Autre'
            ),
            date_blessure DATE,
            date_retour_prevue DATE,
            severite_blessure ENUM('Légère', 'Modérée', 'Grave', 'Très grave'),
            description_blessure TEXT,
            
            
            -- Index
            INDEX idx_nom_prenom (nom, prenom),
            INDEX idx_categorie (categorie),
            INDEX idx_poste (poste_principal),
            INDEX idx_blesse (est_blesse)
        );
        """
        cursor.execute(req_creation)
        print("Table 'joueur' créée avec succès!")

        
    except pymysql.Error as err:
        print(f"Error: {err}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
                  
def creer_table_match():
    try:
        db =create_connection()
        
        cursor = db.cursor()
        
        req_creation = """
        CREATE TABLE IF NOT EXISTS matchs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date_match DATETIME NOT NULL,
            lieu VARCHAR(100) NOT NULL,
            adversaire VARCHAR(100) NOT NULL,
            type_match ENUM('Amical', 'Championnat', 'Coupe', 'Tournoi') NOT NULL,
            domicile BOOLEAN DEFAULT TRUE,
            score_equipe TINYINT UNSIGNED,
            score_adversaire TINYINT UNSIGNED,
            resultat ENUM('Victoire', 'Défaite', 'Nul') GENERATED ALWAYS AS (
                CASE 
                    WHEN score_equipe > score_adversaire THEN 'Victoire'
                    WHEN score_equipe < score_adversaire THEN 'Défaite'
                    ELSE 'Nul'
                END
            ) STORED,
            competion VARCHAR(100),
            saison VARCHAR(20) NOT NULL,
            temps_reglementaire TINYINT DEFAULT 90,
            prolongation BOOLEAN DEFAULT FALSE,
            penalties BOOLEAN DEFAULT FALSE,
            conditions_meteo ENUM('Bon', 'Pluie', 'Vent', 'Neige', 'Chaleur', 'Brouillard'),
            temperature TINYINT,
            public INT,
            arbitre_principal VARCHAR(100),
            arbitre_assistant_1 VARCHAR(100),
            arbitre_assistant_2 VARCHAR(100),
            commentaires TEXT,
            
            INDEX idx_date (date_match),
            INDEX idx_adversaire (adversaire),
            INDEX idx_saison (saison),
            INDEX idx_type (type_match)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'matchs' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_evaluation_technique(): 
    try:
        db =create_connection()
        
        cursor = db.cursor()
        
        
        req_creation = """
        CREATE TABLE IF NOT EXISTS evaluation_technique (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            evaluation_date DATE NOT NULL,
            
            qualite_premiere_touche TINYINT,
            qualite_passes TINYINT ,
            technique_defensive TINYINT,
            sens_tactique_vision TINYINT,
            vitesse_pensee TINYINT,
            anticipation TINYINT,
            adaptation_adversaire TINYINT,
            sens_replacement TINYINT,
            sens_demarquage TINYINT,
            sens_marquage TINYINT,
            technique_generale TINYINT,
            jeu_tete TINYINT,
            puissance_frappe TINYINT,
            drible_feinte TINYINT,
            technique_au_poste TINYINT,
            puissance_physique TINYINT,
            rapidite TINYINT,

            
            moyenne_technique DECIMAL(3,2),
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_player (id_joueur),
            INDEX idx_date (evaluation_date),
            UNIQUE KEY uk_joueur_date (id_joueur, evaluation_date)
        );
        """
        
        
        cursor.execute(req_creation)
        print("Table 'evaluation_technique' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Error: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_evaluation_tactique():
    try:
        db =create_connection()
        
        
        cursor = db.cursor()
        req_creation ="""
        CREATE TABLE IF NOT EXISTS evaluation_tactique (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            evaluation_date DATE NOT NULL,
            
            disponibilite TINYINT,
            intelligence_de_jeu TINYINT,
            jouer_vers_avant TINYINT,
            jouer_dos_adversaires TINYINT,
            changer_rythme TINYINT, 
            
            
            moyenne_tactique DECIMAL(3,2),
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_player (id_joueur),
            INDEX idx_date (evaluation_date),
            UNIQUE KEY uk_joueur_date (id_joueur, evaluation_date)
        );
        """
        cursor.execute(req_creation)
        print("Table 'evaluation_tactique' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Error: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_evaluation_comportementale():
    try:
        db =create_connection()
        
        
        cursor = db.cursor()
        req_creation ="""
        CREATE TABLE IF NOT EXISTS evaluation_comportementale (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            evaluation_date DATE NOT NULL,
            
            -- Tableau principal
            assiduite TINYINT,
            motivation_volonte TINYINT,
            confiance_prise_risque TINYINT,
            calme_maitrise_soi TINYINT,
            combativite TINYINT,
            sportivite TINYINT ,
            amabilite TINYINT,
            
            moyenne_comportementale DECIMAL(3,2),
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_player (id_joueur),
            INDEX idx_date (evaluation_date),
            UNIQUE KEY uk_joueur_date (id_joueur, evaluation_date)
            
        );
        """
        cursor.execute(req_creation)
        print("Table 'evaluation_comportementale' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Error: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_test_athletique():  
    try:
        db =create_connection()
        
        cursor = db.cursor()
        
        req_creation = """
        CREATE TABLE IF NOT EXISTS test_athletique (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            categorie ENUM('Minimes A','Minimes B', 'Juniors', 'Cadets A', 'Cadets B', 'Seniors A', 'Seniors B') NOT NULL DEFAULT 'Juniors',
            date_test DATE NOT NULL,
            periode_test ENUM('Période 1', 'Période 2', 'Période 3', 'Période 4', 'Période 5') NOT NULL DEFAULT 'Période 1',
            
            -- Détente Horizontale
            detente_horizontale DECIMAL(5,2) COMMENT 'en mètres',
            
            -- Détente Verticale
            detente_verticale DECIMAL(5,2) COMMENT 'en cm',
            
            -- Vitesse
            vitesse_thalf_test DECIMAL(4,2) COMMENT 'En secondes',
            vitesse_10m DECIMAL(4,2) COMMENT 'En secondes',
            vitesse_20m DECIMAL(4,2) COMMENT 'En secondes',
            vitesse_30m DECIMAL(4,2) COMMENT 'En secondes',
            
            -- Aérobie
            aerobie_vameval_vo2max DECIMAL(5,2),
            vma_kmh DECIMAL(4,2) COMMENT 'Vitesse Maximale Aérobie en km/h',
            vma_ms DECIMAL(4,2) COMMENT 'Vitesse Maximale Aérobie en m/s',
            yoyo_pal INT COMMENT 'Palier YOYO atteint',
            
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_joueur (id_joueur),
            INDEX idx_date (date_test),
            INDEX idx_periode (periode_test),
            UNIQUE KEY uk_joueur_date (id_joueur, date_test),
            UNIQUE KEY uk_joueur_periode (id_joueur, periode_test)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'tests_athletiques' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_test_morphologique():
    try:
        db =create_connection()
        
        cursor = db.cursor()
        
        req_creation = """
        CREATE TABLE IF NOT EXISTS test_morphologique (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            date_test DATE NOT NULL,
            periode_test ENUM('Période 1', 'Période 2', 'Période 3', 'Période 4', 'Période 5') NOT NULL DEFAULT 'Période 1',
            
            
            -- Mesures de base
            poids DECIMAL(5,2) COMMENT 'Poids en kg',
            taille INT COMMENT 'Taille en cm',
            
            -- Calculs
            imc DECIMAL(5,2) GENERATED ALWAYS AS (poids / ((taille/100) * (taille/100))) STORED COMMENT 'Indice de Masse Corporelle',
            masse_grasse DECIMAL(5,2) COMMENT 'Pourcentage de masse grasse',
            
            -- Classification
            classification_imc VARCHAR(50) GENERATED ALWAYS AS (
                CASE 
                    WHEN poids / ((taille/100) * (taille/100)) < 18.5 THEN 'Maigreur'
                    WHEN poids / ((taille/100) * (taille/100)) < 25 THEN 'Normal'
                    WHEN poids / ((taille/100) * (taille/100)) < 30 THEN 'Surpoids'
                    ELSE 'Obésité'
                END
            ) STORED,
            
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_joueur (id_joueur),
            INDEX idx_date (date_test),
            INDEX idx_periode (periode_test),
            UNIQUE KEY uk_joueur_date (id_joueur, date_test),
            UNIQUE KEY uk_joueur_periode (id_joueur, periode_test)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'tests_morphologiques' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_test_medical():
    try:
        db =create_connection()
        
        cursor = db.cursor()
        
        req_creation = """
        CREATE TABLE IF NOT EXISTS test_medical (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            categorie ENUM('Minimes A','Minimes B', 'Juniors', 'Cadets A', 'Cadets B', 'Seniors A', 'Seniors B') NOT NULL DEFAULT 'Juniors',
            
            date_test DATE NOT NULL,
            periode_test ENUM('Période 1', 'Période 2', 'Période 3', 'Période 4', 'Période 5') NOT NULL DEFAULT 'Période 1',
            
            
            -- Examen Morphologique
            taille INT COMMENT 'Taille en cm',
            poids DECIMAL(5,2) COMMENT 'Poids en kg',
            masse_grasse DECIMAL(5,2) COMMENT 'Masse grasse en %',
            
            -- Examens médicaux
            examen_general TINYINT,
            examen_orthopedique TINYINT,
            examen_dentaire TINYINT,
            examen_orl TINYINT,
            examen_dermatologique TINYINT,
            examen_psychologique TINYINT,
            
            
            -- Commentaires généraux
            commentaires TEXT,
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_joueur (id_joueur),
            INDEX idx_date (date_test),
            INDEX idx_periode (periode_test),
            INDEX idx_categorie (categorie),
            UNIQUE KEY uk_joueur_date (id_joueur, date_test),
            UNIQUE KEY uk_joueur_periode (id_joueur, periode_test)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'test_medical' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_suivi_nutritionnel():
    try:
        db =create_connection()
        
        cursor = db.cursor()
        
        req_creation = """
        CREATE TABLE IF NOT EXISTS suivi_nutritionnel (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            groupe VARCHAR(50) NOT NULL,
            date_creation DATE NOT NULL,
            periode_test ENUM('Période 1', 'Période 2', 'Période 3', 'Période 4', 'Période 5') NOT NULL DEFAULT 'Période 1',
            
            
            
            -- Données de base
            age TINYINT UNSIGNED,
            poids_depart DECIMAL(5,2) COMMENT 'Poids initial en kg',
            taille DECIMAL(3,2) COMMENT 'Taille en mètres',
            imc DECIMAL(5,2) GENERATED ALWAYS AS (poids_depart/(taille*taille)) STORED,
            
            -- Objectifs
            objectif ENUM('Perte poids', 'Prise masse', 'Maintien', 'Optimisation performance', 'Récomposition corporelle') NOT NULL DEFAULT 'Perte poids',
            details_objectif TEXT COMMENT "Détails de l'objectif",
            
            -- Suivi nutritionnel
            regime_specifique TEXT COMMENT 'Détails du régime',
            date_premier_suivi DATE,
            date_deuxieme_suivi DATE,
            date_troisieme_suivi DATE,
            
            -- Évaluations
            eval_premier_suivi TEXT,
            eval_deuxieme_suivi TEXT,
            eval_troisieme_suivi TEXT,
            
            -- Résultats
            poids_actuel DECIMAL(5,2),
            evolution_poids DECIMAL(5,2) GENERATED ALWAYS AS (poids_actuel - poids_depart) STORED,
            satisfaction TINYINT COMMENT 'Note de satisfaction 1-5',
            
            -- Commentaires
            commentaires TEXT,
            
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            INDEX idx_joueur (id_joueur),
            INDEX idx_groupe (groupe),
            INDEX idx_objectif (objectif),
            INDEX idx_date_creation (date_creation),
            INDEX idx_periode (periode_test),
            UNIQUE KEY uk_joueur_date (id_joueur, date_creation),
            UNIQUE KEY uk_joueur_periode (id_joueur, periode_test)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'suivi_nutritionnel' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_suivi_psychologique():
    pass

def creer_table_test_physique():
    pass

def creer_table_evaluation_sur_periode(): 
    try:
        db =create_connection()
        
        cursor = db.cursor()
        req_creation = """
        CREATE TABLE IF NOT EXISTS evaluation_sur_periode (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_joueur INT NOT NULL,
            periode_test ENUM('Période 1', 'Période 2', 'Période 3', 'Période 4', 'Période 5') NOT NULL DEFAULT 'Période 1',
            evaluation_date DATE NOT NULL,
            
            
            -- IDs des évaluations spécifiques
            id_evaluation_technique INT,
            id_evaluation_tactique INT,
            id_evaluation_comportementale INT,
            id_test_athletique INT,
            id_test_morphologique INT,
            id_test_medical INT,
            id_suivi_nutritionnel INT,

            
            
            -- Moyenne
            moyenne_generale DECIMAL(3,2),
            
            -- Contraintes et index
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            FOREIGN KEY (id_evaluation_technique) REFERENCES evaluation_technique(id),
            FOREIGN KEY (id_evaluation_tactique) REFERENCES evaluation_tactique(id),
            FOREIGN KEY (id_evaluation_comportementale) REFERENCES evaluation_comportementale(id),
            FOREIGN KEY (id_test_athletique) REFERENCES test_athletique(id),
            FOREIGN KEY (id_test_morphologique) REFERENCES test_morphologique(id),
            FOREIGN KEY (id_test_medical) REFERENCES test_medical(id),
            FOREIGN KEY (id_suivi_nutritionnel) REFERENCES suivi_nutritionnel(id),


        
            INDEX idx_joueur (id_joueur),
            INDEX idx_periode (periode_test),
            UNIQUE KEY uk_joueur_date (id_joueur, evaluation_date),
            UNIQUE KEY uk_joueur_periode (id_joueur, periode_test)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'evaluation_sur_periode' créée avec succès!")
        
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def creer_table_evaluation_sur_match():
    try:
        db =create_connection()
        
        cursor = db.cursor()
        

        
        req_creation = """
        CREATE TABLE IF NOT EXISTS evaluation_sur_match (
            id_joueur INT NOT NULL,
            id_match INT NOT NULL,
            
            -- IDs des évaluations spécifiques
            id_evaluation_technique INT,
            id_evaluation_tactique INT,
            id_evaluation_comportementale INT,
            
            -- Moyenne
            moyenne_generale DECIMAL(3,2),
            
            -- Contraintes et index
            FOREIGN KEY (id_joueur) REFERENCES joueur(id),
            FOREIGN KEY (id_evaluation_tactique) REFERENCES evaluation_tactique(id),
            FOREIGN KEY (id_evaluation_comportementale) REFERENCES evaluation_comportementale(id),
            FOREIGN KEY (id_evaluation_technique) REFERENCES evaluation_technique(id),
            FOREIGN KEY (id_match) REFERENCES matchs(id),
            
            INDEX idx_joueur (id_joueur),
            INDEX idx_match (id_match)
        );
        """
        
        cursor.execute(req_creation)
        print("Table 'evaluation_sur_match' créée avec succès!")          
              
    except pymysql.Error as err:
        print(f"Erreur: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
    









# test de l'insertion
def inserer_15_joueurs():
    try:
        db = create_connection()
        cursor = db.cursor()

        joueurs = [
            ("Dupont", "Jean", "Senior", "France", "Milieu", "Droit", 180, 75.5, "1990-05-15", 50, 40, 10, 3600, 15, 10, 2, 0, False, None, None, None, None, None),
            ("Martin", "Paul", "Junior", "France", "Défenseur", "Gauche", 185, 80.0, "2002-03-10", 30, 25, 5, 2700, 5, 3, 1, 0, False, None, None, None, None, None),
            ("Durand", "Luc", "Senior", "France", "Attaquant", "Droit", 175, 70.0, "1995-07-20", 60, 50, 10, 4000, 25, 12, 3, 1, False, None, None, None, None, None),
            ("Petit", "Marie", "Junior", "France", "Gardien", "Ambidextre", 190, 85.0, "2004-11-05", 20, 18, 2, 1800, 0, 0, 0, 0, False, None, None, None, None, None),
            ("Bernard", "Sophie", "Senior", "France", "Latéral", "Gauche", 165, 60.0, "1992-02-25", 40, 35, 5, 3200, 8, 6, 2, 0, False, None, None, None, None, None),
            ("Morel", "Julien", "Junior", "France", "Pivot", "Droit", 195, 90.0, "2003-06-15", 25, 20, 5, 2000, 10, 8, 1, 0, False, None, None, None, None, None),
            ("Simon", "Claire", "Senior", "France", "Milieu", "Gauche", 170, 65.0, "1991-09-30", 55, 45, 10, 3500, 12, 9, 3, 1, False, None, None, None, None, None),
            ("Lemoine", "Hugo", "Junior", "France", "Défenseur", "Droit", 180, 75.0, "2005-01-12", 15, 12, 3, 1200, 3, 2, 0, 0, False, None, None, None, None, None),
            ("Roux", "Emma", "Senior", "France", "Attaquant", "Ambidextre", 175, 68.0, "1993-04-18", 65, 55, 10, 4200, 30, 15, 4, 1, False, None, None, None, None, None),
            ("Blanc", "Lucas", "Junior", "France", "Gardien", "Droit", 185, 82.0, "2001-08-22", 18, 15, 3, 1500, 0, 0, 0, 0, False, None, None, None, None, None),
            ("Fontaine", "Alice", "Senior", "France", "Latéral", "Gauche", 160, 55.0, "1994-12-10", 45, 40, 5, 3000, 6, 4, 1, 0, False, None, None, None, None, None),
            ("Chevalier", "Thomas", "Junior", "France", "Pivot", "Droit", 200, 95.0, "2006-03-05", 10, 8, 2, 800, 5, 3, 0, 0, False, None, None, None, None, None),
            ("Garnier", "Julie", "Senior", "France", "Milieu", "Gauche", 175, 62.0, "1997-05-25", 50, 45, 5, 3600, 18, 12, 2, 0, False, None, None, None, None, None),
            ("Lambert", "Antoine", "Junior", "France", "Défenseur", "Droit", 180, 78.0, "2000-10-10", 35, 30, 5, 2500, 7, 5, 1, 0, False, None, None, None, None, None),
            ("Girard", "Camille", "Senior", "France", "Attaquant", "Ambidextre", 170, 63.0, "1996-07-07", 70, 60, 10, 4500, 35, 20, 5, 2, False, None, None, None, None, None)
        ]

        query = """
        INSERT INTO joueur (nom, prenom, categorie, selection_nationale, poste_principal, pied_fort, taille, poids, date_naissance,
        matchs_joues, titulaire, remplacant, tempsjeu, buts, assists, carton_jaune, carton_rouge, est_blesse, type_blessure,
        date_blessure, date_retour_prevue, severite_blessure, description_blessure)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        cursor.executemany(query, joueurs)
        db.commit()
        print("15 joueurs insérés avec succès!")
    except pymysql.Error as err:
        print(f"Erreur lors de l'insertion des joueurs: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
def inserer_sur_periodes_evaluations_pour_joueurs():
    try:
        db = create_connection()
        cursor = db.cursor()

        # Fetch all player IDs
        cursor.execute("SELECT id FROM joueur")
        joueurs = cursor.fetchall()

        # Define periods
        periodes = ["Période 1", "Période 2", "Période 3", "Période 4", "Période 5"]

        for joueur in joueurs:
            joueur_id = joueur[0]

            for i, periode in enumerate(periodes):
                # Generate a unique evaluation date for each period
                evaluation_date = f"2025-04-{4 + i}"  # Example: 2025-04-04, 2025-04-05, etc.

                # Insert technical evaluation
                query_technique = """
                INSERT INTO evaluation_technique (id_joueur, evaluation_date, qualite_premiere_touche, qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee, anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte, technique_au_poste, puissance_physique, rapidite, moyenne_technique)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_technique, (joueur_id, evaluation_date, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 3.5))
                id_technique = cursor.lastrowid

                # Insert tactical evaluation
                query_tactique = """
                INSERT INTO evaluation_tactique (id_joueur, evaluation_date, disponibilite, intelligence_de_jeu, jouer_vers_avant, jouer_dos_adversaires, changer_rythme, moyenne_tactique)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_tactique, (joueur_id, evaluation_date, 4, 3, 4, 3, 4, 3.6))
                id_tactique = cursor.lastrowid

                # Insert behavioral evaluation
                query_comportementale = """
                INSERT INTO evaluation_comportementale (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_comportementale, (joueur_id, evaluation_date, 4, 4, 3, 4, 3, 4, 3, 3.6))
                id_comportementale = cursor.lastrowid

                # Insert athletic test
                query_athletique = """
                INSERT INTO test_athletique (id_joueur, categorie, date_test, periode_test, detente_horizontale, detente_verticale, vitesse_thalf_test, vitesse_10m, vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_athletique, (joueur_id, "Juniors", evaluation_date, periode, 2.5, 50, 12.5, 1.8, 3.5, 5.0, 60.0, 15.0, 4.2, 15))

                # Insert morphological test
                query_morphologique = """
                INSERT INTO test_morphologique (id_joueur, date_test, periode_test, poids, taille, masse_grasse)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_morphologique, (joueur_id, evaluation_date, periode, 75.5, 180, 15.0))

                # Insert medical test
                query_medical = """
                INSERT INTO test_medical (id_joueur, categorie, date_test, periode_test, taille, poids, masse_grasse, examen_general, examen_orthopedique, examen_dentaire, examen_orl, examen_dermatologique, examen_psychologique, commentaires)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_medical, (joueur_id, "Juniors", evaluation_date, periode, 180, 75.5, 15.0, 4, 4, 3, 4, 3, 4, "RAS"))

                # Insert nutritional follow-up
                query_nutritionnel = """
                INSERT INTO suivi_nutritionnel (id_joueur, groupe, date_creation, periode_test, age, poids_depart, taille, objectif, details_objectif, regime_specifique, poids_actuel, satisfaction, commentaires)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_nutritionnel, (joueur_id, "Groupe 1", evaluation_date, periode, 25, 75.5, 1.80, "Maintien", "Maintenir le poids", "Régime équilibré", 75.5, 5, "RAS"))

                # Insert evaluation for the period
                query_evaluation_periode = """
                INSERT INTO evaluation_sur_periode (id_joueur, periode_test, evaluation_date, id_evaluation_technique, id_evaluation_tactique, id_evaluation_comportementale, moyenne_generale)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                moyenne_generale = (3.5 + 3.6 + 3.6) / 3
                cursor.execute(query_evaluation_periode, (joueur_id, periode, evaluation_date, id_technique, id_tactique, id_comportementale, moyenne_generale))

        db.commit()
        print("Évaluations insérées avec succès pour tous les joueurs!")
    except pymysql.Error as err:
        print(f"Erreur lors de l'insertion des évaluations: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()
            
def inserer_evaluations_par_match_pour_joueurs():
    try:
        db = create_connection()
        cursor = db.cursor()

        # Fetch all player IDs
        cursor.execute("SELECT id FROM joueur")
        joueurs = cursor.fetchall()

        # Fetch all match IDs
        cursor.execute("SELECT id FROM matchs")
        matchs = cursor.fetchall()

        for joueur in joueurs:
            joueur_id = joueur[0]

            for i, match in enumerate(matchs[:10]):  # Limit to 10 matches per player
                match_id = match[0]

                # Generate a unique evaluation date for each match
                evaluation_date = f"2025-05-{4 + i}"  # Example: 2025-04-04, 2025-04-05, etc.

                # Insert technical evaluation
                query_technique = """
                INSERT INTO evaluation_technique (id_joueur, evaluation_date, qualite_premiere_touche, qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee, anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte, technique_au_poste, puissance_physique, rapidite, moyenne_technique)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_technique, (joueur_id, evaluation_date, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 3.5))
                id_technique = cursor.lastrowid

                # Insert tactical evaluation
                query_tactique = """
                INSERT INTO evaluation_tactique (id_joueur, evaluation_date, disponibilite, intelligence_de_jeu, jouer_vers_avant, jouer_dos_adversaires, changer_rythme, moyenne_tactique)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_tactique, (joueur_id, evaluation_date, 4, 3, 4, 3, 4, 3.6))
                id_tactique = cursor.lastrowid

                # Insert behavioral evaluation
                query_comportementale = """
                INSERT INTO evaluation_comportementale (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query_comportementale, (joueur_id, evaluation_date, 4, 4, 3, 4, 3, 4, 3, 3.6))
                id_comportementale = cursor.lastrowid

                # Insert evaluation for the match
                query_evaluation_match = """
                INSERT INTO evaluation_sur_match (id_joueur, id_match, id_evaluation_technique, id_evaluation_tactique, id_evaluation_comportementale, moyenne_generale)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                moyenne_generale = (3.5 + 3.6 + 3.6) / 3
                cursor.execute(query_evaluation_match, (joueur_id, match_id, id_technique, id_tactique, id_comportementale, moyenne_generale))

        db.commit()
        print("Évaluations par match insérées avec succès pour tous les joueurs!")
    except pymysql.Error as err:
        print(f"Erreur lors de l'insertion des évaluations par match: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()

def inserer_evaluation_sur_periode_pour_joueur_7():
    try:
        db = create_connection()
        cursor = db.cursor()

        joueur_id = 7
        periode = "Période 1"
        evaluation_date = "2025-06-04"

        # Insert technical evaluation
        query_technique = """
        INSERT INTO evaluation_technique (id_joueur, evaluation_date, qualite_premiere_touche, qualite_passes, technique_defensive, sens_tactique_vision, vitesse_pensee, anticipation, adaptation_adversaire, sens_replacement, sens_demarquage, sens_marquage, technique_generale, jeu_tete, puissance_frappe, drible_feinte, technique_au_poste, puissance_physique, rapidite, moyenne_technique)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_technique, (joueur_id, evaluation_date, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 3.5))
        id_technique = cursor.lastrowid

        # Insert tactical evaluation
        query_tactique = """
        INSERT INTO evaluation_tactique (id_joueur, evaluation_date, disponibilite, intelligence_de_jeu, jouer_vers_avant, jouer_dos_adversaires, changer_rythme, moyenne_tactique)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_tactique, (joueur_id, evaluation_date, 4, 3, 4, 3, 4, 3.6))
        id_tactique = cursor.lastrowid

        # Insert behavioral evaluation
        query_comportementale = """
        INSERT INTO evaluation_comportementale (id_joueur, evaluation_date, assiduite, motivation_volonte, confiance_prise_risque, calme_maitrise_soi, combativite, sportivite, amabilite, moyenne_comportementale)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_comportementale, (joueur_id, evaluation_date, 4, 4, 3, 4, 3, 4, 3, 3.6))
        id_comportementale = cursor.lastrowid

        # Insert athletic test
        query_athletique = """
        INSERT INTO test_athletique (id_joueur, categorie, date_test, periode_test, detente_horizontale, detente_verticale, vitesse_thalf_test, vitesse_10m, vitesse_20m, vitesse_30m, aerobie_vameval_vo2max, vma_kmh, vma_ms, yoyo_pal)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_athletique, (joueur_id, "Juniors", evaluation_date, periode, 2.5, 50, 12.5, 1.8, 3.5, 5.0, 60.0, 15.0, 4.2, 15))
        id_athletique = cursor.lastrowid

        # Insert morphological test
        query_morphologique = """
        INSERT INTO test_morphologique (id_joueur, date_test, periode_test, poids, taille, masse_grasse)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_morphologique, (joueur_id, evaluation_date, periode, 75.5, 180, 15.0))
        id_morphologique = cursor.lastrowid

        # Insert medical test
        query_medical = """
        INSERT INTO test_medical (id_joueur, categorie, date_test, periode_test, taille, poids, masse_grasse, examen_general, examen_orthopedique, examen_dentaire, examen_orl, examen_dermatologique, examen_psychologique, commentaires)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_medical, (joueur_id, "Juniors", evaluation_date, periode, 180, 75.5, 15.0, 4, 4, 3, 4, 3, 4, "RAS"))
        id_medical = cursor.lastrowid

        # Insert nutritional follow-up
        query_nutritionnel = """
        INSERT INTO suivi_nutritionnel (id_joueur, groupe, date_creation, periode_test, age, poids_depart, taille, objectif, details_objectif, regime_specifique, poids_actuel, satisfaction, commentaires)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_nutritionnel, (joueur_id, "Groupe 1", evaluation_date, periode, 25, 75.5, 1.80, "Maintien", "Maintenir le poids", "Régime équilibré", 75.5, 5, "RAS"))
        id_nutritionnel = cursor.lastrowid

        # Insert evaluation for the period
        query_evaluation_periode = """
        INSERT INTO evaluation_sur_periode (id_joueur, periode_test, evaluation_date, id_evaluation_technique, id_evaluation_tactique, id_evaluation_comportementale, id_test_athletique, id_test_morphologique, id_test_medical, id_suivi_nutritionnel, moyenne_generale)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        moyenne_generale = (3.5 + 3.6 + 3.6) / 3
        cursor.execute(query_evaluation_periode, (joueur_id, periode, evaluation_date, id_technique, id_tactique, id_comportementale, id_athletique, id_morphologique, id_medical, id_nutritionnel, moyenne_generale))

        db.commit()
        print("Évaluation sur période insérée avec succès pour le joueur d'ID 7!")
    except pymysql.Error as err:
        print(f"Erreur lors de l'insertion de l'évaluation sur période: {err}")
    finally:
        if 'db' in locals():
            cursor.close()
            db.close()





create_connection()

# creer_table_joueur()
# creer_table_match()
# creer_table_evaluation_technique()
# creer_table_evaluation_tactique()
# creer_table_evaluation_comportementale()
# creer_table_test_athletique()
# creer_table_test_morphologique()
# creer_table_test_medical()
# creer_table_suivi_nutritionnel()
# creer_table_suivi_psychologique()
# creer_table_test_physique()
# creer_table_evaluation_sur_periode()
# creer_table_evaluation_sur_match()

# inserer_15_joueurs()
# inserer_sur_periodes_evaluations_pour_joueurs()
# inserer_evaluations_par_match_pour_joueurs()
inserer_evaluation_sur_periode_pour_joueur_7()
