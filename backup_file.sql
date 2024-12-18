-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: localhost    Database: AbioticFactor
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `Entity`
--

DROP TABLE IF EXISTS `Entity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Entity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codename` varchar(32) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entity`
--

LOCK TABLES `Entity` WRITE;
/*!40000 ALTER TABLE `Entity` DISABLE KEYS */;
INSERT INTO `Entity` VALUES (8,'IS-111','abiotic factor','good game'),(12,'IS-0064','Composer','DESIGNATION:Crucis(AG/IV)\r\nCONTAINMENT PROTOCOL: Effective containmentof non-adjusted lS-0064 specimens requires thefacility be located at least 2000m from anyperforation phenomenon. All locations are to beequipped with perforation-suppressing fields,back-up power and fully hermetically sealed.Acoustic baffling is recommended, as the longterm effects of exposure to the Composer\'s \'songsare currently unknown.'),(13,'IS-0138','The Train - Anteverse Xl','DESIGNATION:Thela(EH/EN/R)\r\nCONTAINMENT PROTOCOL: A recursive,superpositioned meta-location, lS-0138 is theorizedto be held together at the atomic level by theTrain\'s ongoing momentum. Although untested,mathematical modelling suggests that if the trainwere to stop, the energy released would be 10 topower 55 joules.'),(14,'IS-0184-A','Exor','DESIGNATION:Crucis(AG/EN/IN)\r\nCONTAINMENT PROTOCOLS: All containmentfacilities for lS-0184-A require Grade 4impactshielding and/or Grade 5 blast dampening inaccordance with GlSP ratings. All personnelconducting research on this subject must wearGrade 4 body armor with full electrical grounding.even when subject is sedated or unconscious.Direct interaction in any state is not advised.\r\nIS-0184-A should not be exposed to any flammablematerials. Feed remotely.');
/*!40000 ALTER TABLE `Entity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Location`
--

DROP TABLE IF EXISTS `Location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Location` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Location`
--

LOCK TABLES `Location` WRITE;
/*!40000 ALTER TABLE `Location` DISABLE KEYS */;
INSERT INTO `Location` VALUES (3,'Office Sector','The Office Sector is a 3 floor section within Gate\'s facility. Between the Cascade Laboratories and Manufacturing West, by the time of the player\'s arrival, it is nearly devoid of human life save for a few who are either stranded or chose to stay. Other areas are locked which are opened elsewhere'),(6,'china','good'),(8,'Anteverse ll B','The Mycofields\r\nCraggy and malformed, this region of Anteverse ll islittle more than a mass of rock orbiting a \'sun\' that isno sun at all - rather a vacuum point slowly suckingeverything towards it.\r\nMuch closer to it\'s \'star\' than Anteverse ll A, the tidalforces generate tremendous heat, producingtributaries of superheated magma that restrict thegrowth of endemic vegetation, already limited bythe realm\'s direly low entropy.\r\nA jagged maze of caves, cliffs, ledges and ancientpaths, existence under these conditions is extremelyharsh and competition for resources is brutallyintense. The creatures that live within it are forced toadapt to - and exploit - the profusion of fungal lifethat persists there.'),(9,'Anteverse ll A','Far Carden\r\nIn accordance with trans-luminal modelling, GATE\'Ssecond perforation experiment \'grounded’ itself inone of the largest bodies of mass in Anteverse ll- itsunfathomably old heart.'),(10,'Cascade Laboratories','Advanced Study and Containment\r\nLabs Sector is the epicenter of the GATE CascadeResearch Facility\'s research into advancedtechnology, as well as anomalies, xenoforms,paranormal phenomenon, arcane entities andartefacts of note.\r\nProviding secure immurment for entities rated up toThela level, Labs is divided into various sub-sectorsfocused variously on containment, advancedstudies and field research.'),(11,'Manufacturing West','Engineering and Fabrication\r\nThe industrial heart of the GATE Cascade ResearchFacility, the Manufacturing Sector is responsible fordesigning and engineering all research equipmentand machinery for study within the facility - as wellas fabricating technical and specialist tools for otherGATE facilities.\r\nIt is here the facility\'s origins as a decommissionedlithium mine are most clearly visible.');
/*!40000 ALTER TABLE `Location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `authorized` int DEFAULT '0',
  `sector` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (7,'Kenny','666',1,'Office Sector'),(9,'Dr. Ulrich ThulePhysicist','123',0,'Cascade Laboratories'),(10,'Zmoke','888',1,'Security Sector'),(11,'Jack','222',0,'Security Sector'),(12,'Dr. Elanor Newman','123',0,'Cascade Laboratories'),(13,'Dr. Steven Stewart','321',0,'Office Sector');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Theory`
--

DROP TABLE IF EXISTS `Theory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Theory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Theory`
--

LOCK TABLES `Theory` WRITE;
/*!40000 ALTER TABLE `Theory` DISABLE KEYS */;
INSERT INTO `Theory` VALUES (2,'Airborne Spores','Weather\r\nAs research expands across biological destinationsthroughout the so-called \"Anteverses\", all staff arereminded to take effective precautions whenvisiting these locations.\r\nGISP-approved airtight maskings are required whenconducting experiments or visiting any site with arisk of ingesting or inhaling spores, viral analoguesor other contaminants that may cause respiratoryissues, infection or death.\r\nReturning to a GATE facility without undertakingcomplete decontamination procedures is strictlyprohibited. Contamination of GATE property due tonegligence by TransRecon or other field personnel isgrounds for dismissal.'),(3,'The Dark Lens','Tachyonic Telemetry Targeting(T3) Unit\r\nThe Dark Lens - technically a Tachyonic TelemetryTargeting or T3 unit - was developed by ElanorNewman to guide and control the tachyonic field!that underpin perforation technology\r\nIt cannot safely be turned off.'),(4,'The Synchrotron','The GATE Cascade Research Facility Collider\r\nThe GATE Cascade Research Facility\'s particleaccelerator is one of the few private synchrotrons inthe world. Operating at ranges approaching1.0TeV, it is used in everything from materialsresearch to trans-luminal investigations.\r\nIt was the synchroton that allowed Dr. S. Tengku tomake her discovery of a new category of bosonicmatter, opening the way for perforationtechnology.'),(5,'Temporal Tethering','Why do portal worlds reset?\r\n\"One of the most fascinating aspects of perforationtechnology is temporal tethering: Each entry to ananteverse seems to start a timer, which resets after agiven period - as though a band of time stretches,before snapping back to its origin.l am confidentwe will understand this phenomenon in time, butuntil we do, it violates a dozen scientific principles.\r\n~ Dr. Derek Manse');
/*!40000 ALTER TABLE `Theory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-15  8:50:33
