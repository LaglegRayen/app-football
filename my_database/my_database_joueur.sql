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
-- Table structure for table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joueur` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_prenom` varchar(100) NOT NULL,
  `categorie` enum('Junior','Senior') DEFAULT NULL,
  `selection_nationale` varchar(50) DEFAULT NULL,
  `poste_principal` enum('Gardien','Arrière droit','Défenseur central droit','Défenseur central gauche','Arrière gauche','Milieu défensif','Milieu central','Milieu offensif','Ailier droit','Ailier gauche','Attaquant','Milieu') NOT NULL DEFAULT 'Milieu',
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
  `videopath` varchar(266) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_nom_prenom` (`nom_prenom`),
  KEY `idx_categorie` (`categorie`),
  KEY `idx_poste` (`poste_principal`),
  KEY `idx_blesse` (`est_blesse`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueur`
--

LOCK TABLES `joueur` WRITE;
/*!40000 ALTER TABLE `joueur` DISABLE KEYS */;
INSERT INTO `joueur` VALUES (1,'Dupont Jean','Senior','France','Milieu','Droit',180,75.50,'1990-05-15',50,40,10,3600,15,10,2,0,0,NULL,NULL,NULL,NULL,NULL,''),(2,'Martin Paul','Junior','France','Défenseur central droit','Gauche',185,80.00,'2002-03-10',30,25,5,2700,5,3,1,0,0,NULL,NULL,NULL,NULL,NULL,''),(3,'Durand Luc','Senior','France','Attaquant','Droit',175,70.00,'1995-07-20',60,50,10,4000,25,12,3,1,0,NULL,NULL,NULL,NULL,NULL,''),(4,'Petit Marie','Junior','France','Gardien','Ambidextre',190,85.00,'2004-11-05',20,18,2,1800,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,''),(5,'Bernard Sophie','Senior','France','Arrière gauche','Gauche',165,60.00,'1992-02-25',40,35,5,3200,8,6,2,0,0,NULL,NULL,NULL,NULL,NULL,''),(6,'Morel Julien','Junior','France','Milieu offensif','Droit',195,90.00,'2003-06-15',25,20,5,2000,10,8,1,0,0,NULL,NULL,NULL,NULL,NULL,''),(7,'Simon Claire','Senior','France','Milieu','Gauche',170,65.00,'1991-09-30',55,45,10,3500,12,9,3,1,0,NULL,NULL,NULL,NULL,NULL,''),(8,'Lemoine Hugo','Junior','France','Défenseur central gauche','Droit',180,75.00,'2005-01-12',15,12,3,1200,3,2,0,0,0,NULL,NULL,NULL,NULL,NULL,''),(9,'Roux Emma','Senior','France','Attaquant','Ambidextre',175,68.00,'1993-04-18',65,55,10,4200,30,15,4,1,0,NULL,NULL,NULL,NULL,NULL,''),(10,'Blanc Lucas','Junior','France','Gardien','Droit',185,82.00,'2001-08-22',18,15,3,1500,0,0,0,0,0,NULL,NULL,NULL,NULL,NULL,''),(11,'Fontaine Alice','Senior','France','Arrière droit','Gauche',160,55.00,'1994-12-10',45,40,5,3000,6,4,1,0,0,NULL,NULL,NULL,NULL,NULL,''),(12,'Chevalier Thomas','Junior','France','Milieu offensif','Droit',200,95.00,'2006-03-05',10,8,2,800,5,3,0,0,0,NULL,NULL,NULL,NULL,NULL,''),(13,'Garnier Julie','Senior','France','Milieu','Gauche',175,62.00,'1997-05-25',50,45,5,3600,18,12,2,0,0,NULL,NULL,NULL,NULL,NULL,''),(14,'Lambert Antoine','Junior','France','Défenseur central droit','Droit',180,78.00,'2000-10-10',35,30,5,2500,7,5,1,0,0,NULL,NULL,NULL,NULL,NULL,''),(15,'Girard Camille','Senior','France','Attaquant','Ambidextre',170,63.00,'1996-07-07',70,60,10,4500,35,20,5,2,0,NULL,NULL,NULL,NULL,NULL,'');
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

-- Dump completed on 2025-04-15 20:42:54
