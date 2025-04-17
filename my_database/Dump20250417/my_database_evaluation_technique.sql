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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_technique`
--

LOCK TABLES `evaluation_technique` WRITE;
/*!40000 ALTER TABLE `evaluation_technique` DISABLE KEYS */;
INSERT INTO `evaluation_technique` VALUES (1,1,'2025-01-01',3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3.50),(2,1,'2025-02-01',4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4.00),(3,1,'2025-03-01',5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4.50),(4,1,'2025-01-15',3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3.50),(5,1,'2025-02-20',4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4.00),(8,1,'2025-03-10',1,0,1,1,1,1,1,1,1,1,0,1,3,0,2,3,3,1.24),(9,1,'2025-04-16',2,1,1,5,1,1,1,1,1,0,0,0,0,0,0,0,0,0.82),(13,1,'2024-07-14',4,2,4,3,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2.80),(14,1,'2024-08-02',3,4,3,2,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2.80),(15,1,'2024-05-05',3,3,2,4,5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.40),(16,1,'2024-06-03',4,3,4,1,3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.00),(17,1,'2024-10-10',1,5,2,2,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2.20),(18,1,'2024-07-27',1,5,3,5,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.20),(19,1,'2024-12-31',4,4,3,1,5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.40),(20,1,'2025-03-23',2,3,4,3,5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.40),(21,1,'2024-12-13',5,5,5,2,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,4.20),(22,1,'2024-08-18',5,3,5,1,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.20),(23,1,'2025-02-06',2,3,5,2,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2.60),(24,1,'2024-10-15',4,1,2,3,2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2.40),(25,1,'2024-07-29',3,4,4,3,4,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,3.60),(26,1,'2024-12-09',5,5,3,5,5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,4.60);
/*!40000 ALTER TABLE `evaluation_technique` ENABLE KEYS */;
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
