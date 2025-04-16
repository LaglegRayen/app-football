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
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_sur_periode`
--

LOCK TABLES `evaluation_sur_periode` WRITE;
/*!40000 ALTER TABLE `evaluation_sur_periode` DISABLE KEYS */;
INSERT INTO `evaluation_sur_periode` VALUES (1,4,'Période 1','2025-04-04',1,1,1,NULL,NULL,NULL,NULL,3.57),(2,4,'Période 2','2025-04-05',2,2,2,NULL,NULL,NULL,NULL,3.57),(3,4,'Période 3','2025-04-06',3,3,3,NULL,NULL,NULL,NULL,3.57),(4,4,'Période 4','2025-04-07',4,4,4,NULL,NULL,NULL,NULL,3.57),(5,4,'Période 5','2025-04-08',5,5,5,NULL,NULL,NULL,NULL,3.57),(6,10,'Période 1','2025-04-04',6,6,6,NULL,NULL,NULL,NULL,3.57),(7,10,'Période 2','2025-04-05',7,7,7,NULL,NULL,NULL,NULL,3.57),(8,10,'Période 3','2025-04-06',8,8,8,NULL,NULL,NULL,NULL,3.57),(9,10,'Période 4','2025-04-07',9,9,9,NULL,NULL,NULL,NULL,3.57),(10,10,'Période 5','2025-04-08',10,10,10,NULL,NULL,NULL,NULL,3.57),(11,11,'Période 1','2025-04-04',11,11,11,NULL,NULL,NULL,NULL,3.57),(12,11,'Période 2','2025-04-05',12,12,12,NULL,NULL,NULL,NULL,3.57),(13,11,'Période 3','2025-04-06',13,13,13,NULL,NULL,NULL,NULL,3.57),(14,11,'Période 4','2025-04-07',14,14,14,NULL,NULL,NULL,NULL,3.57),(15,11,'Période 5','2025-04-08',15,15,15,NULL,NULL,NULL,NULL,3.57),(16,2,'Période 1','2025-04-04',16,16,16,NULL,NULL,NULL,NULL,3.57),(17,2,'Période 2','2025-04-05',17,17,17,NULL,NULL,NULL,NULL,3.57),(18,2,'Période 3','2025-04-06',18,18,18,NULL,NULL,NULL,NULL,3.57),(19,2,'Période 4','2025-04-07',19,19,19,NULL,NULL,NULL,NULL,3.57),(20,2,'Période 5','2025-04-08',20,20,20,NULL,NULL,NULL,NULL,3.57),(21,14,'Période 1','2025-04-04',21,21,21,NULL,NULL,NULL,NULL,3.57),(22,14,'Période 2','2025-04-05',22,22,22,NULL,NULL,NULL,NULL,3.57),(23,14,'Période 3','2025-04-06',23,23,23,NULL,NULL,NULL,NULL,3.57),(24,14,'Période 4','2025-04-07',24,24,24,NULL,NULL,NULL,NULL,3.57),(25,14,'Période 5','2025-04-08',25,25,25,NULL,NULL,NULL,NULL,3.57),(26,8,'Période 1','2025-04-04',26,26,26,NULL,NULL,NULL,NULL,3.57),(27,8,'Période 2','2025-04-05',27,27,27,NULL,NULL,NULL,NULL,3.57),(28,8,'Période 3','2025-04-06',28,28,28,NULL,NULL,NULL,NULL,3.57),(29,8,'Période 4','2025-04-07',29,29,29,NULL,NULL,NULL,NULL,3.57),(30,8,'Période 5','2025-04-08',30,30,30,NULL,NULL,NULL,NULL,3.57),(31,5,'Période 1','2025-04-04',31,31,31,NULL,NULL,NULL,NULL,3.57),(32,5,'Période 2','2025-04-05',32,32,32,NULL,NULL,NULL,NULL,3.57),(33,5,'Période 3','2025-04-06',33,33,33,NULL,NULL,NULL,NULL,3.57),(34,5,'Période 4','2025-04-07',34,34,34,NULL,NULL,NULL,NULL,3.57),(35,5,'Période 5','2025-04-08',35,35,35,NULL,NULL,NULL,NULL,3.57),(36,6,'Période 1','2025-04-04',36,36,36,NULL,NULL,NULL,NULL,3.57),(37,6,'Période 2','2025-04-05',37,37,37,NULL,NULL,NULL,NULL,3.57),(38,6,'Période 3','2025-04-06',38,38,38,NULL,NULL,NULL,NULL,3.57),(39,6,'Période 4','2025-04-07',39,39,39,NULL,NULL,NULL,NULL,3.57),(40,6,'Période 5','2025-04-08',40,40,40,NULL,NULL,NULL,NULL,3.57),(41,12,'Période 1','2025-04-04',41,41,41,NULL,NULL,NULL,NULL,3.57),(42,12,'Période 2','2025-04-05',42,42,42,NULL,NULL,NULL,NULL,3.57),(43,12,'Période 3','2025-04-06',43,43,43,NULL,NULL,NULL,NULL,3.57),(44,12,'Période 4','2025-04-07',44,44,44,NULL,NULL,NULL,NULL,3.57),(45,12,'Période 5','2025-04-08',45,45,45,NULL,NULL,NULL,NULL,3.57),(46,3,'Période 1','2025-04-04',46,46,46,NULL,NULL,NULL,NULL,3.57),(47,3,'Période 2','2025-04-05',47,47,47,NULL,NULL,NULL,NULL,3.57),(48,3,'Période 3','2025-04-06',48,48,48,NULL,NULL,NULL,NULL,3.57),(49,3,'Période 4','2025-04-07',49,49,49,NULL,NULL,NULL,NULL,3.57),(50,3,'Période 5','2025-04-08',50,50,50,NULL,NULL,NULL,NULL,3.57),(51,9,'Période 1','2025-04-04',51,51,51,NULL,NULL,NULL,NULL,3.57),(52,9,'Période 2','2025-04-05',52,52,52,NULL,NULL,NULL,NULL,3.57),(53,9,'Période 3','2025-04-06',53,53,53,NULL,NULL,NULL,NULL,3.57),(54,9,'Période 4','2025-04-07',54,54,54,NULL,NULL,NULL,NULL,3.57),(55,9,'Période 5','2025-04-08',55,55,55,NULL,NULL,NULL,NULL,3.57),(56,15,'Période 1','2025-04-04',56,56,56,NULL,NULL,NULL,NULL,3.57),(57,15,'Période 2','2025-04-05',57,57,57,NULL,NULL,NULL,NULL,3.57),(58,15,'Période 3','2025-04-06',58,58,58,NULL,NULL,NULL,NULL,3.57),(59,15,'Période 4','2025-04-07',59,59,59,NULL,NULL,NULL,NULL,3.57),(60,15,'Période 5','2025-04-08',60,60,60,NULL,NULL,NULL,NULL,3.57),(61,1,'Période 1','2025-04-04',61,61,61,NULL,NULL,NULL,NULL,3.57),(62,1,'Période 2','2025-04-05',62,62,62,NULL,NULL,NULL,NULL,3.57),(63,1,'Période 3','2025-04-06',63,63,63,NULL,NULL,NULL,NULL,3.57),(64,1,'Période 4','2025-04-07',64,64,64,NULL,NULL,NULL,NULL,3.57),(65,1,'Période 5','2025-04-08',65,65,65,NULL,NULL,NULL,NULL,3.57),(66,7,'Période 1','2025-04-04',66,66,66,NULL,NULL,NULL,NULL,3.57),(67,7,'Période 2','2025-04-05',67,67,67,NULL,NULL,NULL,NULL,3.57),(68,7,'Période 3','2025-04-06',68,68,68,NULL,NULL,NULL,NULL,3.57),(69,7,'Période 4','2025-04-07',69,69,69,NULL,NULL,NULL,NULL,3.57),(70,7,'Période 5','2025-04-08',70,70,70,NULL,NULL,NULL,NULL,3.57),(71,13,'Période 1','2025-04-04',71,71,71,NULL,NULL,NULL,NULL,3.57),(72,13,'Période 2','2025-04-05',72,72,72,NULL,NULL,NULL,NULL,3.57),(73,13,'Période 3','2025-04-06',73,73,73,NULL,NULL,NULL,NULL,3.57),(74,13,'Période 4','2025-04-07',74,74,74,NULL,NULL,NULL,NULL,3.57),(75,13,'Période 5','2025-04-08',75,75,75,NULL,NULL,NULL,NULL,3.57);
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

-- Dump completed on 2025-04-15 20:42:54
