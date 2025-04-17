-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: my_database
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suivi_nutritionnel`
--

LOCK TABLES `suivi_nutritionnel` WRITE;
/*!40000 ALTER TABLE `suivi_nutritionnel` DISABLE KEYS */;
/*!40000 ALTER TABLE `suivi_nutritionnel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17  9:14:56
