-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: recruitment
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AppliedJobs`
--

DROP TABLE IF EXISTS `AppliedJobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AppliedJobs` (
  `job_id` varchar(100) NOT NULL,
  `applicant` varchar(150) NOT NULL,
  PRIMARY KEY (`job_id`,`applicant`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppliedJobs`
--

LOCK TABLES `AppliedJobs` WRITE;
/*!40000 ALTER TABLE `AppliedJobs` DISABLE KEYS */;
INSERT INTO `AppliedJobs` VALUES ('2017ucs00572020-12-19 09:04:39.955141','udaramrdc@gmail.com'),('udaramrdc2020-12-17 20:34:02.435124','udaramrdc@gmail.com'),('udaramrdc2020-12-19 08:58:39.158456','udaramrdc@gmail.com');
/*!40000 ALTER TABLE `AppliedJobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Candidate`
--

DROP TABLE IF EXISTS `Candidate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Candidate` (
  `email` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `linkedin` varchar(100) DEFAULT NULL,
  `github` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `experience` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`email`),
  CONSTRAINT `Candidate_ibfk_1` FOREIGN KEY (`email`) REFERENCES `CandidateCredentials` (`email`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Candidate`
--

LOCK TABLES `Candidate` WRITE;
/*!40000 ALTER TABLE `Candidate` DISABLE KEYS */;
INSERT INTO `Candidate` VALUES ('udaramrdc@gmail.com','Udaram Prajapat','7051303387','262ec2dc9b7ee3cdb92399d5941ec824e5212c867ae01a4e44efed8e0bd6d789.jpg','https://www.linkedin.com/in/udaram-prajapat-545ab6159','https://github.com/udaram','Deeplearning Enthausiast','RAMSISAR CHAINANIYA','2-3 years');
/*!40000 ALTER TABLE `Candidate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CandidateCredentials`
--

DROP TABLE IF EXISTS `CandidateCredentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CandidateCredentials` (
  `email` varchar(100) NOT NULL,
  `password` varchar(150) DEFAULT NULL,
  `verification` int DEFAULT (0),
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CandidateCredentials`
--

LOCK TABLES `CandidateCredentials` WRITE;
/*!40000 ALTER TABLE `CandidateCredentials` DISABLE KEYS */;
INSERT INTO `CandidateCredentials` VALUES ('udaramrdc@gmail.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',1);
/*!40000 ALTER TABLE `CandidateCredentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JobDetails`
--

DROP TABLE IF EXISTS `JobDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `JobDetails` (
  `job_id` varchar(100) NOT NULL,
  `postedby` varchar(150) DEFAULT NULL,
  `jobstatus` int DEFAULT '1',
  `applicantscount` int DEFAULT (0),
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JobDetails`
--

LOCK TABLES `JobDetails` WRITE;
/*!40000 ALTER TABLE `JobDetails` DISABLE KEYS */;
INSERT INTO `JobDetails` VALUES ('2017ucs00572020-12-19 09:04:39.955141','2017ucs0057@iitjammu.ac.in',1,0),('udaramrdc2020-12-17 20:29:54.467054','udaramrdc@gmail.com',0,0),('udaramrdc2020-12-17 20:34:02.435124','udaramrdc@gmail.com',1,0),('udaramrdc2020-12-19 08:58:39.158456','udaramrdc@gmail.com',1,0);
/*!40000 ALTER TABLE `JobDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PostedJobs`
--

DROP TABLE IF EXISTS `PostedJobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PostedJobs` (
  `job_id` varchar(100) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `open_date` varchar(15) DEFAULT NULL,
  `close_date` varchar(15) DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  `skills` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`job_id`),
  CONSTRAINT `PostedJobs_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `JobDetails` (`job_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PostedJobs`
--

LOCK TABLES `PostedJobs` WRITE;
/*!40000 ALTER TABLE `PostedJobs` DISABLE KEYS */;
INSERT INTO `PostedJobs` VALUES ('2017ucs00572020-12-19 09:04:39.955141','Agriculture Specialist','Churu','30/12/2020','26/01/2021','Candidate have to work in fields,\r\nknowledge of different agriculture equipment and crop disease needed','agriculture diploma or any degree in agriculture'),('udaramrdc2020-12-17 20:29:54.467054','Research Intern','Jammu','18/12/2020','24/12/2020','1. Research on Computer vision and augmented reality\r\n2. Research on Image depth estimation\r\n3. Image enhancement','Deeplearning, python, Opencv'),('udaramrdc2020-12-17 20:34:02.435124','Software Engineer','Hydrabad','25/12/2020','20/01/2021','1. You will be managing a large database\r\n2. handling the software glitches \r\n3. Handon experience with software lifecycle technologies','Software management,\r\nProeficient in cpp,python or Java'),('udaramrdc2020-12-19 08:58:39.158456','System Engineer','Chandigarh','25/12/2020','31/12/2020','Managing different softwares, Handling client issues and documenting the software','software life cycle and knowledge of c,c++,java');
/*!40000 ALTER TABLE `PostedJobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recruiter`
--

DROP TABLE IF EXISTS `Recruiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Recruiter` (
  `email` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  `experience` varchar(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `linkedin` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`),
  CONSTRAINT `Recruiter_ibfk_1` FOREIGN KEY (`email`) REFERENCES `RecruiterCredentials` (`email`) ON DELETE CASCADE,
  CONSTRAINT `Recruiter_ibfk_2` FOREIGN KEY (`email`) REFERENCES `RecruiterCredentials` (`email`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recruiter`
--

LOCK TABLES `Recruiter` WRITE;
/*!40000 ALTER TABLE `Recruiter` DISABLE KEYS */;
INSERT INTO `Recruiter` VALUES ('2017ucs0057@gmail.com','HANSRAJ PRAJAPAT','TCS Research','7051303387',NULL,NULL,NULL,NULL,NULL),('2017ucs0057@iitjammu.ac.in','HANSRAJ PRAJAPAT','Agro india','7051303387','2-3 years','RAMSISAR CHAINANIYA','Agriculture Analyst','https://www.linkedin.com/in/udaram-prajapat-545ab6159','2017ucs0057@iitjammu.ac.in.jpg'),('udaramrdc@gmail.com','Udaram Prajapat','TCS Research','7051303387','3-5 years','None','Research Intern','None','959189ce46d7a3727e3f90df28b5fb6337aaecaf29f473de55c05e0bdbbab10c.jpg');
/*!40000 ALTER TABLE `Recruiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RecruiterCredentials`
--

DROP TABLE IF EXISTS `RecruiterCredentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RecruiterCredentials` (
  `email` varchar(100) NOT NULL,
  `password` varchar(150) DEFAULT NULL,
  `verification` int DEFAULT (0),
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RecruiterCredentials`
--

LOCK TABLES `RecruiterCredentials` WRITE;
/*!40000 ALTER TABLE `RecruiterCredentials` DISABLE KEYS */;
INSERT INTO `RecruiterCredentials` VALUES ('2017ucs0057@gmail.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',0),('2017ucs0057@iitjammu.ac.in','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',1),('udaramrdc@gmail.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',1);
/*!40000 ALTER TABLE `RecruiterCredentials` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-21 16:26:52
