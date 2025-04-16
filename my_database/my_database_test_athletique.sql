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
-- Table structure for table `test_athletique`
--

DROP TABLE IF EXISTS `test_athletique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_athletique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `categorie` enum('Minimes A','Minimes B','Juniors','Cadets A','Cadets B','Seniors A','Seniors B') NOT NULL DEFAULT 'Juniors',
  `date_test` date NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `detente_horizontale` decimal(5,2) DEFAULT NULL COMMENT 'en mètres',
  `detente_verticale` decimal(5,2) DEFAULT NULL COMMENT 'en cm',
  `vitesse_thalf_test` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `vitesse_10m` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `vitesse_20m` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `vitesse_30m` decimal(4,2) DEFAULT NULL COMMENT 'En secondes',
  `aerobie_vameval_vo2max` decimal(5,2) DEFAULT NULL,
  `vma_kmh` decimal(4,2) DEFAULT NULL COMMENT 'Vitesse Maximale Aérobie en km/h',
  `vma_ms` decimal(4,2) DEFAULT NULL COMMENT 'Vitesse Maximale Aérobie en m/s',
  `yoyo_pal` int DEFAULT NULL COMMENT 'Palier YOYO atteint',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`date_test`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_date` (`date_test`),
  KEY `idx_periode` (`periode_test`),
  CONSTRAINT `test_athletique_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_athletique`
--

LOCK TABLES `test_athletique` WRITE;
/*!40000 ALTER TABLE `test_athletique` DISABLE KEYS */;
INSERT INTO `test_athletique` VALUES (1,4,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(2,4,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(3,4,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(4,4,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(5,4,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(6,10,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(7,10,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(8,10,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(9,10,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(10,10,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(11,11,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(12,11,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(13,11,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(14,11,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(15,11,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(16,2,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(17,2,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(18,2,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(19,2,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(20,2,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(21,14,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(22,14,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(23,14,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(24,14,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(25,14,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(26,8,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(27,8,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(28,8,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(29,8,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(30,8,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(31,5,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(32,5,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(33,5,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(34,5,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(35,5,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(36,6,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(37,6,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(38,6,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(39,6,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(40,6,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(41,12,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(42,12,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(43,12,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(44,12,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(45,12,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(46,3,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(47,3,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(48,3,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(49,3,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(50,3,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(51,9,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(52,9,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(53,9,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(54,9,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(55,9,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(56,15,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(57,15,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(58,15,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(59,15,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(60,15,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(61,1,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(62,1,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(63,1,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(64,1,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(65,1,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(66,7,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(67,7,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(68,7,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(69,7,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(70,7,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(71,13,'Juniors','2025-04-04','Période 1',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(72,13,'Juniors','2025-04-05','Période 2',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(73,13,'Juniors','2025-04-06','Période 3',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(74,13,'Juniors','2025-04-07','Période 4',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15),(75,13,'Juniors','2025-04-08','Période 5',2.50,50.00,12.50,1.80,3.50,5.00,60.00,15.00,4.20,15);
/*!40000 ALTER TABLE `test_athletique` ENABLE KEYS */;
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
