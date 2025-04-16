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
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_medical`
--

LOCK TABLES `test_medical` WRITE;
/*!40000 ALTER TABLE `test_medical` DISABLE KEYS */;
INSERT INTO `test_medical` VALUES (1,4,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(2,4,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(3,4,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(4,4,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(5,4,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(6,10,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(7,10,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(8,10,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(9,10,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(10,10,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(11,11,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(12,11,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(13,11,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(14,11,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(15,11,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(16,2,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(17,2,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(18,2,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(19,2,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(20,2,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(21,14,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(22,14,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(23,14,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(24,14,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(25,14,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(26,8,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(27,8,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(28,8,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(29,8,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(30,8,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(31,5,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(32,5,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(33,5,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(34,5,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(35,5,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(36,6,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(37,6,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(38,6,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(39,6,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(40,6,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(41,12,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(42,12,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(43,12,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(44,12,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(45,12,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(46,3,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(47,3,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(48,3,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(49,3,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(50,3,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(51,9,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(52,9,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(53,9,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(54,9,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(55,9,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(56,15,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(57,15,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(58,15,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(59,15,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(60,15,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(61,1,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(62,1,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(63,1,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(64,1,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(65,1,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(66,7,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(67,7,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(68,7,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(69,7,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(70,7,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(71,13,'Juniors','2025-04-04','Période 1',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(72,13,'Juniors','2025-04-05','Période 2',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(73,13,'Juniors','2025-04-06','Période 3',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(74,13,'Juniors','2025-04-07','Période 4',180,75.50,15.00,4,4,3,4,3,4,'RAS'),(75,13,'Juniors','2025-04-08','Période 5',180,75.50,15.00,4,4,3,4,3,4,'RAS');
/*!40000 ALTER TABLE `test_medical` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-15 20:42:55
