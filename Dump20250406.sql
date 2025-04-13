-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: my_database
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `evaluation_comportementale`
--

DROP TABLE IF EXISTS `evaluation_comportementale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation_comportementale` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `evaluation_date` date NOT NULL,
  `assiduite` tinyint DEFAULT NULL,
  `motivation_volonte` tinyint DEFAULT NULL,
  `confiance_prise_risque` tinyint DEFAULT NULL,
  `calme_maitrise_soi` tinyint DEFAULT NULL,
  `combativite` tinyint DEFAULT NULL,
  `sportivite` tinyint DEFAULT NULL,
  `amabilite` tinyint DEFAULT NULL,
  `moyenne_comportementale` decimal(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`evaluation_date`),
  KEY `idx_player` (`id_joueur`),
  KEY `idx_date` (`evaluation_date`),
  CONSTRAINT `evaluation_comportementale_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_comportementale`
--

LOCK TABLES `evaluation_comportementale` WRITE;
/*!40000 ALTER TABLE `evaluation_comportementale` DISABLE KEYS */;
INSERT INTO `evaluation_comportementale` VALUES (1,7,'2025-06-04',4,4,3,4,3,4,3,3.60);
/*!40000 ALTER TABLE `evaluation_comportementale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `evaluation_generale`
--

DROP TABLE IF EXISTS `evaluation_generale`;
/*!50001 DROP VIEW IF EXISTS `evaluation_generale`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `evaluation_generale` AS SELECT 
 1 AS `TYPE`,
 1 AS `Date`,
 1 AS `moyenne_technique`,
 1 AS `moyenne_tactique`,
 1 AS `moyenne_comportementale`,
 1 AS `moyenne_generale`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `evaluation_sur_match`
--

DROP TABLE IF EXISTS `evaluation_sur_match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation_sur_match` (
  `id_joueur` int NOT NULL,
  `id_match` int NOT NULL,
  `id_evaluation_technique` int DEFAULT NULL,
  `id_evaluation_tactique` int DEFAULT NULL,
  `id_evaluation_comportementale` int DEFAULT NULL,
  `moyenne_generale` decimal(3,2) DEFAULT NULL,
  KEY `id_evaluation_tactique` (`id_evaluation_tactique`),
  KEY `id_evaluation_comportementale` (`id_evaluation_comportementale`),
  KEY `id_evaluation_technique` (`id_evaluation_technique`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_match` (`id_match`),
  CONSTRAINT `evaluation_sur_match_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`),
  CONSTRAINT `evaluation_sur_match_ibfk_2` FOREIGN KEY (`id_evaluation_tactique`) REFERENCES `evaluation_tactique` (`id`),
  CONSTRAINT `evaluation_sur_match_ibfk_3` FOREIGN KEY (`id_evaluation_comportementale`) REFERENCES `evaluation_comportementale` (`id`),
  CONSTRAINT `evaluation_sur_match_ibfk_4` FOREIGN KEY (`id_evaluation_technique`) REFERENCES `evaluation_technique` (`id`),
  CONSTRAINT `evaluation_sur_match_ibfk_5` FOREIGN KEY (`id_match`) REFERENCES `matchs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_sur_match`
--

LOCK TABLES `evaluation_sur_match` WRITE;
/*!40000 ALTER TABLE `evaluation_sur_match` DISABLE KEYS */;
/*!40000 ALTER TABLE `evaluation_sur_match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_sur_periode`
--

DROP TABLE IF EXISTS `evaluation_sur_periode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation_sur_periode` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `evaluation_date` date NOT NULL,
  `id_evaluation_technique` int DEFAULT NULL,
  `id_evaluation_tactique` int DEFAULT NULL,
  `id_evaluation_comportementale` int DEFAULT NULL,
  `id_test_athletique` int DEFAULT NULL,
  `id_test_morphologique` int DEFAULT NULL,
  `id_test_medical` int DEFAULT NULL,
  `id_suivi_nutritionnel` int DEFAULT NULL,
  `moyenne_generale` decimal(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`evaluation_date`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `id_evaluation_technique` (`id_evaluation_technique`),
  KEY `id_evaluation_tactique` (`id_evaluation_tactique`),
  KEY `id_evaluation_comportementale` (`id_evaluation_comportementale`),
  KEY `id_test_athletique` (`id_test_athletique`),
  KEY `id_test_morphologique` (`id_test_morphologique`),
  KEY `id_test_medical` (`id_test_medical`),
  KEY `id_suivi_nutritionnel` (`id_suivi_nutritionnel`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_periode` (`periode_test`),
  CONSTRAINT `evaluation_sur_periode_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_2` FOREIGN KEY (`id_evaluation_technique`) REFERENCES `evaluation_technique` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_3` FOREIGN KEY (`id_evaluation_tactique`) REFERENCES `evaluation_tactique` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_4` FOREIGN KEY (`id_evaluation_comportementale`) REFERENCES `evaluation_comportementale` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_5` FOREIGN KEY (`id_test_athletique`) REFERENCES `test_athletique` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_6` FOREIGN KEY (`id_test_morphologique`) REFERENCES `test_morphologique` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_7` FOREIGN KEY (`id_test_medical`) REFERENCES `test_medical` (`id`),
  CONSTRAINT `evaluation_sur_periode_ibfk_8` FOREIGN KEY (`id_suivi_nutritionnel`) REFERENCES `suivi_nutritionnel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_sur_periode`
--

LOCK TABLES `evaluation_sur_periode` WRITE;
/*!40000 ALTER TABLE `evaluation_sur_periode` DISABLE KEYS */;
INSERT INTO `evaluation_sur_periode` VALUES (1,7,'Période 1','2025-06-04',6,1,1,1,1,1,1,3.57);
/*!40000 ALTER TABLE `evaluation_sur_periode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_tactique`
--

DROP TABLE IF EXISTS `evaluation_tactique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation_tactique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `evaluation_date` date NOT NULL,
  `disponibilite` tinyint DEFAULT NULL,
  `intelligence_de_jeu` tinyint DEFAULT NULL,
  `jouer_vers_avant` tinyint DEFAULT NULL,
  `jouer_dos_adversaires` tinyint DEFAULT NULL,
  `changer_rythme` tinyint DEFAULT NULL,
  `moyenne_tactique` decimal(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`evaluation_date`),
  KEY `idx_player` (`id_joueur`),
  KEY `idx_date` (`evaluation_date`),
  CONSTRAINT `evaluation_tactique_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_tactique`
--

LOCK TABLES `evaluation_tactique` WRITE;
/*!40000 ALTER TABLE `evaluation_tactique` DISABLE KEYS */;
INSERT INTO `evaluation_tactique` VALUES (1,7,'2025-06-04',4,3,4,3,4,3.60);
/*!40000 ALTER TABLE `evaluation_tactique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_technique`
--

DROP TABLE IF EXISTS `evaluation_technique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation_technique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `evaluation_date` date NOT NULL,
  `qualite_premiere_touche` tinyint DEFAULT NULL,
  `qualite_passes` tinyint DEFAULT NULL,
  `technique_defensive` tinyint DEFAULT NULL,
  `sens_tactique_vision` tinyint DEFAULT NULL,
  `vitesse_pensee` tinyint DEFAULT NULL,
  `anticipation` tinyint DEFAULT NULL,
  `adaptation_adversaire` tinyint DEFAULT NULL,
  `sens_replacement` tinyint DEFAULT NULL,
  `sens_demarquage` tinyint DEFAULT NULL,
  `sens_marquage` tinyint DEFAULT NULL,
  `technique_generale` tinyint DEFAULT NULL,
  `jeu_tete` tinyint DEFAULT NULL,
  `puissance_frappe` tinyint DEFAULT NULL,
  `drible_feinte` tinyint DEFAULT NULL,
  `technique_au_poste` tinyint DEFAULT NULL,
  `puissance_physique` tinyint DEFAULT NULL,
  `rapidite` tinyint DEFAULT NULL,
  `moyenne_technique` decimal(3,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`evaluation_date`),
  KEY `idx_player` (`id_joueur`),
  KEY `idx_date` (`evaluation_date`),
  CONSTRAINT `evaluation_technique_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_technique`
--

LOCK TABLES `evaluation_technique` WRITE;
/*!40000 ALTER TABLE `evaluation_technique` DISABLE KEYS */;
INSERT INTO `evaluation_technique` VALUES (6,7,'2025-06-04',3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3.50);
/*!40000 ALTER TABLE `evaluation_technique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joueur` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_prenom` varchar(50) NOT NULL,
  `nationalities` varchar(20) NOT NULL,
  `categorie` enum('Ecole B','Ecole A','Minimes B','Minimes A','Cadets B','Cadets A','Juniors B','Juniors A','Seniors B','Seniors A') NOT NULL,
  `poste_principal` enum('Gardien','Arrière droit','Défenseur central droit','Défenseur central gauche','Arrière gauche','Milieu défensif','Milieu central','Milieu offensif','Ailier droit','Ailier gauche','Attaquant') NOT NULL,
  `pied_fort` enum('Droit','Gauche','Ambidextre') DEFAULT NULL,
  `taille` int DEFAULT NULL,
  `poids` decimal(5,2) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `matchs_joues` int DEFAULT '0',
  `titulaire` int DEFAULT '0',
  `remplacant` int DEFAULT '0',
  `tempsjeu` int DEFAULT '0',
  `buts` int DEFAULT '0',
  `assists` int DEFAULT '0',
  `carton_jaune` int DEFAULT '0',
  `carton_rouge` int DEFAULT '0',
  `est_blesse` enum('Oui','Non') DEFAULT 'Non',
  `type_blessure` enum('Musculaire','Articulaire','Fracture','Ligamentaire','Tendinite','Commotion','Autre') DEFAULT NULL,
  `date_blessure` date DEFAULT NULL,
  `date_retour_prevue` date DEFAULT NULL,
  `severite_blessure` enum('Légère','Modérée','Grave','Très grave') DEFAULT NULL,
  `description_blessure` text,
  PRIMARY KEY (`id`),
  KEY `idx_nom_prenom` (`nom_prenom`),
  KEY `idx_categorie` (`categorie`),
  KEY `idx_poste` (`poste_principal`),
  KEY `idx_blesse` (`est_blesse`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueur`
--

LOCK TABLES `joueur` WRITE;
/*!40000 ALTER TABLE `joueur` DISABLE KEYS */;
INSERT INTO `joueur` VALUES (1,'Dupont Jean','France','Seniors A','Milieu central','Droit',180,75.50,'1990-05-15',50,40,10,3600,15,10,2,0,'Non',NULL,NULL,NULL,NULL,NULL),(2,'Martin Paul','France','Juniors B','Défenseur central droit','Gauche',185,80.00,'2002-03-10',30,25,5,2700,5,3,1,0,'Non',NULL,NULL,NULL,NULL,NULL),(3,'Durand Luc','France','Seniors A','Attaquant','Droit',175,70.00,'1995-07-20',60,50,10,4000,25,12,3,1,'Non',NULL,NULL,NULL,NULL,NULL),(4,'Petit Marie','France','Juniors A','Gardien','Ambidextre',190,85.00,'2004-11-05',20,18,2,1800,0,0,0,0,'Non',NULL,NULL,NULL,NULL,NULL),(5,'Bernard Sophie','France','Seniors A','Arrière gauche','Gauche',165,60.00,'1992-02-25',40,35,5,3200,8,6,2,0,'Non',NULL,NULL,NULL,NULL,NULL),(6,'Morel Julien','France','Juniors A','Milieu défensif','Droit',195,90.00,'2003-06-15',25,20,5,2000,10,8,1,0,'Non',NULL,NULL,NULL,NULL,NULL),(7,'Simon Claire','France','Seniors B','Milieu central','Gauche',170,65.00,'1991-09-30',55,45,10,3500,12,9,3,1,'Non',NULL,NULL,NULL,NULL,NULL),(8,'Lemoine Hugo','France','Juniors A','Défenseur central gauche','Droit',180,75.00,'2005-01-12',15,12,3,1200,3,2,0,0,'Non',NULL,NULL,NULL,NULL,NULL),(9,'Roux Emma','France','Seniors A','Attaquant','Ambidextre',175,68.00,'1993-04-18',65,55,10,4200,30,15,4,1,'Non',NULL,NULL,NULL,NULL,NULL),(10,'Blanc Lucas','France','Juniors A','Gardien','Droit',185,82.00,'2001-08-22',18,15,3,1500,0,0,0,0,'Non',NULL,NULL,NULL,NULL,NULL),(11,'Fontaine Alice','France','Seniors B','Arrière gauche','Gauche',160,55.00,'1994-12-10',45,40,5,3000,6,4,1,0,'Non',NULL,NULL,NULL,NULL,NULL),(12,'Chevalier Thomas','France','Juniors B','Milieu offensif','Droit',200,95.00,'2006-03-05',10,8,2,800,5,3,0,0,'Non',NULL,NULL,NULL,NULL,NULL),(13,'Garnier Julie','France','Seniors A','Milieu central','Gauche',175,62.00,'1997-05-25',50,45,5,3600,18,12,2,0,'Non',NULL,NULL,NULL,NULL,NULL),(14,'Lambert Antoine','France','Juniors A','Défenseur central droit','Droit',180,78.00,'2000-10-10',35,30,5,2500,7,5,1,0,'Non',NULL,NULL,NULL,NULL,NULL),(15,'Girard Camille','France','Seniors A','Attaquant','Ambidextre',170,63.00,'1996-07-07',70,60,10,4500,35,20,5,2,'Non',NULL,NULL,NULL,NULL,NULL),(16,'Mahdi Mzari','Tunisie','Ecole B','Gardien','Droit',100,30.00,'2025-04-06',0,0,0,0,0,0,0,0,'Non',NULL,NULL,NULL,NULL,NULL),(17,'Rayen Lagleg','Tunisie','Ecole B','Gardien','Droit',100,30.00,'2025-04-06',0,0,0,0,0,0,0,0,'Non',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `joueur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matchs`
--

DROP TABLE IF EXISTS `matchs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matchs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_match` datetime NOT NULL,
  `lieu` varchar(100) NOT NULL,
  `adversaire` varchar(100) NOT NULL,
  `type_match` enum('Amical','Championnat','Coupe','Tournoi') NOT NULL,
  `domicile` tinyint(1) DEFAULT '1',
  `score_equipe` tinyint unsigned DEFAULT NULL,
  `score_adversaire` tinyint unsigned DEFAULT NULL,
  `resultat` enum('Victoire','Défaite','Nul') GENERATED ALWAYS AS ((case when (`score_equipe` > `score_adversaire`) then _utf8mb4'Victoire' when (`score_equipe` < `score_adversaire`) then _utf8mb4'Défaite' else _utf8mb4'Nul' end)) STORED,
  `competion` varchar(100) DEFAULT NULL,
  `saison` varchar(20) NOT NULL,
  `temps_reglementaire` tinyint DEFAULT '90',
  `prolongation` tinyint(1) DEFAULT '0',
  `penalties` tinyint(1) DEFAULT '0',
  `conditions_meteo` enum('Bon','Pluie','Vent','Neige','Chaleur','Brouillard') DEFAULT NULL,
  `temperature` tinyint DEFAULT NULL,
  `public` int DEFAULT NULL,
  `arbitre_principal` varchar(100) DEFAULT NULL,
  `arbitre_assistant_1` varchar(100) DEFAULT NULL,
  `arbitre_assistant_2` varchar(100) DEFAULT NULL,
  `commentaires` text,
  PRIMARY KEY (`id`),
  KEY `idx_date` (`date_match`),
  KEY `idx_adversaire` (`adversaire`),
  KEY `idx_saison` (`saison`),
  KEY `idx_type` (`type_match`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchs`
--

LOCK TABLES `matchs` WRITE;
/*!40000 ALTER TABLE `matchs` DISABLE KEYS */;
/*!40000 ALTER TABLE `matchs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suivi_nutritionnel`
--

DROP TABLE IF EXISTS `suivi_nutritionnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suivi_nutritionnel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `groupe` varchar(50) NOT NULL,
  `date_creation` date NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `age` tinyint unsigned DEFAULT NULL,
  `poids_depart` decimal(5,2) DEFAULT NULL COMMENT 'Poids initial en kg',
  `taille` decimal(3,2) DEFAULT NULL COMMENT 'Taille en mètres',
  `imc` decimal(5,2) GENERATED ALWAYS AS ((`poids_depart` / (`taille` * `taille`))) STORED,
  `objectif` enum('Perte poids','Prise masse','Maintien','Optimisation performance','Récomposition corporelle') NOT NULL DEFAULT 'Perte poids',
  `details_objectif` text COMMENT 'Détails de l''objectif',
  `regime_specifique` text COMMENT 'Détails du régime',
  `date_premier_suivi` date DEFAULT NULL,
  `date_deuxieme_suivi` date DEFAULT NULL,
  `date_troisieme_suivi` date DEFAULT NULL,
  `eval_premier_suivi` text,
  `eval_deuxieme_suivi` text,
  `eval_troisieme_suivi` text,
  `poids_actuel` decimal(5,2) DEFAULT NULL,
  `evolution_poids` decimal(5,2) GENERATED ALWAYS AS ((`poids_actuel` - `poids_depart`)) STORED,
  `satisfaction` tinyint DEFAULT NULL COMMENT 'Note de satisfaction 1-5',
  `commentaires` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`date_creation`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_groupe` (`groupe`),
  KEY `idx_objectif` (`objectif`),
  KEY `idx_date_creation` (`date_creation`),
  KEY `idx_periode` (`periode_test`),
  CONSTRAINT `suivi_nutritionnel_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suivi_nutritionnel`
--

LOCK TABLES `suivi_nutritionnel` WRITE;
/*!40000 ALTER TABLE `suivi_nutritionnel` DISABLE KEYS */;
INSERT INTO `suivi_nutritionnel` (`id`, `id_joueur`, `groupe`, `date_creation`, `periode_test`, `age`, `poids_depart`, `taille`, `objectif`, `details_objectif`, `regime_specifique`, `date_premier_suivi`, `date_deuxieme_suivi`, `date_troisieme_suivi`, `eval_premier_suivi`, `eval_deuxieme_suivi`, `eval_troisieme_suivi`, `poids_actuel`, `satisfaction`, `commentaires`) VALUES (1,7,'Groupe 1','2025-06-04','Période 1',25,75.50,1.80,'Maintien','Maintenir le poids','Régime équilibré',NULL,NULL,NULL,NULL,NULL,NULL,75.50,5,'RAS');
/*!40000 ALTER TABLE `suivi_nutritionnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_athletique`
--

DROP TABLE IF EXISTS `test_athletique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_athletique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `categorie` enum('Minimes A','Minimes B','Juniors','Cadets A','Cadets B','Seniors A','Seniors B') NOT NULL DEFAULT 'Juniors',
  `date_test` date NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `detente_horizontale` decimal(5,2) DEFAULT NULL COMMENT 'en mètres',
  `detente_verticale` decimal(5,2) DEFAULT NULL COMMENT 'en cm',
  `vitesse_thalf_test` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `vitesse_10m` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `vitesse_20m` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `vitesse_30m` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `aerobie_vameval_vo2max` decimal(5,2) DEFAULT NULL,
  `vma_kmh` decimal(4,2) DEFAULT NULL COMMENT 'Vitesse Maximale Aérobie en km/h',
  `vma_ms` decimal(4,2) DEFAULT NULL COMMENT 'Vitesse Maximale Aérobie en m/s',
  `yoyo_pal` int DEFAULT NULL COMMENT 'Palier YOYO atteint',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`date_test`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_date` (`date_test`),
  KEY `idx_periode` (`periode_test`),
  CONSTRAINT `test_athletique_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_athletique`
--

LOCK TABLES `test_athletique` WRITE;
/*!40000 ALTER TABLE `test_athletique` DISABLE KEYS */;
INSERT INTO `test_athletique` VALUES (1,7,'Juniors','2025-06-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15);
/*!40000 ALTER TABLE `test_athletique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_medical`
--

DROP TABLE IF EXISTS `test_medical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_medical` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `categorie` enum('Minimes A','Minimes B','Juniors','Cadets A','Cadets B','Seniors A','Seniors B') NOT NULL DEFAULT 'Juniors',
  `date_test` date NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `taille` int DEFAULT NULL COMMENT 'Taille en cm',
  `poids` decimal(5,2) DEFAULT NULL COMMENT 'Poids en kg',
  `masse_grasse` decimal(5,2) DEFAULT NULL COMMENT 'Masse grasse en %',
  `examen_general` tinyint DEFAULT NULL,
  `examen_orthopedique` tinyint DEFAULT NULL,
  `examen_dentaire` tinyint DEFAULT NULL,
  `examen_orl` tinyint DEFAULT NULL,
  `examen_dermatologique` tinyint DEFAULT NULL,
  `examen_psychologique` tinyint DEFAULT NULL,
  `commentaires` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`date_test`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_date` (`date_test`),
  KEY `idx_periode` (`periode_test`),
  KEY `idx_categorie` (`categorie`),
  CONSTRAINT `test_medical_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_medical`
--

LOCK TABLES `test_medical` WRITE;
/*!40000 ALTER TABLE `test_medical` DISABLE KEYS */;
INSERT INTO `test_medical` VALUES (1,7,'Juniors','2025-06-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS');
/*!40000 ALTER TABLE `test_medical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_morphologique`
--

DROP TABLE IF EXISTS `test_morphologique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_morphologique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `date_test` date NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `poids` decimal(5,2) DEFAULT NULL COMMENT 'Poids en kg',
  `taille` int DEFAULT NULL COMMENT 'Taille en cm',
  `imc` decimal(5,2) GENERATED ALWAYS AS ((`poids` / ((`taille` / 100) * (`taille` / 100)))) STORED COMMENT 'Indice de Masse Corporelle',
  `masse_grasse` decimal(5,2) DEFAULT NULL COMMENT 'Pourcentage de masse grasse',
  `classification_imc` varchar(50) GENERATED ALWAYS AS ((case when ((`poids` / ((`taille` / 100) * (`taille` / 100))) < 18.5) then _utf8mb4'Maigreur' when ((`poids` / ((`taille` / 100) * (`taille` / 100))) < 25) then _utf8mb4'Normal' when ((`poids` / ((`taille` / 100) * (`taille` / 100))) < 30) then _utf8mb4'Surpoids' else _utf8mb4'Obésité' end)) STORED,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`date_test`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_date` (`date_test`),
  KEY `idx_periode` (`periode_test`),
  CONSTRAINT `test_morphologique_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_morphologique`
--

LOCK TABLES `test_morphologique` WRITE;
/*!40000 ALTER TABLE `test_morphologique` DISABLE KEYS */;
INSERT INTO `test_morphologique` (`id`, `id_joueur`, `date_test`, `periode_test`, `poids`, `taille`, `masse_grasse`) VALUES (1,7,'2025-06-04','Période 1',75.50,180,15.00);
/*!40000 ALTER TABLE `test_morphologique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `evaluation_generale`
--

/*!50001 DROP VIEW IF EXISTS `evaluation_generale`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `evaluation_generale` AS select 'Periode' AS `TYPE`,`e`.`evaluation_date` AS `Date`,`etec`.`moyenne_technique` AS `moyenne_technique`,`etac`.`moyenne_tactique` AS `moyenne_tactique`,`ec`.`moyenne_comportementale` AS `moyenne_comportementale`,`e`.`moyenne_generale` AS `moyenne_generale` from (((`evaluation_sur_periode` `e` join `evaluation_technique` `etec`) join `evaluation_tactique` `etac`) join `evaluation_comportementale` `ec`) where ((`e`.`id_evaluation_technique` = `etec`.`id`) and (`e`.`id_evaluation_tactique` = `etac`.`id`) and (`e`.`id_evaluation_comportementale` = `ec`.`id`) and (`e`.`id_joueur` = 7)) union all select 'Match' AS `TYPE`,`m`.`date_match` AS `Date`,`etec`.`moyenne_technique` AS `moyenne_technique`,`etac`.`moyenne_tactique` AS `moyenne_tactique`,`ec`.`moyenne_comportementale` AS `moyenne_comportementale`,`e`.`moyenne_generale` AS `moyenne_generale` from ((((`evaluation_sur_match` `e` join `evaluation_technique` `etec`) join `evaluation_tactique` `etac`) join `evaluation_comportementale` `ec`) join `matchs` `m`) where ((`e`.`id_evaluation_technique` = `etec`.`id`) and (`e`.`id_evaluation_tactique` = `etac`.`id`) and (`e`.`id_evaluation_comportementale` = `ec`.`id`) and (`e`.`id_match` = `m`.`id`) and (`e`.`id_joueur` = 7)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-06 21:12:31
