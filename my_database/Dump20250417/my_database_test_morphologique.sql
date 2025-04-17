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
-- Table structure for table `test_morphologique`
--

DROP TABLE IF EXISTS `test_morphologique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_morphologique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_joueur` int NOT NULL,
  `date_test` date NOT NULL,
  `periode_test` enum('Période 1','Période 2','Période 3','Période 4','Période 5') NOT NULL DEFAULT 'Période 1',
  `poids` decimal(5,2) DEFAULT NULL COMMENT 'Poids en kg',
  `taille` int DEFAULT NULL COMMENT 'Taille en cm',
  `imc` decimal(5,2) GENERATED ALWAYS AS ((`poids` / ((`taille` / 100) * (`taille` / 100)))) STORED COMMENT 'Indice de Masse Corporelle',
  `masse_grasse` decimal(5,2) DEFAULT NULL COMMENT 'Pourcentage de masse grasse',
  `classification_imc` varchar(50) GENERATED ALWAYS AS ((case when ((`poids` / ((`taille` / 100) * (`taille` / 100))) < 18.5) then _utf8mb4'Maigreur' when ((`poids` / ((`taille` / 100) * (`taille` / 100))) < 25) then _utf8mb4'Normal' when ((`poids` / ((`taille` / 100) * (`taille` / 100))) < 30) then _utf8mb4'Surpoids' else _utf8mb4'Obésité' end)) STORED,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_joueur_date` (`id_joueur`,`date_test`),
  UNIQUE KEY `uk_joueur_periode` (`id_joueur`,`periode_test`),
  KEY `idx_joueur` (`id_joueur`),
  KEY `idx_date` (`date_test`),
  KEY `idx_periode` (`periode_test`),
  CONSTRAINT `test_morphologique_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_morphologique`
--

LOCK TABLES `test_morphologique` WRITE;
/*!40000 ALTER TABLE `test_morphologique` DISABLE KEYS */;
INSERT INTO `test_morphologique` (`id`, `id_joueur`, `date_test`, `periode_test`, `poids`, `taille`, `masse_grasse`) VALUES (1,1,'2025-01-15','Période 1',70.00,180,15.00),(2,1,'2025-02-20','Période 2',71.00,180,14.00),(3,1,'2025-03-10','Période 3',72.00,180,13.00),(4,1,'2025-04-16','Période 4',50.00,50,50.00);
/*!40000 ALTER TABLE `test_morphologique` ENABLE KEYS */;
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
