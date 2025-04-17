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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchs`
--

LOCK TABLES `matchs` WRITE;
/*!40000 ALTER TABLE `matchs` DISABLE KEYS */;
INSERT INTO `matchs` (`id`, `date_match`, `lieu`, `adversaire`, `type_match`, `domicile`, `score_equipe`, `score_adversaire`, `competion`, `saison`, `temps_reglementaire`, `prolongation`, `penalties`, `conditions_meteo`, `temperature`, `public`, `arbitre_principal`, `arbitre_assistant_1`, `arbitre_assistant_2`, `commentaires`) VALUES (1,'2025-01-15 00:00:00','Stade A','EST','Championnat',1,2,1,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'2025-02-20 00:00:00','Stade B','EST','Coupe',0,1,1,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(3,'2025-03-10 00:00:00','Stade C','EST','Amical',1,3,0,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'2025-01-10 00:00:00','Stade Rades','EST','Championnat',1,2,1,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'2025-01-20 00:00:00','Stade Sousse','ESS','Championnat',0,1,1,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,'2025-02-05 00:00:00','Stade Bardo','ST','Coupe',1,3,0,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,'2025-02-15 00:00:00','Stade Tunis','CA','Championnat',0,0,2,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(8,'2025-03-01 00:00:00','Stade Monastir','USMo','Championnat',1,1,1,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(9,'2025-03-10 00:00:00','Stade Gabes','ASG','Amical',0,2,2,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(10,'2025-03-20 00:00:00','Stade Tataouine','UST','Championnat',1,3,1,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11,'2025-04-05 00:00:00','Stade Kairouan','JSK','Coupe',0,1,0,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(12,'2025-04-15 00:00:00','Stade Hammamet','ASH','Amical',1,4,2,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(13,'2025-04-25 00:00:00','Stade Zarzis','ESZ','Championnat',0,0,0,NULL,'2024/2025',90,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `matchs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17  9:14:57
