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
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_comportementale`
--

LOCK TABLES `evaluation_comportementale` WRITE;
/*!40000 ALTER TABLE `evaluation_comportementale` DISABLE KEYS */;
INSERT INTO `evaluation_comportementale` VALUES (1,4,'2025-04-04',4,4,3,4,3,4,3,3.60),(2,4,'2025-04-05',4,4,3,4,3,4,3,3.60),(3,4,'2025-04-06',4,4,3,4,3,4,3,3.60),(4,4,'2025-04-07',4,4,3,4,3,4,3,3.60),(5,4,'2025-04-08',4,4,3,4,3,4,3,3.60),(6,10,'2025-04-04',4,4,3,4,3,4,3,3.60),(7,10,'2025-04-05',4,4,3,4,3,4,3,3.60),(8,10,'2025-04-06',4,4,3,4,3,4,3,3.60),(9,10,'2025-04-07',4,4,3,4,3,4,3,3.60),(10,10,'2025-04-08',4,4,3,4,3,4,3,3.60),(11,11,'2025-04-04',4,4,3,4,3,4,3,3.60),(12,11,'2025-04-05',4,4,3,4,3,4,3,3.60),(13,11,'2025-04-06',4,4,3,4,3,4,3,3.60),(14,11,'2025-04-07',4,4,3,4,3,4,3,3.60),(15,11,'2025-04-08',4,4,3,4,3,4,3,3.60),(16,2,'2025-04-04',4,4,3,4,3,4,3,3.60),(17,2,'2025-04-05',4,4,3,4,3,4,3,3.60),(18,2,'2025-04-06',4,4,3,4,3,4,3,3.60),(19,2,'2025-04-07',4,4,3,4,3,4,3,3.60),(20,2,'2025-04-08',4,4,3,4,3,4,3,3.60),(21,14,'2025-04-04',4,4,3,4,3,4,3,3.60),(22,14,'2025-04-05',4,4,3,4,3,4,3,3.60),(23,14,'2025-04-06',4,4,3,4,3,4,3,3.60),(24,14,'2025-04-07',4,4,3,4,3,4,3,3.60),(25,14,'2025-04-08',4,4,3,4,3,4,3,3.60),(26,8,'2025-04-04',4,4,3,4,3,4,3,3.60),(27,8,'2025-04-05',4,4,3,4,3,4,3,3.60),(28,8,'2025-04-06',4,4,3,4,3,4,3,3.60),(29,8,'2025-04-07',4,4,3,4,3,4,3,3.60),(30,8,'2025-04-08',4,4,3,4,3,4,3,3.60),(31,5,'2025-04-04',4,4,3,4,3,4,3,3.60),(32,5,'2025-04-05',4,4,3,4,3,4,3,3.60),(33,5,'2025-04-06',4,4,3,4,3,4,3,3.60),(34,5,'2025-04-07',4,4,3,4,3,4,3,3.60),(35,5,'2025-04-08',4,4,3,4,3,4,3,3.60),(36,6,'2025-04-04',4,4,3,4,3,4,3,3.60),(37,6,'2025-04-05',4,4,3,4,3,4,3,3.60),(38,6,'2025-04-06',4,4,3,4,3,4,3,3.60),(39,6,'2025-04-07',4,4,3,4,3,4,3,3.60),(40,6,'2025-04-08',4,4,3,4,3,4,3,3.60),(41,12,'2025-04-04',4,4,3,4,3,4,3,3.60),(42,12,'2025-04-05',4,4,3,4,3,4,3,3.60),(43,12,'2025-04-06',4,4,3,4,3,4,3,3.60),(44,12,'2025-04-07',4,4,3,4,3,4,3,3.60),(45,12,'2025-04-08',4,4,3,4,3,4,3,3.60),(46,3,'2025-04-04',4,4,3,4,3,4,3,3.60),(47,3,'2025-04-05',4,4,3,4,3,4,3,3.60),(48,3,'2025-04-06',4,4,3,4,3,4,3,3.60),(49,3,'2025-04-07',4,4,3,4,3,4,3,3.60),(50,3,'2025-04-08',4,4,3,4,3,4,3,3.60),(51,9,'2025-04-04',4,4,3,4,3,4,3,3.60),(52,9,'2025-04-05',4,4,3,4,3,4,3,3.60),(53,9,'2025-04-06',4,4,3,4,3,4,3,3.60),(54,9,'2025-04-07',4,4,3,4,3,4,3,3.60),(55,9,'2025-04-08',4,4,3,4,3,4,3,3.60),(56,15,'2025-04-04',4,4,3,4,3,4,3,3.60),(57,15,'2025-04-05',4,4,3,4,3,4,3,3.60),(58,15,'2025-04-06',4,4,3,4,3,4,3,3.60),(59,15,'2025-04-07',4,4,3,4,3,4,3,3.60),(60,15,'2025-04-08',4,4,3,4,3,4,3,3.60),(61,1,'2025-04-04',4,4,3,4,5,4,3,3.60),(62,1,'2025-04-05',4,4,3,4,3,4,3,3.60),(63,1,'2025-04-06',4,4,3,4,3,4,3,3.60),(64,1,'2025-04-07',4,4,3,4,3,4,3,3.60),(65,1,'2025-04-08',4,4,3,4,3,4,3,3.60),(66,7,'2025-04-04',4,4,3,4,3,4,3,3.60),(67,7,'2025-04-05',4,4,3,4,3,4,3,3.60),(68,7,'2025-04-06',4,4,3,4,3,4,3,3.60),(69,7,'2025-04-07',4,4,3,4,3,4,3,3.60),(70,7,'2025-04-08',4,4,3,4,3,4,3,3.60),(71,13,'2025-04-04',4,4,3,4,3,4,3,3.60),(72,13,'2025-04-05',4,4,3,4,3,4,3,3.60),(73,13,'2025-04-06',4,4,3,4,3,4,3,3.60),(74,13,'2025-04-07',4,4,3,4,3,4,3,3.60),(75,13,'2025-04-08',4,4,3,4,3,4,3,3.60),(77,1,'2024-10-31',0,0,0,0,0,0,0,0.00);
/*!40000 ALTER TABLE `evaluation_comportementale` ENABLE KEYS */;
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
