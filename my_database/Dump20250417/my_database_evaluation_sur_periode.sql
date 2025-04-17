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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_sur_periode`
--

LOCK TABLES `evaluation_sur_periode` WRITE;
/*!40000 ALTER TABLE `evaluation_sur_periode` DISABLE KEYS */;
INSERT INTO `evaluation_sur_periode` VALUES (1,1,'Période 1','2025-01-15',1,1,1,1,1,1,NULL,3.50),(2,1,'Période 2','2025-02-20',2,2,2,2,2,2,NULL,4.00),(3,1,'Période 3','2025-03-10',3,3,3,3,3,3,NULL,4.50);
/*!40000 ALTER TABLE `evaluation_sur_periode` ENABLE KEYS */;
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
