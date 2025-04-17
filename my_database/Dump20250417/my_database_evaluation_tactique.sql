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
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_tactique`
--

LOCK TABLES `evaluation_tactique` WRITE;
/*!40000 ALTER TABLE `evaluation_tactique` DISABLE KEYS */;
INSERT INTO `evaluation_tactique` VALUES (1,1,'2025-01-01',3,3,4,3,4,3.40),(2,1,'2025-02-01',4,4,4,4,4,4.00),(3,1,'2025-03-01',4,5,5,4,5,4.60),(4,1,'2025-01-15',3,3,4,3,4,3.40),(5,1,'2025-02-20',4,4,4,4,4,4.00),(8,1,'2025-03-10',5,1,1,1,1,1.80),(9,1,'2025-04-16',1,1,1,1,1,1.00),(13,1,'2024-07-14',5,1,2,NULL,1,2.25),(14,1,'2024-08-02',2,5,3,NULL,1,2.75),(15,1,'2024-05-05',1,1,2,NULL,2,1.50),(16,1,'2024-06-03',5,5,2,NULL,3,3.75),(17,1,'2024-10-10',4,1,3,NULL,4,3.00),(18,1,'2024-07-27',2,4,2,NULL,2,2.50),(19,1,'2024-12-31',3,3,1,NULL,4,2.75),(20,1,'2025-03-23',3,4,5,NULL,4,4.00),(21,1,'2024-12-13',4,5,3,NULL,4,4.00),(22,1,'2024-08-18',4,3,5,NULL,3,3.75),(23,1,'2025-02-06',4,3,2,NULL,1,2.50),(24,1,'2024-10-15',1,4,3,NULL,1,2.25),(25,1,'2024-07-29',3,4,2,NULL,1,2.50),(26,1,'2024-12-09',2,2,3,NULL,1,2.00);
/*!40000 ALTER TABLE `evaluation_tactique` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17  9:14:55
