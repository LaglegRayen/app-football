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
-- Table structure for table `test_athletique`
--

DROP TABLE IF EXISTS `test_athletique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_athletique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `categorie` enum('Ecole B','Ecole A','Minime B','Minime A','Cadet B','Cadet A','Junior','Senior B','Senior') NOT NULL DEFAULT 'Ecole B',
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_athletique`
--

LOCK TABLES `test_athletique` WRITE;
/*!40000 ALTER TABLE `test_athletique` DISABLE KEYS */;
INSERT INTO `test_athletique` VALUES (1,1,'Senior','2025-01-15','Période 1',2.50,50.00,12.50,1.20,2.40,3.60,45.00,12.00,3.30,15),(2,1,'Senior','2025-02-20','Période 2',2.60,51.00,12.40,1.10,2.30,3.50,46.00,12.50,3.40,16),(3,1,'Senior','2025-03-10','Période 3',2.70,52.00,12.30,1.00,2.20,3.40,47.00,13.00,3.50,17),(7,1,'Senior','2025-04-16','Période 4',0.70,0.60,0.50,0.30,0.70,0.50,0.80,0.50,0.70,5);
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

-- Dump completed on 2025-04-17  9:14:58
