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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matchs`
--

LOCK TABLES `matchs` WRITE;
/*!40000 ALTER TABLE `matchs` DISABLE KEYS */;
INSERT INTO `matchs` (`id`, `date_match`, `lieu`, `adversaire`, `type_match`, `domicile`, `score_equipe`, `score_adversaire`, `competion`, `saison`, `temps_reglementaire`, `prolongation`, `penalties`, `conditions_meteo`, `temperature`, `public`, `arbitre_principal`, `arbitre_assistant_1`, `arbitre_assistant_2`, `commentaires`) VALUES (1,'2024-06-08 17:30:08','Stade Olympique de Radès','USMO','Tournoi',1,2,2,'Coupe de Tunisie','2024/2025',90,0,1,'Neige',18,28475,'Sami M.','Tahar G.','Hichem C.','But exceptionnel à la 90e.'),(2,'2024-10-31 17:30:08','Stade Mustapha Ben Jannet','EST','Amical',0,0,3,'Tournoi Printemps','2023/2024',90,0,0,'Neige',34,40606,'Karim H.','Ali S.','Hichem C.','Carton rouge direct à la 65e.'),(3,'2024-07-13 17:30:08','Stade Chedly Zouiten','EST','Championnat',1,3,0,'Coupe de Tunisie','2024/2025',90,0,1,'Chaleur',30,47695,'Fethi B.','Tahar G.','Hichem C.','Interruption de 10 minutes pour incident.'),(4,'2024-08-13 17:30:08','Stade Chedly Zouiten','USMO','Coupe',1,3,2,'Coupe de Tunisie','2024/2025',90,1,0,'Neige',23,10712,'Sami M.','Tahar G.','Hichem C.','Interruption de 10 minutes pour incident.'),(5,'2024-04-21 17:30:08','Stade Chedly Zouiten','ASG','Tournoi',0,3,1,'Ligue 1','2024/2025',90,0,1,'Brouillard',21,34584,'Karim H.','Nidhal K.','Yassine B.','But exceptionnel à la 90e.'),(6,'2024-09-19 17:30:08','Stade Olympique de Radès','EST','Coupe',1,4,2,'Ligue 1','2024/2025',90,1,0,'Pluie',26,31759,'Fethi B.','Tahar G.','Yassine B.','Match sans incidents.'),(7,'2024-08-16 17:30:08','Stade Chedly Zouiten','USBG','Coupe',1,4,4,'Coupe de Tunisie','2023/2024',90,0,0,'Vent',35,13022,'Karim H.','Ali S.','Hichem C.','Match sans incidents.'),(8,'2024-07-29 17:30:08','Stade Chedly Zouiten','ASG','Tournoi',1,3,0,'Tournoi Printemps','2024/2025',90,0,1,'Bon',35,4008,'Sami M.','Tahar G.','Yassine B.','Carton rouge direct à la 65e.'),(9,'2024-04-23 17:30:08','Stade Mustapha Ben Jannet','USMO','Tournoi',1,1,2,'Ligue 1','2023/2024',90,0,1,'Brouillard',23,3309,'Sami M.','Nidhal K.','Omar R.','Carton rouge direct à la 65e.'),(10,'2024-04-21 17:30:08','Stade Mustapha Ben Jannet','CA','Tournoi',1,4,2,'Tournoi Printemps','2023/2024',90,0,1,'Vent',38,47851,'Sami M.','Tahar G.','Yassine B.','Interruption de 10 minutes pour incident.'),(11,'2025-01-13 17:30:08','Stade Mustapha Ben Jannet','JSK','Tournoi',1,2,5,'Coupe de Tunisie','2024/2025',90,0,1,'Pluie',10,39451,'Karim H.','Tahar G.','Hichem C.','Match sans incidents.'),(12,'2025-02-09 17:30:08','Stade Mustapha Ben Jannet','CSS','Tournoi',1,4,2,'Ligue 1','2023/2024',90,1,1,'Chaleur',11,16630,'Sami M.','Nidhal K.','Omar R.','Match sans incidents.'),(13,'2024-08-14 17:30:08','Stade Chedly Zouiten','CSS','Amical',0,2,2,'Tournoi Printemps','2024/2025',90,1,0,'Bon',24,21933,'Fethi B.','Tahar G.','Yassine B.','Carton rouge direct à la 65e.'),(14,'2024-07-13 17:30:08','Stade Mustapha Ben Jannet','CA','Coupe',0,1,5,'Tournoi Printemps','2023/2024',90,1,1,'Chaleur',19,3796,'Sami M.','Ali S.','Hichem C.','Carton rouge direct à la 65e.'),(15,'2024-11-21 17:30:08','Stade Olympique de Radès','USBG','Championnat',1,5,1,'Ligue 1','2023/2024',90,0,0,'Chaleur',13,40442,'Sami M.','Tahar G.','Yassine B.','But exceptionnel à la 90e.'),(16,'2024-08-01 17:30:08','Stade Olympique de Radès','CA','Tournoi',1,3,4,'Ligue 1','2024/2025',90,0,1,'Chaleur',15,423,'Fethi B.','Tahar G.','Yassine B.','Carton rouge direct à la 65e.'),(17,'2025-03-03 17:30:08','Stade Mustapha Ben Jannet','ESS','Amical',1,1,4,'Tournoi Printemps','2023/2024',90,1,0,'Brouillard',16,30630,'Sami M.','Ali S.','Hichem C.','Interruption de 10 minutes pour incident.'),(18,'2024-08-20 17:30:08','Stade Chedly Zouiten','USBG','Coupe',1,2,5,'Tournoi Printemps','2023/2024',90,0,1,'Pluie',20,3508,'Fethi B.','Nidhal K.','Omar R.','Carton rouge direct à la 65e.'),(19,'2025-01-01 17:30:08','Stade Mustapha Ben Jannet','EST','Amical',1,5,1,'Tournoi Printemps','2023/2024',90,1,1,'Neige',40,21283,'Karim H.','Nidhal K.','Yassine B.','Interruption de 10 minutes pour incident.'),(20,'2024-12-08 17:30:08','Stade Chedly Zouiten','CAB','Amical',1,0,5,'Coupe de Tunisie','2024/2025',90,1,1,'Bon',18,41240,'Fethi B.','Ali S.','Yassine B.','Match sans incidents.');
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

-- Dump completed on 2025-04-15 20:42:54
