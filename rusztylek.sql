/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.14-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: rusztylek_test
-- ------------------------------------------------------
-- Server version	10.11.14-MariaDB-0+deb12u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `biegi`
--

DROP TABLE IF EXISTS `biegi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biegi` (
  `id` int(11) NOT NULL,
  `wynik` varchar(8) NOT NULL,
  `kategoria` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biegi`
--

LOCK TABLES `biegi` WRITE;
/*!40000 ALTER TABLE `biegi` DISABLE KEYS */;
/*!40000 ALTER TABLE `biegi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plywanie`
--

DROP TABLE IF EXISTS `plywanie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `plywanie` (
  `id` int(11) NOT NULL,
  `wynik` varchar(8) NOT NULL,
  `kategoria` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plywanie`
--

LOCK TABLES `plywanie` WRITE;
/*!40000 ALTER TABLE `plywanie` DISABLE KEYS */;
/*!40000 ALTER TABLE `plywanie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `runmagedon`
--

DROP TABLE IF EXISTS `runmagedon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `runmagedon` (
  `id` int(11) NOT NULL,
  `wynik` varchar(8) DEFAULT NULL,
  `kategoria` varchar(20) DEFAULT NULL,
  `czasStartu` time DEFAULT NULL,
  `czasMety` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `runmagedon`
--

LOCK TABLES `runmagedon` WRITE;
/*!40000 ALTER TABLE `runmagedon` DISABLE KEYS */;
INSERT INTO `runmagedon` VALUES
(0,'0:29:20','RM_M_2006-2010','00:00:00','00:29:20'),
(1,'0:19:41',NULL,'00:00:30','00:20:11'),
(2,'0:18:34',NULL,'00:01:00','00:19:34'),
(3,'0:21:41',NULL,'00:01:30','00:23:11'),
(4,'0:05:55',NULL,'00:02:00','00:07:55'),
(5,'0:19:08','RM_M_2006-2010','00:02:30','00:21:38'),
(6,'0:10:49',NULL,'00:03:00','00:13:49'),
(7,'0:22:49','RM_M_2006-2010','00:03:30','00:26:19'),
(8,'0:16:58',NULL,'00:04:00','00:20:58'),
(9,'0:27:40',NULL,'00:04:30','00:32:10'),
(10,'0:23:50','RM_M_2006-2010','00:05:00','00:28:50'),
(11,'0:17:34',NULL,'00:05:30','00:23:04'),
(12,'0:05:23',NULL,'00:06:00','00:11:23'),
(13,'0:24:24',NULL,'00:06:30','00:30:54'),
(14,'0:08:12',NULL,'00:07:00','00:15:12'),
(15,'0:11:59',NULL,'00:07:30','00:19:29'),
(16,'0:07:13',NULL,'00:08:00','00:15:13'),
(17,'0:13:33',NULL,'00:08:30','00:22:03'),
(18,'0:18:22','RM_M_2006-2010','00:09:00','00:27:22'),
(19,'0:08:15',NULL,'00:09:30','00:17:45'),
(20,'0:27:36',NULL,'00:10:00','00:37:36'),
(21,'0:17:05',NULL,'00:10:30','00:27:35'),
(22,'0:26:02',NULL,'00:11:00','00:37:02'),
(23,'0:23:27',NULL,'00:11:30','00:34:57'),
(24,'0:26:40',NULL,'00:12:00','00:38:40'),
(25,'0:14:05',NULL,'00:12:30','00:26:35'),
(26,'0:07:05',NULL,'00:13:00','00:20:05'),
(27,'0:30:21',NULL,'00:13:30','00:43:51'),
(28,'0:21:17',NULL,'00:14:00','00:35:17'),
(29,'0:22:02',NULL,'00:14:30','00:36:32'),
(30,'0:07:36','RM_M_2006-2010','00:15:00','00:22:36'),
(31,'0:14:56',NULL,'00:15:30','00:30:26'),
(32,'0:05:00','RM_M_2006-2010','00:16:00','00:21:00'),
(33,'0:15:11',NULL,'00:16:30','00:31:41'),
(34,'0:23:28',NULL,'00:17:00','00:40:28'),
(35,'0:30:11',NULL,'00:17:30','00:47:41'),
(36,'0:17:30',NULL,'00:18:00','00:35:30'),
(37,'0:12:33',NULL,'00:18:30','00:31:03'),
(38,'0:27:27',NULL,'00:19:00','00:46:27'),
(39,'0:09:19',NULL,'00:19:30','00:28:49'),
(40,'0:06:09',NULL,'00:20:00','00:26:09'),
(41,'0:22:28',NULL,'00:20:30','00:42:58'),
(42,'0:16:01','RM_M_2006-2010','00:21:00','00:37:01'),
(43,'0:13:57',NULL,'00:21:30','00:35:27'),
(44,'0:22:35','RM_M_2006-2010','00:22:00','00:44:35'),
(45,'0:17:07',NULL,'00:22:30','00:39:37'),
(46,'0:13:50',NULL,'00:23:00','00:36:50'),
(47,'0:27:51',NULL,'00:23:30','00:51:21'),
(48,'0:26:12','RM_M_2006-2010','00:24:00','00:50:12'),
(49,'0:15:31',NULL,'00:24:30','00:40:01'),
(50,'0:11:15',NULL,'00:25:00','00:36:15'),
(51,'0:09:05',NULL,'00:25:30','00:34:35'),
(52,'0:23:11',NULL,'00:26:00','00:49:11'),
(53,'0:10:07',NULL,'00:26:30','00:36:37'),
(54,'0:24:13',NULL,'00:27:00','00:51:13'),
(55,'0:29:40',NULL,'00:27:30','00:57:10'),
(56,'0:09:11',NULL,'00:28:00','00:37:11'),
(57,'0:13:42',NULL,'00:28:30','00:42:12'),
(58,'0:25:29',NULL,'00:29:00','00:54:29'),
(59,'0:14:29','RM_M_2006-2010','00:29:30','00:43:59'),
(60,'0:05:17','RM_M_2006-2010','00:30:00','00:35:17'),
(61,'0:12:59','RM_M_2006-2010','00:30:30','00:43:29'),
(62,'0:20:35','RM_M_2006-2010','00:31:00','00:51:35'),
(63,'0:23:41','RM_M_2006-2010','00:31:30','00:55:11'),
(64,'0:24:08','RM_M_2006-2010','00:32:00','00:56:08'),
(65,'0:14:11',NULL,'00:32:30','00:46:41'),
(66,'0:30:24',NULL,'00:33:00','01:03:24'),
(67,'0:29:22',NULL,'00:33:30','01:02:52'),
(68,'0:13:16',NULL,'00:34:00','00:47:16'),
(69,'0:05:27',NULL,'00:34:30','00:39:57'),
(70,'0:13:17',NULL,'00:35:00','00:48:17'),
(71,'0:13:57',NULL,'00:35:30','00:49:27'),
(72,'0:14:06','RM_M_2006-2010','00:36:00','00:50:06'),
(73,'0:26:12',NULL,'00:36:30','01:02:42'),
(74,'0:17:30','RM_M_2006-2010','00:37:00','00:54:30'),
(75,'0:20:52','RM_M_2006-2010','00:37:30','00:58:22'),
(76,'0:20:20',NULL,'00:38:00','00:58:20'),
(77,'0:09:37',NULL,'00:38:30','00:48:07'),
(78,'0:14:34',NULL,'00:39:00','00:53:34'),
(79,'0:30:52','RM_M_2006-2010','00:39:30','01:10:22'),
(80,'0:24:19',NULL,'00:40:00','01:04:19'),
(81,'0:25:18',NULL,'00:40:30','01:05:48'),
(82,'0:19:39',NULL,'00:41:00','01:00:39'),
(83,'0:05:11',NULL,'00:41:30','00:46:41'),
(84,'0:13:30','RM_M_2006-2010','00:42:00','00:55:30'),
(85,'0:07:28',NULL,'00:42:30','00:49:58'),
(86,'0:20:32',NULL,'00:43:00','01:03:32'),
(87,'0:10:32','RM_M_2006-2010','00:43:30','00:54:02'),
(88,'0:22:35',NULL,'00:44:00','01:06:35'),
(89,'0:10:31',NULL,'00:44:30','00:55:01'),
(90,'0:27:40',NULL,'00:45:00','01:12:40'),
(91,'0:26:00',NULL,'00:45:30','01:11:30'),
(92,'0:26:51','RM_M_2006-2010','00:46:00','01:12:51'),
(93,'0:29:31',NULL,'00:46:30','01:16:01'),
(94,'0:20:37',NULL,'00:47:00','01:07:37'),
(95,'0:30:44',NULL,'00:47:30','01:18:14'),
(96,'0:18:29',NULL,'00:48:00','01:06:29'),
(97,'0:19:16',NULL,'00:48:30','01:07:46'),
(98,'0:18:07',NULL,'00:49:00','01:07:07'),
(99,'0:27:01',NULL,'00:49:30','01:16:31'),
(100,'0:30:15',NULL,'00:50:00','01:20:15'),
(101,'0:18:15','RM_M_2006-2010','00:50:30','01:08:45'),
(102,'0:29:06',NULL,'00:51:00','01:20:06'),
(103,'0:20:11','RM_M_2006-2010','00:51:30','01:11:41'),
(104,'0:05:35',NULL,'00:52:00','00:57:35'),
(105,'0:25:14',NULL,'00:52:30','01:17:44'),
(106,'0:10:45',NULL,'00:53:00','01:03:45'),
(107,'0:25:31',NULL,'00:53:30','01:19:01'),
(108,'0:15:54',NULL,'00:54:00','01:09:54'),
(109,'0:06:47','RM_M_2006-2010','00:54:30','01:01:17'),
(110,'0:17:44',NULL,'00:55:00','01:12:44'),
(111,'0:07:38',NULL,'00:55:30','01:03:08'),
(112,'0:09:22',NULL,'00:56:00','01:05:22'),
(113,'0:06:32',NULL,'00:56:30','01:03:02'),
(114,'0:11:26',NULL,'00:57:00','01:08:26'),
(115,'0:16:28',NULL,'00:57:30','01:13:58'),
(116,'0:22:00',NULL,'00:58:00','01:20:00'),
(117,'0:12:02',NULL,'00:58:30','01:10:32'),
(118,'0:14:11',NULL,'00:59:00','01:13:11'),
(119,'0:10:16',NULL,'00:59:30','01:09:46'),
(120,'0:16:31',NULL,'01:00:00','01:16:31'),
(121,'0:12:37','RM_M_2006-2010','01:00:30','01:13:07'),
(122,'0:10:11',NULL,'01:01:00','01:11:11'),
(123,'0:11:56','RM_M_2006-2010','01:01:30','01:13:26'),
(124,'0:14:08',NULL,'01:02:00','01:16:08'),
(125,'0:06:42',NULL,'01:02:30','01:09:12'),
(126,'0:13:14',NULL,'01:03:00','01:16:14'),
(127,'0:17:01',NULL,'01:03:30','01:20:31'),
(128,'0:26:46',NULL,'01:04:00','01:30:46'),
(129,'0:11:18','RM_M_2006-2010','01:04:30','01:15:48'),
(130,'0:21:10',NULL,'01:05:00','01:26:10'),
(131,'0:25:00',NULL,'01:05:30','01:30:30'),
(132,'0:12:00',NULL,'01:06:00','01:18:00'),
(133,'0:12:41',NULL,'01:06:30','01:19:11'),
(134,'0:11:42',NULL,'01:07:00','01:18:42'),
(135,'0:10:26',NULL,'01:07:30','01:17:56'),
(136,'0:21:27',NULL,'01:08:00','01:29:27'),
(137,'0:28:56','RM_M_2006-2010','01:08:30','01:37:26'),
(138,'0:19:01',NULL,'01:09:00','01:28:01'),
(139,'0:10:24',NULL,'01:09:30','01:19:54'),
(140,'0:14:19',NULL,'01:10:00','01:24:19'),
(141,'0:12:07','RM_M_2006-2010','01:10:30','01:22:37'),
(142,'0:30:07',NULL,'01:11:00','01:41:07'),
(143,'0:16:07',NULL,'01:11:30','01:27:37'),
(144,'0:06:50',NULL,'01:12:00','01:18:50'),
(145,'0:27:00',NULL,'01:12:30','01:39:30'),
(146,'0:30:14',NULL,'01:13:00','01:43:14'),
(147,'0:27:18',NULL,'01:13:30','01:40:48'),
(148,'0:05:35',NULL,'01:14:00','01:19:35'),
(149,'0:18:57',NULL,'01:14:30','01:33:27'),
(150,'0:28:49',NULL,'01:15:00','01:43:49'),
(151,'0:30:56','RM_M_2006-2010','01:15:30','01:46:26'),
(152,'0:28:02',NULL,'01:16:00','01:44:02'),
(153,'0:12:05',NULL,'01:16:30','01:28:35'),
(154,'0:14:47',NULL,'01:17:00','01:31:47'),
(155,'0:20:06',NULL,'01:17:30','01:37:36'),
(156,'0:15:07',NULL,'01:18:00','01:33:07'),
(157,'0:19:07',NULL,'01:18:30','01:37:37'),
(158,'0:22:55','RM_M_2006-2010','01:19:00','01:41:55'),
(159,'0:15:20','RM_M_2006-2010','01:19:30','01:34:50'),
(160,'0:19:14',NULL,'01:20:00','01:39:14'),
(161,'0:26:44',NULL,'01:20:30','01:47:14'),
(162,'0:11:46',NULL,'01:21:00','01:32:46'),
(163,'0:16:16',NULL,'01:21:30','01:37:46'),
(164,'0:18:16',NULL,'01:22:00','01:40:16'),
(165,'0:05:20',NULL,'01:22:30','01:27:50'),
(166,'0:05:09','RM_M_2006-2010','01:23:00','01:28:09'),
(167,'0:27:28',NULL,'01:23:30','01:50:58'),
(168,'0:07:30',NULL,'01:24:00','01:31:30'),
(169,'0:29:24',NULL,'01:24:30','01:53:54'),
(170,'0:13:33',NULL,'01:25:00','01:38:33'),
(171,'0:20:16',NULL,'01:25:30','01:45:46'),
(172,'0:30:20',NULL,'01:26:00','01:56:20'),
(173,'0:06:49',NULL,'01:26:30','01:33:19'),
(174,'0:27:33',NULL,'01:27:00','01:54:33'),
(175,'0:09:56',NULL,'01:27:30','01:37:26'),
(176,'0:15:44','RM_M_2006-2010','01:28:00','01:43:44'),
(177,'0:29:03',NULL,'01:28:30','01:57:33'),
(178,'0:28:06',NULL,'01:29:00','01:57:06'),
(179,'0:11:49',NULL,'01:29:30','01:41:19'),
(180,'0:23:07',NULL,'01:30:00','01:53:07'),
(181,'0:13:21',NULL,'01:30:30','01:43:51'),
(182,'0:07:33',NULL,'01:31:00','01:38:33'),
(183,'0:18:01',NULL,'01:31:30','01:49:31'),
(184,'0:22:52','RM_M_2006-2010','01:32:00','01:54:52'),
(185,'0:10:29','RM_M_2006-2010','01:32:30','01:42:59'),
(186,'0:30:09',NULL,'01:33:00','02:03:09'),
(187,'0:18:57',NULL,'01:33:30','01:52:27'),
(188,'0:21:32',NULL,'01:34:00','01:55:32'),
(189,'0:25:32','RM_M_2006-2010','01:34:30','02:00:02'),
(190,'0:10:08',NULL,'01:35:00','01:45:08'),
(191,'0:14:24',NULL,'01:35:30','01:49:54'),
(192,'0:07:35',NULL,'01:36:00','01:43:35'),
(193,'0:26:03',NULL,'01:36:30','02:02:33'),
(194,'0:23:09','RM_M_2006-2010','01:37:00','02:00:09'),
(195,'0:26:25',NULL,'01:37:30','02:03:55'),
(196,'0:05:18',NULL,'01:38:00','01:43:18'),
(197,'0:22:37',NULL,'01:38:30','02:01:07'),
(198,'0:23:30',NULL,'01:39:00','02:02:30'),
(199,'0:26:08','RM_M_2006-2010','01:39:30','02:05:38'),
(200,'0:06:38',NULL,'01:40:00','01:46:38'),
(201,'0:08:37',NULL,'01:40:30','01:49:07'),
(202,'0:08:17',NULL,'01:41:00','01:49:17'),
(203,'0:22:37',NULL,'01:41:30','02:04:07'),
(204,'0:09:51',NULL,'01:42:00','01:51:51'),
(205,'0:24:19',NULL,'01:42:30','02:06:49'),
(206,'0:28:15','RM_M_2006-2010','01:43:00','02:11:15'),
(207,'0:12:32',NULL,'01:43:30','01:56:02'),
(208,'0:25:52',NULL,'01:44:00','02:09:52'),
(209,'0:11:27',NULL,'01:44:30','01:55:57'),
(210,'0:27:45',NULL,'01:45:00','02:12:45'),
(211,'0:06:02',NULL,'01:45:30','01:51:32'),
(212,'0:25:02',NULL,'01:46:00','02:11:02'),
(213,'0:17:20',NULL,'01:46:30','02:03:50'),
(214,'0:13:42',NULL,'01:47:00','02:00:42'),
(215,'0:06:59',NULL,'01:47:30','01:54:29'),
(216,'0:17:19',NULL,'01:48:00','02:05:19'),
(217,'0:24:12',NULL,'01:48:30','02:12:42'),
(218,'0:05:53','RM_M_2006-2010','01:49:00','01:54:53'),
(219,'0:30:21',NULL,'01:49:30','02:19:51'),
(220,'0:18:59',NULL,'01:50:00','02:08:59'),
(221,'0:17:02',NULL,'01:50:30','02:07:32'),
(222,'0:13:32',NULL,'01:51:00','02:04:32'),
(223,'0:09:28',NULL,'01:51:30','02:00:58'),
(224,'0:25:21','RM_M_2006-2010','01:52:00','02:17:21'),
(225,'0:05:17',NULL,'01:52:30','01:57:47'),
(226,'0:11:50','RM_M_2006-2010','01:53:00','02:04:50'),
(227,'0:22:07',NULL,'01:53:30','02:15:37'),
(228,'0:28:12',NULL,'01:54:00','02:22:12'),
(229,'0:24:15','RM_M_2006-2010','01:54:30','02:18:45'),
(230,'0:12:31','RM_M_2006-2010','01:55:00','02:07:31'),
(231,'0:19:15',NULL,'01:55:30','02:14:45'),
(232,'0:06:02','RM_M_2006-2010','01:56:00','02:02:02'),
(233,'0:30:35','RM_M_2006-2010','01:56:30','02:27:05'),
(234,'0:30:10','RM_M_2006-2010','01:57:00','02:27:10'),
(235,'0:29:20',NULL,'01:57:30','02:26:50'),
(236,'0:20:05',NULL,'01:58:00','02:18:05'),
(237,'0:28:32',NULL,'01:58:30','02:27:02'),
(238,'0:23:53',NULL,'01:59:00','02:22:53'),
(239,'0:16:52',NULL,'01:59:30','02:16:22'),
(240,'0:23:29','RM_M_2006-2010','02:00:00','02:23:29'),
(241,'0:22:31',NULL,'02:00:30','02:23:01'),
(242,'0:13:04',NULL,'02:01:00','02:14:04'),
(243,'0:15:58',NULL,'02:01:30','02:17:28'),
(244,'0:27:01',NULL,'02:02:00','02:29:01'),
(245,'0:05:12',NULL,'02:02:30','02:07:42'),
(246,'0:27:17',NULL,'02:03:00','02:30:17');
/*!40000 ALTER TABLE `runmagedon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uczestnik`
--

DROP TABLE IF EXISTS `uczestnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `uczestnik` (
  `id` int(10) unsigned NOT NULL,
  `imie` varchar(50) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `dataUrodzenia` date NOT NULL,
  `plec` varchar(20) NOT NULL,
  `imieObozowe` varchar(50) DEFAULT NULL,
  `turnus` int(11) NOT NULL,
  `wychowawca` int(11) DEFAULT NULL,
  `pierwszyRaz` varchar(3) NOT NULL,
  `leki` varchar(3) NOT NULL,
  `plywanie` int(11) DEFAULT NULL,
  `biegi` int(11) DEFAULT NULL,
  `runmagedon` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `plywanie` (`plywanie`),
  KEY `biegi` (`biegi`),
  KEY `runmagedon` (`runmagedon`),
  KEY `wychowawca` (`wychowawca`),
  CONSTRAINT `uczestnik_ibfk_1` FOREIGN KEY (`runmagedon`) REFERENCES `runmagedon` (`id`),
  CONSTRAINT `uczestnik_ibfk_2` FOREIGN KEY (`biegi`) REFERENCES `biegi` (`id`),
  CONSTRAINT `uczestnik_ibfk_3` FOREIGN KEY (`plywanie`) REFERENCES `plywanie` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uczestnik`
--

LOCK TABLES `uczestnik` WRITE;
/*!40000 ALTER TABLE `uczestnik` DISABLE KEYS */;
INSERT INTO `uczestnik` VALUES
(0,'Przemysław','Andrzejewski','2006-10-16','Mężczyzna','Mroczny Trzciny',1,10,'tak','Tak',NULL,NULL,0),
(1,'Franciszek','Baran','2011-05-29','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,1),
(2,'Ignacy','Baran','2014-10-21','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,2),
(3,'Lena','Baran','2013-04-22','Kobieta','Wodny Mewa',1,2,'tak','Nie',NULL,NULL,3),
(4,'Dorota','Bąk','2010-01-19','Kobieta','Szumiący Trzciny',1,2,'tak','Nie',NULL,NULL,4),
(5,'Mikołaj','Bąk','2009-01-12','Mężczyzna',NULL,1,4,'nie','Tak',NULL,NULL,5),
(6,'Barbara','Bielawski','2019-06-09','Kobieta','Skryty Fale',1,10,'tak','Tak',NULL,NULL,6),
(7,'Igor','Bielawski','2009-12-07','Mężczyzna',NULL,1,3,'nie','Tak',NULL,NULL,7),
(8,'Lena','Bielawski','2013-08-31','Kobieta','Szumiący Głębina',1,4,'tak','Nie',NULL,NULL,8),
(9,'Stanisław','Bielawski','2011-08-07','Mężczyzna',NULL,1,7,'nie','Nie',NULL,NULL,9),
(10,'Bartosz','Borkowski','2010-08-06','Mężczyzna','Krystaliczny Sitowie',1,8,'tak','Tak',NULL,NULL,10),
(11,'Julia','Borkowski','2008-06-21','Kobieta','Jeziorny Mewa',1,2,'tak','Tak',NULL,NULL,11),
(12,'Leonard','Borkowski','2011-10-04','Mężczyzna',NULL,1,8,'nie','Tak',NULL,NULL,12),
(13,'Sabina','Borkowski','2006-03-04','Kobieta',NULL,1,7,'nie','Tak',NULL,NULL,13),
(14,'Halina','Brzeziński','2012-12-20','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,14),
(15,'Jan','Brzeziński','2014-07-29','Mężczyzna',NULL,1,2,'nie','Tak',NULL,NULL,15),
(16,'Róża','Brzeziński','2007-11-09','Kobieta',NULL,1,10,'nie','Nie',NULL,NULL,16),
(17,'Stefan','Brzeziński','2019-12-30','Mężczyzna','Mglisty Brzeg',1,2,'tak','Nie',NULL,NULL,17),
(18,'Jan','Błaszczyk','2006-02-15','Mężczyzna',NULL,1,10,'nie','Tak',NULL,NULL,18),
(19,'Mikołaj','Błaszczyk','2013-04-28','Mężczyzna',NULL,1,2,'nie','Tak',NULL,NULL,19),
(20,'Przemysław','Błaszczyk','2014-02-26','Mężczyzna',NULL,1,6,'nie','Nie',NULL,NULL,20),
(21,'Grzegorz','Chmielewski','2019-05-16','Mężczyzna',NULL,1,10,'nie','Nie',NULL,NULL,21),
(22,'Gustaw','Chmielewski','2017-05-20','Mężczyzna',NULL,1,8,'nie','Nie',NULL,NULL,22),
(23,'Celina','Ciesielski','2019-08-08','Kobieta','Jeziorny Żuraw',1,6,'tak','Nie',NULL,NULL,23),
(24,'Emil','Ciesielski','2018-02-16','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,24),
(25,'Katarzyna','Ciesielski','2008-01-09','Kobieta',NULL,1,8,'nie','Nie',NULL,NULL,25),
(26,'Karol','Czajkowski','2014-05-24','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,26),
(27,'Lech','Czerwiński','2011-02-25','Mężczyzna',NULL,1,1,'nie','Tak',NULL,NULL,27),
(28,'Alicja','Gajewski','2011-04-27','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,28),
(29,'Henryk','Gajewski','2015-06-28','Mężczyzna','Cichy Perkoz',1,6,'tak','Tak',NULL,NULL,29),
(30,'Igor','Gajewski','2009-12-20','Mężczyzna',NULL,1,2,'nie','Nie',NULL,NULL,30),
(31,'Julia','Gajewski','2007-12-31','Kobieta','Tęczowy Rybak',1,7,'tak','Tak',NULL,NULL,31),
(32,'Leszek','Gajewski','2008-05-26','Mężczyzna',NULL,1,7,'nie','Nie',NULL,NULL,32),
(33,'Natalia','Góra','2006-09-05','Kobieta',NULL,1,4,'nie','Tak',NULL,NULL,33),
(34,'Halina','Górski','2018-03-08','Kobieta',NULL,1,6,'nie','Nie',NULL,NULL,34),
(35,'Karol','Górski','2017-06-18','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,35),
(36,'Lech','Górski','2012-03-12','Mężczyzna',NULL,1,7,'nie','Nie',NULL,NULL,36),
(37,'Monika','Górski','2014-07-25','Kobieta',NULL,1,7,'nie','Tak',NULL,NULL,37),
(38,'Tomasz','Górski','2012-12-19','Mężczyzna','Mglisty Rybak',1,7,'tak','Nie',NULL,NULL,38),
(39,'Beata','Grabowski','2010-09-22','Kobieta','Skryty Głębina',1,3,'tak','Nie',NULL,NULL,39),
(40,'Marlena','Grabowski','2011-01-17','Kobieta',NULL,1,1,'nie','Nie',NULL,NULL,40),
(41,'Agnieszka','Głowacki','2006-12-02','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,41),
(42,'Leszek','Głowacki','2008-11-27','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,42),
(43,'Maria','Głowacki','2014-07-31','Kobieta',NULL,1,4,'nie','Nie',NULL,NULL,43),
(44,'Henryk','Jabłoński','2007-04-24','Mężczyzna',NULL,1,9,'nie','Nie',NULL,NULL,44),
(45,'Lucyna','Jabłoński','2017-04-19','Kobieta',NULL,1,3,'nie','Nie',NULL,NULL,45),
(46,'Adam','Jakubowski','2013-10-04','Mężczyzna','Szumiący Zatoka',1,8,'tak','Nie',NULL,NULL,46),
(47,'Dominik','Jakubowski','2013-02-03','Mężczyzna',NULL,1,8,'nie','Nie',NULL,NULL,47),
(48,'Paweł','Jakubowski','2008-02-05','Mężczyzna','Dziki Brzeg',1,5,'tak','Tak',NULL,NULL,48),
(49,'Wiktoria','Jakubowski','2015-09-09','Kobieta',NULL,1,6,'nie','Tak',NULL,NULL,49),
(50,'Łucja','Jankowski','2015-11-13','Kobieta','Tęczowy Fale',1,3,'tak','Tak',NULL,NULL,50),
(51,'Agnieszka','Kacprzak','2013-06-18','Kobieta',NULL,1,1,'tak','Nie',NULL,NULL,51),
(52,'Emil','Kacprzak','2015-05-16','Mężczyzna','Zielony Trzciny',1,6,'tak','Nie',NULL,NULL,52),
(53,'Franciszek','Kacprzak','2011-10-28','Mężczyzna','Dziki Perkoz',1,10,'tak','Tak',NULL,NULL,53),
(54,'Kacper','Kacprzak','2018-04-02','Mężczyzna',NULL,1,5,'nie','Nie',NULL,NULL,54),
(55,'Ewa','Kaczmarczyk','2011-12-13','Kobieta',NULL,1,2,'nie','Tak',NULL,NULL,55),
(56,'Natalia','Kaczmarczyk','2015-04-15','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,56),
(57,'Cezary','Kaczmarek','2013-05-25','Mężczyzna',NULL,1,9,'nie','Tak',NULL,NULL,57),
(58,'Halina','Kaczmarek','2008-08-18','Kobieta',NULL,1,3,'nie','Tak',NULL,NULL,58),
(59,'Paweł','Kaczmarek','2007-05-24','Mężczyzna','Kamienny Sitowie',1,3,'tak','Tak',NULL,NULL,59),
(60,'Radosław','Kaczmarek','2008-01-20','Mężczyzna','Leśny Zatoka',1,4,'tak','Nie',NULL,NULL,60),
(61,'Łukasz','Kaczmarek','2010-04-06','Mężczyzna','Dziki Żuraw',1,8,'tak','Nie',NULL,NULL,61),
(62,'Jarosław','Kaczor','2008-04-16','Mężczyzna','Mglisty Łabędź',1,6,'tak','Nie',NULL,NULL,62),
(63,'Kazimierz','Kaczor','2010-12-24','Mężczyzna',NULL,1,10,'nie','Tak',NULL,NULL,63),
(64,'Kazimierz','Kaczor','2007-07-27','Mężczyzna','Wietrzny Sitowie',1,8,'tak','Nie',NULL,NULL,64),
(65,'Stefan','Kaczor','2012-09-11','Mężczyzna',NULL,1,9,'nie','Tak',NULL,NULL,65),
(66,'Wiktoria','Kaczor','2006-12-10','Kobieta',NULL,1,1,'nie','Tak',NULL,NULL,66),
(67,'Lidia','Kalinowski','2014-11-18','Kobieta',NULL,1,1,'tak','Nie',NULL,NULL,67),
(68,'Lucyna','Kalinowski','2007-10-05','Kobieta','Wodny Żuraw',1,9,'tak','Tak',NULL,NULL,68),
(69,'Sabina','Kalinowski','2007-01-18','Kobieta',NULL,1,8,'nie','Tak',NULL,NULL,69),
(70,'Łukasz','Kalinowski','2019-04-03','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,70),
(71,'Elżbieta','Kamiński','2006-11-12','Kobieta',NULL,1,10,'nie','Nie',NULL,NULL,71),
(72,'Kazimierz','Konieczny','2008-07-14','Mężczyzna','Błotny Żeglarz',1,5,'tak','Tak',NULL,NULL,72),
(73,'Bogusław','Kostrzewa','2015-07-20','Mężczyzna','Wodny Pomost',1,9,'tak','Tak',NULL,NULL,73),
(74,'Bogusław','Kot','2006-05-19','Mężczyzna','Wietrzny Łabędź',1,6,'tak','Nie',NULL,NULL,74),
(75,'Gustaw','Kot','2009-04-20','Mężczyzna',NULL,1,5,'nie','Nie',NULL,NULL,75),
(76,'Marta','Kot','2013-02-18','Kobieta','Cichy Poranek',1,6,'tak','Nie',NULL,NULL,76),
(77,'Beata','Kowalczyk','2016-12-30','Kobieta','Błękitny Łabędź',1,3,'tak','Nie',NULL,NULL,77),
(78,'Ewa','Kowalski','2016-10-10','Kobieta',NULL,1,10,'nie','Nie',NULL,NULL,78),
(79,'Natan','Kowalski','2007-05-21','Mężczyzna','Błotny Żeglarz',1,4,'tak','Nie',NULL,NULL,79),
(80,'Norbert','Kowalski','2016-06-21','Mężczyzna','Złoty Wodnik',1,10,'tak','Tak',NULL,NULL,80),
(81,'Daniel','Kozak','2016-04-13','Mężczyzna',NULL,1,1,'nie','Tak',NULL,NULL,81),
(82,'Kinga','Kozak','2015-03-20','Kobieta','Skryty Rybak',1,8,'tak','Nie',NULL,NULL,82),
(83,'Marta','Kozak','2012-11-28','Kobieta',NULL,1,8,'nie','Nie',NULL,NULL,83),
(84,'Łukasz','Kozieł','2010-04-16','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,84),
(85,'Elżbieta','Kozłowski','2014-02-11','Kobieta',NULL,1,5,'nie','Nie',NULL,NULL,85),
(86,'Ewa','Kozłowski','2017-07-30','Kobieta','Kamienny Szczupak',1,8,'tak','Tak',NULL,NULL,86),
(87,'Mirosław','Kozłowski','2010-10-01','Mężczyzna','Złoty Rybak',1,6,'tak','Tak',NULL,NULL,87),
(88,'Wiktoria','Kozłowski','2009-07-12','Kobieta',NULL,1,2,'nie','Tak',NULL,NULL,88),
(89,'Gabriela','Krawczyk','2019-05-20','Kobieta',NULL,1,7,'nie','Nie',NULL,NULL,89),
(90,'Gabriela','Krawczyk','2006-06-09','Kobieta',NULL,1,10,'nie','Nie',NULL,NULL,90),
(91,'Barbara','Kruk','2009-05-03','Kobieta','Cichy Pływak',1,7,'tak','Nie',NULL,NULL,91),
(92,'Emil','Kruk','2010-04-17','Mężczyzna',NULL,1,9,'nie','Tak',NULL,NULL,92),
(93,'Halina','Kruk','2006-08-12','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,93),
(94,'Janina','Kubiak','2017-10-27','Kobieta',NULL,1,9,'nie','Tak',NULL,NULL,94),
(95,'Mirosław','Kubiak','2019-09-17','Mężczyzna','Piaskowy Szczupak',1,10,'tak','Nie',NULL,NULL,95),
(96,'Oliwia','Kubiak','2012-07-19','Kobieta',NULL,1,9,'nie','Nie',NULL,NULL,96),
(97,'Robert','Kubiak','2011-07-11','Mężczyzna','Jeziorny Pomost',1,4,'tak','Tak',NULL,NULL,97),
(98,'Agnieszka','Kurek','2006-04-14','Kobieta',NULL,1,9,'nie','Nie',NULL,NULL,98),
(99,'Bogdan','Kurek','2017-01-28','Mężczyzna',NULL,1,8,'nie','Nie',NULL,NULL,99),
(100,'Eryk','Kurek','2012-01-31','Mężczyzna','Złoty Mewa',1,6,'tak','Tak',NULL,NULL,100),
(101,'Szymon','Kurek','2006-01-03','Mężczyzna',NULL,1,3,'nie','Tak',NULL,NULL,101),
(102,'Andrzej','Kwiatkowski','2018-01-10','Mężczyzna',NULL,1,5,'nie','Tak',NULL,NULL,102),
(103,'Hubert','Kwiatkowski','2007-07-06','Mężczyzna','Mglisty Karp',1,5,'tak','Tak',NULL,NULL,103),
(104,'Magdalena','Kwiatkowski','2016-08-20','Kobieta',NULL,1,1,'nie','Tak',NULL,NULL,104),
(105,'Mikołaj','Kwiatkowski','2013-10-29','Mężczyzna',NULL,1,8,'nie','Nie',NULL,NULL,105),
(106,'Bogdan','Lewandowski','2018-09-16','Mężczyzna',NULL,1,9,'nie','Tak',NULL,NULL,106),
(107,'Kinga','Lewandowski','2019-02-03','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,107),
(108,'Lucjan','Lipiński','2018-11-14','Mężczyzna',NULL,1,7,'nie','Nie',NULL,NULL,108),
(109,'Mieczysław','Lipiński','2010-04-06','Mężczyzna','Słoneczny Rybak',1,5,'tak','Nie',NULL,NULL,109),
(110,'Agnieszka','Malinowski','2008-06-16','Kobieta',NULL,1,7,'nie','Nie',NULL,NULL,110),
(111,'Agnieszka','Malinowski','2008-05-30','Kobieta','Dziki Głębina',1,7,'tak','Tak',NULL,NULL,111),
(112,'Daniel','Malinowski','2012-08-03','Mężczyzna',NULL,1,10,'nie','Tak',NULL,NULL,112),
(113,'Jerzy','Malinowski','2014-02-08','Mężczyzna',NULL,1,2,'nie','Nie',NULL,NULL,113),
(114,'Magdalena','Marcinek','2013-02-03','Kobieta','Skryty Głębina',1,8,'tak','Tak',NULL,NULL,114),
(115,'Sabina','Marcinek','2015-08-04','Kobieta',NULL,1,2,'nie','Tak',NULL,NULL,115),
(116,'Stefan','Marcinek','2014-12-08','Mężczyzna',NULL,1,5,'nie','Tak',NULL,NULL,116),
(117,'Iwona','Marciniak','2009-11-21','Kobieta','Dziki Brzeg',1,2,'tak','Nie',NULL,NULL,117),
(118,'Sabina','Marciniak','2007-05-21','Kobieta','Krystaliczny Pływak',1,10,'tak','Nie',NULL,NULL,118),
(119,'Bartosz','Mazur','2017-10-13','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,119),
(120,'Magdalena','Mazur','2008-02-06','Kobieta','Srebrny Karp',1,5,'tak','Nie',NULL,NULL,120),
(121,'Bartosz','Mazurek','2007-11-03','Mężczyzna','Zielony Mewa',1,2,'tak','Tak',NULL,NULL,121),
(122,'Stanisław','Michalak','2016-05-30','Mężczyzna',NULL,1,6,'nie','Nie',NULL,NULL,122),
(123,'Marcin','Michałowski','2009-11-02','Mężczyzna',NULL,1,2,'nie','Nie',NULL,NULL,123),
(124,'Emil','Mikołajczyk','2014-07-13','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,124),
(125,'Irena','Mikołajczyk','2006-10-10','Kobieta',NULL,1,2,'nie','Nie',NULL,NULL,125),
(126,'Magdalena','Mikołajczyk','2010-06-02','Kobieta',NULL,1,1,'nie','Nie',NULL,NULL,126),
(127,'Paweł','Mikołajczyk','2015-09-01','Mężczyzna',NULL,1,2,'nie','Tak',NULL,NULL,127),
(128,'Emilia','Nowacki','2013-08-02','Kobieta','Tęczowy Żeglarz',1,4,'tak','Nie',NULL,NULL,128),
(129,'Kacper','Nowacki','2009-09-03','Mężczyzna','Wietrzny Sitowie',1,4,'tak','Nie',NULL,NULL,129),
(130,'Magdalena','Nowacki','2007-03-26','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,130),
(131,'Marlena','Nowacki','2019-02-25','Kobieta',NULL,1,8,'nie','Tak',NULL,NULL,131),
(132,'Stanisław','Nowacki','2013-03-09','Mężczyzna','Mroczny Poranek',1,7,'tak','Nie',NULL,NULL,132),
(133,'Aleksandra','Nowak','2017-07-29','Kobieta','Cichy Pomost',1,4,'tak','Nie',NULL,NULL,133),
(134,'Lidia','Nowak','2007-06-12','Kobieta','Kamienny Okoń',1,8,'tak','Nie',NULL,NULL,134),
(135,'Maria','Nowak','2017-02-14','Kobieta',NULL,1,1,'tak','Tak',NULL,NULL,135),
(136,'Łucja','Nowicki','2011-03-24','Kobieta','Jeziorny Głębina',1,5,'tak','Tak',NULL,NULL,136),
(137,'Filip','Olszewski','2006-01-21','Mężczyzna','Skryty Żeglarz',1,10,'tak','Tak',NULL,NULL,137),
(138,'Aleksandra','Ostrowski','2014-09-03','Kobieta','Leśny Karp',1,7,'tak','Nie',NULL,NULL,138),
(139,'Ignacy','Ostrowski','2015-01-05','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,139),
(140,'Irena','Ostrowski','2015-11-14','Kobieta',NULL,1,7,'nie','Nie',NULL,NULL,140),
(141,'Bolesław','Pawlak','2006-11-22','Mężczyzna',NULL,1,8,'nie','Nie',NULL,NULL,141),
(142,'Sabina','Pawlak','2012-08-02','Kobieta','Mroczny Głębina',1,8,'tak','Nie',NULL,NULL,142),
(143,'Mikołaj','Pawłowski','2019-03-07','Mężczyzna','Skryty Perkoz',1,10,'tak','Tak',NULL,NULL,143),
(144,'Oliwia','Pawłowski','2008-05-21','Kobieta','Mroczny Zatoka',1,4,'tak','Nie',NULL,NULL,144),
(145,'Ewa','Piątek','2008-10-03','Kobieta',NULL,1,3,'nie','Tak',NULL,NULL,145),
(146,'Oskar','Piątek','2016-10-17','Mężczyzna','Wietrzny Okoń',1,2,'tak','Tak',NULL,NULL,146),
(147,'Henryk','Piotrowski','2013-02-22','Mężczyzna','Mroczny Trzciny',1,5,'tak','Nie',NULL,NULL,147),
(148,'Igor','Piotrowski','2014-05-20','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,148),
(149,'Irena','Piotrowski','2017-08-27','Kobieta',NULL,1,5,'nie','Tak',NULL,NULL,149),
(150,'Katarzyna','Piotrowski','2006-04-02','Kobieta','Jeziorny Wędrowiec',1,4,'tak','Nie',NULL,NULL,150),
(151,'Stefan','Piotrowski','2009-03-25','Mężczyzna',NULL,1,10,'nie','Nie',NULL,NULL,151),
(152,'Marcin','Przybylski','2018-09-22','Mężczyzna',NULL,1,4,'nie','Nie',NULL,NULL,152),
(153,'Beata','Rogowski','2016-03-31','Kobieta',NULL,1,1,'tak','Tak',NULL,NULL,153),
(154,'Halina','Rogowski','2013-11-12','Kobieta',NULL,1,2,'nie','Tak',NULL,NULL,154),
(155,'Marlena','Rogowski','2009-05-12','Kobieta',NULL,1,1,'nie','Nie',NULL,NULL,155),
(156,'Halina','Rutkowski','2016-12-03','Kobieta','Błotny Pływak',1,8,'tak','Nie',NULL,NULL,156),
(157,'Karol','Rutkowski','2016-06-10','Mężczyzna','Mroczny Perkoz',1,3,'tak','Nie',NULL,NULL,157),
(158,'Mateusz','Rutkowski','2006-01-24','Mężczyzna',NULL,1,6,'nie','Tak',NULL,NULL,158),
(159,'Bartosz','Rybicki','2007-11-18','Mężczyzna',NULL,1,2,'nie','Nie',NULL,NULL,159),
(160,'Cezary','Rybicki','2018-09-03','Mężczyzna','Cichy Głębina',1,4,'tak','Tak',NULL,NULL,160),
(161,'Elżbieta','Rybicki','2009-04-01','Kobieta','Srebrny Łabędź',1,7,'tak','Tak',NULL,NULL,161),
(162,'Piotr','Rybicki','2014-12-02','Mężczyzna','Mglisty Sitowie',1,10,'tak','Nie',NULL,NULL,162),
(163,'Agnieszka','Sawicki','2016-10-17','Kobieta','Zielony Poranek',1,4,'tak','Tak',NULL,NULL,163),
(164,'Ireneusz','Sawicki','2017-09-18','Mężczyzna',NULL,1,7,'nie','Tak',NULL,NULL,164),
(165,'Tomasz','Sawicki','2019-09-03','Mężczyzna','Leśny Zatoka',1,3,'tak','Tak',NULL,NULL,165),
(166,'Maciej','Sikora','2007-10-21','Mężczyzna',NULL,1,9,'nie','Nie',NULL,NULL,166),
(167,'Łucja','Sikora','2013-07-04','Kobieta',NULL,1,9,'nie','Tak',NULL,NULL,167),
(168,'Anna','Sobczak','2011-06-19','Kobieta','Mglisty Brzeg',1,3,'tak','Nie',NULL,NULL,168),
(169,'Iwona','Sobczak','2007-06-24','Kobieta','Szumiący Rybak',1,4,'tak','Nie',NULL,NULL,169),
(170,'Oskar','Sobczak','2015-10-14','Mężczyzna',NULL,1,5,'nie','Nie',NULL,NULL,170),
(171,'Marcin','Sokołowski','2013-05-06','Mężczyzna',NULL,1,1,'tak','Tak',NULL,NULL,171),
(172,'Mirosław','Sokołowski','2015-10-10','Mężczyzna',NULL,1,5,'nie','Nie',NULL,NULL,172),
(173,'Olga','Sokołowski','2010-02-11','Kobieta',NULL,1,4,'nie','Tak',NULL,NULL,173),
(174,'Robert','Sokołowski','2015-09-23','Mężczyzna','Wodny Pływak',1,4,'tak','Tak',NULL,NULL,174),
(175,'Lena','Sosnowski','2011-06-24','Kobieta','Słoneczny Zatoka',1,9,'tak','Tak',NULL,NULL,175),
(176,'Andrzej','Sroka','2010-09-21','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,176),
(177,'Cezary','Sroka','2013-12-21','Mężczyzna',NULL,1,4,'nie','Nie',NULL,NULL,177),
(178,'Tomasz','Stankiewicz','2017-01-17','Mężczyzna',NULL,1,7,'nie','Nie',NULL,NULL,178),
(179,'Aleksandra','Stępień','2018-11-19','Kobieta','Leśny Pomost',1,8,'tak','Nie',NULL,NULL,179),
(180,'Beata','Stępień','2014-06-01','Kobieta',NULL,1,7,'nie','Tak',NULL,NULL,180),
(181,'Ignacy','Stępień','2016-06-25','Mężczyzna','Tęczowy Pomost',1,6,'tak','Nie',NULL,NULL,181),
(182,'Jakub','Stępień','2016-03-08','Mężczyzna','Błękitny Brzeg',1,6,'tak','Nie',NULL,NULL,182),
(183,'Monika','Stępień','2013-10-23','Kobieta','Jeziorny Fale',1,5,'tak','Tak',NULL,NULL,183),
(184,'Sławomir','Stępień','2009-11-23','Mężczyzna','Błotny Mewa',1,3,'tak','Tak',NULL,NULL,184),
(185,'Sławomir','Strzelecki','2008-11-04','Mężczyzna','Dziki Sitowie',1,10,'tak','Nie',NULL,NULL,185),
(186,'Aleksandra','Szczepaniak','2009-11-18','Kobieta',NULL,1,2,'nie','Nie',NULL,NULL,186),
(187,'Eryk','Szczepaniak','2011-12-15','Mężczyzna',NULL,1,2,'nie','Nie',NULL,NULL,187),
(188,'Julia','Szczepaniak','2011-01-05','Kobieta','Jeziorny Brzeg',1,3,'tak','Nie',NULL,NULL,188),
(189,'Karol','Szczepański','2008-01-29','Mężczyzna','Wodny Zatoka',1,3,'tak','Nie',NULL,NULL,189),
(190,'Grzegorz','Szulc','2016-04-25','Mężczyzna','Tęczowy Poranek',1,2,'tak','Nie',NULL,NULL,190),
(191,'Irena','Szulc','2015-01-30','Kobieta','Skryty Szczupak',1,1,'tak','Tak',NULL,NULL,191),
(192,'Emil','Szymański','2012-01-14','Mężczyzna',NULL,1,10,'nie','Tak',NULL,NULL,192),
(193,'Jakub','Szymański','2013-07-05','Mężczyzna','Błękitny Okoń',1,5,'tak','Nie',NULL,NULL,193),
(194,'Filip','Szymczak','2009-09-24','Mężczyzna',NULL,1,2,'nie','Tak',NULL,NULL,194),
(195,'Joanna','Szymczak','2008-09-24','Kobieta',NULL,1,4,'nie','Nie',NULL,NULL,195),
(196,'Andrzej','Turczyk','2013-06-20','Mężczyzna','Leśny Trzciny',1,6,'tak','Tak',NULL,NULL,196),
(197,'Dorota','Turczyk','2014-08-18','Kobieta',NULL,1,8,'nie','Nie',NULL,NULL,197),
(198,'Dorota','Turczyk','2012-08-28','Kobieta','Cichy Poranek',1,6,'tak','Tak',NULL,NULL,198),
(199,'Hubert','Turczyk','2006-07-12','Mężczyzna','Krystaliczny Brzeg',1,4,'tak','Nie',NULL,NULL,199),
(200,'Lidia','Turczyk','2016-11-17','Kobieta','Wietrzny Perkoz',1,5,'tak','Nie',NULL,NULL,200),
(201,'Kazimierz','Urban','2011-07-01','Mężczyzna',NULL,1,8,'nie','Nie',NULL,NULL,201),
(202,'Emil','Walczak','2018-04-03','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,202),
(203,'Gabriela','Walczak','2012-01-15','Kobieta','Mroczny Głębina',1,6,'tak','Nie',NULL,NULL,203),
(204,'Katarzyna','Walczak','2018-08-27','Kobieta',NULL,1,2,'nie','Tak',NULL,NULL,204),
(205,'Lech','Walczak','2018-04-25','Mężczyzna','Błękitny Żuraw',1,3,'tak','Tak',NULL,NULL,205),
(206,'Natan','Walczak','2009-11-24','Mężczyzna','Dziki Poranek',1,2,'tak','Tak',NULL,NULL,206),
(207,'Joanna','Walentynowicz','2011-07-09','Kobieta','Mroczny Trzciny',1,9,'tak','Tak',NULL,NULL,207),
(208,'Marlena','Walentynowicz','2012-03-19','Kobieta','Wietrzny Fale',1,8,'tak','Nie',NULL,NULL,208),
(209,'Aleksander','Wawrzyniak','2019-11-27','Mężczyzna','Cichy Brzeg',1,3,'tak','Nie',NULL,NULL,209),
(210,'Henryk','Wawrzyniak','2011-04-09','Mężczyzna','Szumiący Pływak',1,9,'tak','Tak',NULL,NULL,210),
(211,'Bogusław','Wesołowski','2012-07-28','Mężczyzna','Mroczny Karp',1,4,'tak','Tak',NULL,NULL,211),
(212,'Dariusz','Wesołowski','2014-02-01','Mężczyzna',NULL,1,1,'nie','Tak',NULL,NULL,212),
(213,'Janina','Wesołowski','2007-01-02','Kobieta',NULL,1,4,'nie','Nie',NULL,NULL,213),
(214,'Franciszek','Wieczorek','2011-04-27','Mężczyzna','Srebrny Poranek',1,6,'tak','Tak',NULL,NULL,214),
(215,'Lena','Wieczorek','2006-06-30','Kobieta',NULL,1,7,'nie','Nie',NULL,NULL,215),
(216,'Monika','Wieczorek','2013-01-05','Kobieta',NULL,1,4,'nie','Tak',NULL,NULL,216),
(217,'Bolesław','Wilk','2016-03-10','Mężczyzna','Złoty Wędrowiec',1,10,'tak','Tak',NULL,NULL,217),
(218,'Patryk','Wilk','2006-10-08','Mężczyzna','Srebrny Trzciny',1,1,'tak','Nie',NULL,NULL,218),
(219,'Piotr','Wilk','2017-01-15','Mężczyzna','Tęczowy Okoń',1,5,'tak','Nie',NULL,NULL,219),
(220,'Roman','Wilk','2014-08-24','Mężczyzna','Mroczny Zatoka',1,2,'tak','Tak',NULL,NULL,220),
(221,'Magdalena','Wiśniewski','2006-08-13','Kobieta','Mglisty Żuraw',1,6,'tak','Tak',NULL,NULL,221),
(222,'Monika','Wiśniewski','2009-04-02','Kobieta','Szumiący Wodnik',1,7,'tak','Nie',NULL,NULL,222),
(223,'Aleksandra','Wojciechowski','2006-09-30','Kobieta','Kamienny Żuraw',1,4,'tak','Nie',NULL,NULL,223),
(224,'Bogdan','Wojciechowski','2007-08-08','Mężczyzna','Błotny Sitowie',1,1,'tak','Nie',NULL,NULL,224),
(225,'Emilia','Wojciechowski','2019-09-17','Kobieta','Skryty Pomost',1,7,'tak','Nie',NULL,NULL,225),
(226,'Jan','Wojciechowski','2009-09-13','Mężczyzna','Jeziorny Pomost',1,7,'tak','Tak',NULL,NULL,226),
(227,'Lena','Wojciechowski','2018-02-15','Kobieta',NULL,1,6,'nie','Nie',NULL,NULL,227),
(228,'Beata','Woliński','2009-11-20','Kobieta',NULL,1,5,'nie','Nie',NULL,NULL,228),
(229,'Franciszek','Woliński','2008-08-02','Mężczyzna','Srebrny Karp',1,5,'tak','Tak',NULL,NULL,229),
(230,'Bogusław','Woźniak','2009-01-25','Mężczyzna',NULL,1,3,'nie','Nie',NULL,NULL,230),
(231,'Magdalena','Wójcik','2008-04-01','Kobieta','Srebrny Łabędź',1,2,'tak','Tak',NULL,NULL,231),
(232,'Cezary','Wróbel','2008-06-12','Mężczyzna',NULL,1,10,'nie','Tak',NULL,NULL,232),
(233,'Eryk','Wróbel','2006-08-22','Mężczyzna',NULL,1,9,'nie','Nie',NULL,NULL,233),
(234,'Radosław','Wróbel','2009-04-23','Mężczyzna','Kamienny Sitowie',1,2,'tak','Tak',NULL,NULL,234),
(235,'Wiktoria','Wróbel','2017-03-19','Kobieta','Skryty Żuraw',1,4,'tak','Nie',NULL,NULL,235),
(236,'Mikołaj','Zawadzki','2013-05-21','Mężczyzna','Słoneczny Poranek',1,8,'tak','Nie',NULL,NULL,236),
(237,'Olga','Zawadzki','2006-12-13','Kobieta','Wodny Zatoka',1,4,'tak','Nie',NULL,NULL,237),
(238,'Maria','Zielińska','2017-06-05','Kobieta',NULL,1,10,'nie','Nie',NULL,NULL,238),
(239,'Irena','Zieliński','2010-12-04','Kobieta',NULL,1,8,'nie','Nie',NULL,NULL,239),
(240,'Jakub','Zieliński','2008-08-26','Mężczyzna',NULL,1,5,'nie','Tak',NULL,NULL,240),
(241,'Emil','Ziółkowski','2012-12-13','Mężczyzna',NULL,1,3,'nie','Tak',NULL,NULL,241),
(242,'Magdalena','Ziółkowski','2015-07-08','Kobieta',NULL,1,4,'nie','Nie',NULL,NULL,242),
(243,'Monika','Ziółkowski','2018-08-04','Kobieta','Słoneczny Głębina',1,5,'tak','Nie',NULL,NULL,243),
(244,'Janina','Żuk','2019-09-15','Kobieta','Dziki Sitowie',1,6,'tak','Tak',NULL,NULL,244),
(245,'Oliwia','Żuk','2019-09-01','Kobieta',NULL,1,6,'nie','Nie',NULL,NULL,245),
(246,'Sabina','Żuk','2010-11-01','Kobieta',NULL,1,9,'nie','Nie',NULL,NULL,246);
/*!40000 ALTER TABLE `uczestnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wychowawca`
--

DROP TABLE IF EXISTS `wychowawca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `wychowawca` (
  `id` int(11) NOT NULL,
  `imie` varchar(20) NOT NULL,
  `nazwisko` varchar(20) NOT NULL,
  `zajecia` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `wychowawca_ibfk_1` FOREIGN KEY (`id`) REFERENCES `uczestnik` (`wychowawca`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wychowawca`
--

LOCK TABLES `wychowawca` WRITE;
/*!40000 ALTER TABLE `wychowawca` DISABLE KEYS */;
INSERT INTO `wychowawca` VALUES
(1,'Jan','Kowalski','las'),
(2,'Anna','Nowak','wolne'),
(3,'Piotr','Wiśniewski','wolne'),
(4,'Maria','Zielińska','wolne'),
(5,'Tomasz','Kaczmarek','wolne'),
(6,'Katarzyna','Mazur','wolne'),
(7,'Michał','Lewandowski','wolne'),
(8,'Agnieszka','Dąbrowska','wolne'),
(9,'Paweł','Wójcik','wolne'),
(10,'Monika','Kamińska','wolne');
/*!40000 ALTER TABLE `wychowawca` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-21 16:10:34
