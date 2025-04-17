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
-- Table structure for table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joueur` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_prenom` varchar(255) NOT NULL,
  `categorie` enum('Ecole B','Ecole A','Minime B','Minime A','Cadet B','Cadet A','Junior','Senior B','Senior') DEFAULT NULL,
  `selection_nationale` varchar(50) DEFAULT NULL,
  `poste_principal` enum('Gardien','Défenseur','Milieu','Attaquant','Latéral','Pivot') NOT NULL,
  `pied_fort` enum('Droit','Gauche','Ambidextre') DEFAULT NULL,
  `taille` int DEFAULT NULL,
  `poids` decimal(5,2) DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `matchs_joues` int DEFAULT '0',
  `titulaire` int DEFAULT '0',
  `remplacant` int DEFAULT '0',
  `tempsjeu` int DEFAULT '0',
  `buts` int DEFAULT '0',
  `assists` int DEFAULT '0',
  `carton_jaune` int DEFAULT '0',
  `carton_rouge` int DEFAULT '0',
  `est_blesse` tinyint(1) DEFAULT '0',
  `type_blessure` enum('Musculaire','Articulaire','Fracture','Ligamentaire','Tendinite','Commotion','Autre') DEFAULT NULL,
  `date_blessure` date DEFAULT NULL,
  `date_retour_prevue` date DEFAULT NULL,
  `severite_blessure` enum('Légère','Modérée','Grave','Très grave') DEFAULT NULL,
  `description_blessure` text,
  PRIMARY KEY (`id`),
  KEY `idx_categorie` (`categorie`),
  KEY `idx_poste` (`poste_principal`),
  KEY `idx_blesse` (`est_blesse`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueur`
--

LOCK TABLES `joueur` WRITE;
/*!40000 ALTER TABLE `joueur` DISABLE KEYS */;
INSERT INTO `joueur` VALUES (1,'Dupont Jean','Senior','France','Milieu','Droit',180,75.50,'1990-05-15',50,40,10,3600,15,10,2,0,0,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `joueur` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17  9:14:57
