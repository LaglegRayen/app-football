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
-- Temporary view structure for view `evaluation_generale`
--

DROP TABLE IF EXISTS `evaluation_generale`;
/*!50001 DROP VIEW IF EXISTS `evaluation_generale`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `evaluation_generale` AS SELECT 
 1 AS `TYPE`,
 1 AS `Date`,
 1 AS `moyenne_technique`,
 1 AS `moyenne_tactique`,
 1 AS `moyenne_comportementale`,
 1 AS `moyenne_generale`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `evaluation_generale`
--

/*!50001 DROP VIEW IF EXISTS `evaluation_generale`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `evaluation_generale` AS select 'Periode' AS `TYPE`,`e`.`evaluation_date` AS `Date`,`etec`.`moyenne_technique` AS `moyenne_technique`,`etac`.`moyenne_tactique` AS `moyenne_tactique`,`ec`.`moyenne_comportementale` AS `moyenne_comportementale`,`e`.`moyenne_generale` AS `moyenne_generale` from (((`evaluation_sur_periode` `e` join `evaluation_technique` `etec`) join `evaluation_tactique` `etac`) join `evaluation_comportementale` `ec`) where ((`e`.`id_evaluation_technique` = `etec`.`id`) and (`e`.`id_evaluation_tactique` = `etac`.`id`) and (`e`.`id_evaluation_comportementale` = `ec`.`id`) and (`e`.`id_joueur` = 7)) union all select 'Match' AS `TYPE`,`m`.`date_match` AS `Date`,`etec`.`moyenne_technique` AS `moyenne_technique`,`etac`.`moyenne_tactique` AS `moyenne_tactique`,`ec`.`moyenne_comportementale` AS `moyenne_comportementale`,`e`.`moyenne_generale` AS `moyenne_generale` from ((((`evaluation_sur_match` `e` join `evaluation_technique` `etec`) join `evaluation_tactique` `etac`) join `evaluation_comportementale` `ec`) join `matchs` `m`) where ((`e`.`id_evaluation_technique` = `etec`.`id`) and (`e`.`id_evaluation_tactique` = `etac`.`id`) and (`e`.`id_evaluation_comportementale` = `ec`.`id`) and (`e`.`id_match` = `m`.`id`) and (`e`.`id_joueur` = 7)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17  9:14:59
