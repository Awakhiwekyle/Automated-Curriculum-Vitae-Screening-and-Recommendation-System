-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: localhost    Database: awa
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('f90979a80c37');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applications`
--

DROP TABLE IF EXISTS `applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `application_score` float DEFAULT NULL,
  `created` varchar(50) NOT NULL,
  `applicant_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applications`
--

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;
INSERT INTO `applications` VALUES (124,23,1.40374,'2020-07-10 20:04:05.757807',41),(125,23,1.14089,'2020-07-10 20:05:30.273578',45),(126,23,0.817451,'2020-07-10 20:06:36.227955',33);
/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `education`
--

DROP TABLE IF EXISTS `education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education` (
  `id` int NOT NULL AUTO_INCREMENT,
  `degree` varchar(50) NOT NULL,
  `school` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `fieldOfStudy` varchar(50) NOT NULL,
  `duration` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `created` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education`
--

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;
INSERT INTO `education` VALUES (2,'Bachelors Degree','University of Kwazulu Natal','Durban','Engineering','4','BukhosiDube','2020-07-07 20:05:25.846258'),(3,'Bachelors Degree','Lupane State University','Lupane','Human Resources','48','STshalibe','2020-07-07 20:20:50.238770'),(4,'MSC Degree','Midlands State University','Gweru','Food Science','24','Skhabo','2020-07-07 20:30:10.211127'),(5,'BSC Degree','Midlands State University','Gweru','Food Science','48','Skhabo','2020-07-07 20:30:32.945676'),(7,'Bsc Degree','University of Zimbabwe','Harare','Medicine','60','bbkhabo','2020-07-08 20:37:59.427422'),(8,'Diploma ','Bulawayo Polytechnic','Bulawayo','Information technology','48','Mmoyo','2020-07-08 22:09:13.456832'),(9,'Degree','Midlands State University','Gweru','Bachelors Degree in Telecommunications','48','Mmoyo','2020-07-08 22:09:57.870331'),(11,'Degree','National University Of Science and Technology','Bulawayo','Computer Science','48','akhabo','2020-07-10 20:00:02.011608');
/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employer`
--

DROP TABLE IF EXISTS `employer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `created` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employer`
--

LOCK TABLES `employer` WRITE;
/*!40000 ALTER TABLE `employer` DISABLE KEYS */;
/*!40000 ALTER TABLE `employer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experience`
--

DROP TABLE IF EXISTS `experience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experience` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jobtitle` varchar(50) NOT NULL,
  `company` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `currently` varchar(50) NOT NULL,
  `years` varchar(50) NOT NULL,
  `months` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `username` varchar(50) NOT NULL,
  `created` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experience`
--

LOCK TABLES `experience` WRITE;
/*!40000 ALTER TABLE `experience` DISABLE KEYS */;
INSERT INTO `experience` VALUES (1,'Software engineer','Google','Bulawayo','0','1','3','Backend engineer working on the GCP infrastructure','Nkhumalo','2020-03-19 13:36:24.891914'),(6,'Systems Analyst','Econet Zimbabwe','Bulawayo','','3','1','Systems Analysis\nSDLC\nScrum','BukhosiDube','2020-07-07 20:02:40.818389'),(7,'Senior Developer','MTN SA','Durban','','2','3','Java\nC#\npython\nsql\nmySQL','BukhosiDube','2020-07-07 20:04:22.166305'),(9,'Food Science Lecturer','Bulawayo Polytechnic','Bulawayo','','3','7','Lecturing','Skhabo','2020-07-07 20:27:55.091646'),(10,'Medical Delegate','Nestle Zimbabwe','Bulawayo','1','8','3','Nutrition\nDietetics\nInfant Nutrition','Skhabo','2020-07-07 20:29:03.807145'),(14,'Human Resources Officer','Proton Bakers','Bulawayo','','2','1','Administration, Payroll, Recruitment, Training','Stshalibe','2020-07-07 22:47:32.199759'),(15,'DMO','Ministry of health','Gwanda','','4','2','hospital management','bbkhabo','2020-07-08 20:36:49.403664'),(16,'Computer Technician','Kango','Bulawayo','0','1','1','Networking, N+, Cisco CCNA, Linux, Linux Server, Windows ServerUser support, Hardware, software, windows','Mmoyo','2020-07-08 22:07:24.004461'),(17,'Fleet Management Technician','Sendem transport technologies','Harare','1','2','6','Car  tracking, web, mysql, databases','Mmoyo','2020-07-08 22:08:33.610219'),(20,'Database Officer','World vision','Bulawayo','','1','6','MySQL, Excel, Access, SPSS','akhabo','2020-07-10 19:59:14.418677');
/*!40000 ALTER TABLE `experience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_title` varchar(100) NOT NULL,
  `experience_needed` varchar(50) NOT NULL,
  `skills_needed` varchar(100) NOT NULL,
  `education_needed` varchar(100) NOT NULL,
  `ad_starts` varchar(50) NOT NULL,
  `ad_ends` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `created` varchar(50) NOT NULL,
  `employer_email` varchar(50) NOT NULL,
  `company` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employer_email` (`employer_email`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (19,'Business Analyst','2 years','Business analysis, SAP, M&E, Strategy, Economics','Degree in Business Management, Systems Analysis or Related Field','2020-06-29','2020-07-31','Harare','Zimbabwe','2020-06-29','econetrecruit@econet.co.zw','Business Analyst - Econet Zimbabwe'),(20,'Software Developer','2 years','C#, Python, Web, MVC ASP.NET, Windows Server, Linux','Bachelors Degree in Computer Science or Related Field','2020-07-06','2020-07-20','Bulawayo','Zimbabwe','2020-07-06','softit@gmail.com','Software Developer - Soft-IT Consultants'),(23,'Telecommunications Engineer','2 years','Networking, N+, Cisco CCNA, Linux, Linux Server, Windows Server','Bachelors Degree in Telecommunications other Related fields','2020-07-10','2020-07-24','Bulawayo','Zimbabwe','2020-07-10','econetwireless@econet.co.zw','Telecommunications Engineer - Econet Zimbabwe ');
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `created` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (2,'Nkhumalo','Nkosilathii','Khumalo','+263772333444','nkosi@lathi.com','Bulawayo','Zimbabwe','2020-03-18 20:02:35.268216'),(26,'BukhosiDube','Bukhosi','Dube','0778567654','bukhosidube@gmail.com','Bulawayo','Zimbabwe','2020-07-07 20:01:15.979827'),(28,'Skhabo','Sisa','Khabo','0772756592','sisakhabo@gmail.com','Bulawayo','Zimbabwe','2020-07-06'),(29,'STshalibe','Sibonginkosi','Tshalibe','0773711264','sibonginkositshalibe@gmail.com','Bulawayo','Zimbabwe','2020-07-07 20:24:50.890759'),(30,'bbkhabo','Bekezela Bobbie','Khabo','0772567365','drbkhabo@gmail.com','Harare','Zimbabwe','2020-07-07 22:59:25.507864'),(31,'Mmoyo','Mqondisi','Moyo','0776456534','mqondisimoyo@gmail.com','Bulawayo','Zimbabwe','2020-07-08 22:03:47.698850'),(34,'akhabo','Awakhiwe','Khabo','0772567654','akhabo@gmail.com','Bulawayo','Zimbabwe','2020-07-10 19:58:18.875924');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `skill` varchar(50) NOT NULL,
  `experience` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `created` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (5,'java','2','BukhosiDube','2020-07-07 20:05:48.553161'),(6,'Python','2','BukhosiDube','2020-07-07 20:05:56.653010'),(7,'java script','2','BukhosiDube','2020-07-07 20:06:04.875463'),(8,'Training','2','STshalibe','2020-07-07 20:19:11.070977'),(9,'Payroll','1','STshalibe','2020-07-07 20:19:27.977630'),(10,'SAP','1','Skhabo','2020-07-07 20:30:57.543237'),(11,'Infant Nutrition','3','Skhabo','2020-07-07 20:31:15.080680'),(14,'Medicine','3','bbkhabo','2020-07-08 21:34:12.214035'),(15,'Peadiatrics','3','bbkhabo','2020-07-08 21:34:28.890521'),(19,'Networking','2','mmoyo','2020-07-10 00:05:45.738191'),(20,'N+','2','mmoyo','2020-07-10 00:05:55.599927'),(21,'Cisco CCNA','2','mmoyo','2020-07-10 00:06:06.697799'),(22,'Linux','1','mmoyo','2020-07-10 00:06:42.135680'),(23,'Linux server','1','mmoyo','2020-07-10 00:06:51.350685'),(24,'windows','4','mmoyo','2020-07-10 00:07:01.229683'),(30,'Java','2','akhabo','2020-07-10 20:00:22.065962'),(31,'Python','2','akhabo','2020-07-10 20:00:31.581050'),(32,'C#','4','akhabo','2020-07-10 20:00:40.098921');
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(50) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` varchar(20) DEFAULT NULL,
  `created` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Xavi Alonso','xavi@gmail.com','xavi','12345','user','2020-03-14 18:45:07.245578'),(33,'Bukhosi Dube','bukhosidube@gmail.com','BukhosiDube','admin','user','2020-07-06'),(34,'Sibonginkosi Tshalibe','sibonginkositshalibe@gmail.com','STshalibe','1234','user','2020-07-07 20:12:15.135480'),(37,'Sisa Khabo','sisakhabo@gmail.com','Skhabo','1234','user','2020-07-07 20:26:16.335619'),(38,'Bekezela B Khabo','drbkhabo@gmail.com','BBKhabo','admin','user','2020-07-07 22:58:20.629844'),(39,'Admin Admin','admin@gmail.com','admin','admin','admin','2020-07-08 10:09:40.105392'),(41,'Mqondisi Moyo','mqondisimoyo@gmail.com','Mmoyo','admin','user','2020-07-08 22:01:32.292539'),(45,NULL,'awakhiwekhabo@gmail.com','Akhabo','admin',NULL,'2020-07-10 19:54:53.421910');
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

-- Dump completed on 2020-07-10 23:36:27
