-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: crimesdb
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favorites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `updated_at` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_favorites_users_idx` (`user_id`),
  CONSTRAINT `fk_favorites_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
INSERT INTO `favorites` VALUES (19,'Sherry\'s Work','2016-09-02 01:14:01',8,'Cisco Meraki, Terry A Francois Boulevard, San Francisco, CA, United States','2016-09-02 01:14:01'),(20,'Best Sandwiches','2016-09-02 01:15:04',8,'Ike\'s Place, 16th Street, San Francisco, CA, United States','2016-09-02 01:15:04'),(21,'Library','2016-09-02 01:16:45',8,'San Francisco Main Library, Larkin Street, San Francisco, CA, United States','2016-09-02 01:16:45'),(22,'The Fillmore','2016-09-02 01:17:28',8,'The Fillmore, Geary Boulevard, San Francisco, CA, United States','2016-09-02 01:17:28'),(23,'Best Tacos','2016-09-02 01:18:43',8,'Taquerias El Farolito, Mission Street, San Francisco, CA, United States','2016-09-02 01:18:43'),(24,'Exploratorium','2016-09-02 01:21:14',9,'Exploratorium, San Francisco, CA, United States','2016-09-02 01:21:14'),(25,'Let\'s go to the mall!','2016-09-02 01:23:47',9,'Westfield San Francisco Centre, Market Street, San Francisco, CA, United States','2016-09-02 01:54:36');
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pw_hash` varchar(255) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (8,'$2b$12$yyO5QD2DQlv24x.W8U3bg.Fg3owJRV4jIl2n4/mkoFWNjkNNUj5s.','Elliot','elliot@elliot.com','2016-09-02 01:07:43','2016-09-02 01:07:43'),(9,'$2b$12$sxwWoJByxeIGnRTQvh4Iv.bS3Axmm3H285ZnyZEz9/pN9RsDBH.B6','Brandon','brandon@brandon.com','2016-09-02 01:08:02','2016-09-02 01:08:02'),(10,'$2b$12$uX5Zm4g.NAGgUXEwTvAAZul9rBDvDzeLADtz3TyXnuuiUzVYE9yK6','John','jon@jon.com','2016-09-02 01:08:22','2016-09-02 01:08:22'),(11,'$2b$12$q3wsR1uo1nPSLhBWJMKml.a3sJY1SwLvVgpjzhFssJPgxrn6yClp2','Alex','alex@alex.com','2016-09-02 01:08:38','2016-09-02 01:08:38'),(12,'$2b$12$OUn2GpHsentslvAU5aFrwe4/BX5coFKul2knnq/r8LYnPm3qgSIma','Phil','phil@phil.com','2016-09-02 01:09:46','2016-09-02 01:09:46'),(13,'$2b$12$sGGBnBDFQoztgzjKq7qrpenrTrBtWeFuEvT0hNB0HBy2vcYCGDHsC','Sonny','sonny@sonny.com','2016-09-02 01:10:19','2016-09-02 01:10:19'),(14,'$2b$12$CCWmYyWA1a6fcCcsFbIsCO3Ze/2TudFhBWoJ0b5ML.HCw4tGBQ6w6','jag','jag@jag.com','2016-09-02 01:10:44','2016-09-02 01:10:44'),(15,'$2b$12$i74wybnj9U6JX2JziYZ..uq9B4gIzzvf5JunX/2j677CzQeYwXKAi','george','george@george.com','2016-09-02 01:11:33','2016-09-02 01:11:33'),(16,'$2b$12$eGYiUQKgI/dDqRdBRRAc5.eMjVoMp5ouFZemFPk96GkiIfJlSwVAa','lauren','lauren@lauren.com','2016-09-02 01:11:54','2016-09-02 01:11:54');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-02  1:56:40
