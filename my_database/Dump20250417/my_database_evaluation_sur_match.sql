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
  `videopath` varchar(255) NOT NULL,
  UNIQUE KEY `h` (`id_joueur`,`id_match`),
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
INSERT INTO `evaluation_sur_match` VALUES (1,1,4,4,4,3.43,'vid1'),(1,2,5,5,5,4.00,'vid2'),(1,3,8,8,8,1.77,'evaluations-matchs-vids/evaluation-Dupont Jean-EST-2025-03-10 00:00:00.mp4'),(1,5,13,13,13,2.93,'videos/match_5_evaluation.mp4'),(1,6,14,14,14,2.52,'videos/match_6_evaluation.mp4'),(1,7,15,15,15,2.55,'videos/match_7_evaluation.mp4'),(1,8,16,16,16,3.25,'videos/match_8_evaluation.mp4'),(1,9,17,17,17,2.65,'videos/match_9_evaluation.mp4'),(1,10,18,18,18,2.73,'videos/match_10_evaluation.mp4'),(1,11,23,23,23,2.78,'videos/match_11_evaluation.mp4'),(1,12,24,24,24,2.13,'videos/match_12_evaluation.mp4'),(1,13,25,25,25,3.12,'videos/match_13_evaluation.mp4');
/*!40000 ALTER TABLE `evaluation_sur_match` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17  9:14:58
