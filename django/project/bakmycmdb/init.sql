-- MySQL dump 10.13  Distrib 5.5.42, for Linux (x86_64)
--
-- Host: localhost    Database: ht_cmdb_dev
-- ------------------------------------------------------
-- Server version	5.5.42-log

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
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `htmlID` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `availabity` bigint(20) NOT NULL,
  `icon` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fatherID` int(11) NOT NULL,
  `htmlClass` varchar(50) COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_htmlID_66f80517ea65b18b_uniq` (`htmlID`,`availabity`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'仪表盘','dashboard','/dashboard/index/',1,'fa-bar-chart-o',0,'dashboard'),(2,'资产管理','assets','#',1,'fa-desktop',0,'assets'),(4,'设备列表','host_list','/assets/asset_list/',1492681412,'',3,NULL),(5,'添加设备','assetAdd','/assets/assetAdd/',1,'',3,'assetList assetAdd'),(3,'设备管理','assetList','/assets/assetList/',1,'arrow',2,'assetList assetAdd'),(7,'数据中心管理','idcList','/assets/idcList/',1,'',2,'idcList idcAdd'),(8,'数据中心列表','idc_list','/assets/idc_list/',1492681594,'',7,NULL),(9,'添加数据中心','idcAdd','/assets/idcAdd/',1,'',7,'idcList idcAdd'),(10,'应用管理','app','#',1,'fa-money',0,'app'),(11,'应用列表','appList','/app/appList/',1,'',10,'appList appAdd'),(12,'应用添加','appAdd','/app/appAdd/',1,'',11,'appList appAdd'),(13,'应用角色','roleList','/app/roleList/',1,'',10,'roleList roleAdd'),(14,'应用角色添加','roleAdd','/app/roleAdd/',1,'',13,'roleList roleAdd'),(17,'域名管理','domainNameManager','#',1,'fa-font',0,'domainNameManager'),(18,'域名列表','domainNameList','/domainNameManager/domainNameList/',1,'',17,'domainNameList domainNameAdd'),(19,'添加域名','domainNameAdd','/domainNameManager/domainNameAdd/',1,'',18,'domainNameList domainNameAdd'),(20,'配置管理','configManager','#',1,'fa-wrench',0,'configManager'),(21,'配置列表','configList','/configManager/configList/',1,'',20,'configList configAdd'),(22,'添加配置','configAdd','/configManager/configAdd/',1,'',21,'configList configAdd'),(23,'用户管理','accounts','#',1,'fa-user',0,'accounts'),(24,'部门列表','departmentList','/accounts/departmentList/',1,'',23,'departmentList departmentAdd'),(25,'添加部门','departmentAdd','/accounts/departmentAdd/',1,'',24,'departmentList departmentAdd'),(26,'用户列表','userList','/accounts/userList/',1,'',23,'userList userAdd'),(27,'添加用户','userAdd','/accounts/userAdd/',1,'',26,'userList userAdd'),(28,'权限管理','auth','#',1,'fa-ban',0,'auth'),(29,'菜单列表','menuAdminList','/auth/menuAdminList/',1,'',28,'menuAdminList menuAdminAdd'),(30,'添加菜单','menuAdminAdd','/auth/menuAdminAdd/',1,'',29,'menuAdminList menuAdminAdd'),(31,'告警管理','alarm','#',1,'fa-bullhorn',0,'alarm'),(32,'规则列表','alarmList','/alarm/alarmList/',1,'',31,'alarmList alarmAdd'),(33,'添加规则','alarmAdd','/alarm/alarmAdd/',1,'',32,'alarmList alarmAdd'),(34,'仪表盘','index','/dashboard/index/',1,'',1,'dashboard');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `departmentName` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_departmentName_26aae1504634ab6d_uniq` (`departmentName`,`availabity`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'运维部','',1);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--

DROP TABLE IF EXISTS `myUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myUser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `wechat` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mobile` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `qq` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `myUser_username_1843759df7e4cea3_uniq` (`username`,`availabity`),
  KEY `myUser_bf691be4` (`department_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myUser`
--

LOCK TABLES `myUser` WRITE;
/*!40000 ALTER TABLE `myUser` DISABLE KEYS */;
INSERT INTO `myUser` VALUES (1,'pbkdf2_sha256$20000$DYS1J412ozE5$8jxicCjxDxS7SO+nD0nv5pZAbn4kwIsgHECLtfK2h/0=','2017-04-13 14:06:23',1,'cmdbAdmin','系统管理员','','',1,1,'2017-03-28 08:12:21','','','',1,1);
/*!40000 ALTER TABLE `myUser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
--

DROP TABLE IF EXISTS `myUser_auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myUser_auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`menu_id`),
  KEY `myUser_auth_8b14fb18` (`myuser_id`),
  KEY `myUser_auth_93e25458` (`menu_id`)
) ENGINE=MyISAM AUTO_INCREMENT=184 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myUser_auth`
--

LOCK TABLES `myUser_auth` WRITE;
/*!40000 ALTER TABLE `myUser_auth` DISABLE KEYS */;
INSERT INTO `myUser_auth` VALUES (153,1,1),(154,1,34),(155,1,2),(156,1,3),(157,1,5),(158,1,7),(159,1,9),(160,1,10),(161,1,11),(162,1,12),(163,1,13),(164,1,14),(165,1,15),(166,1,16),(167,1,17),(168,1,18),(169,1,19),(170,1,20),(171,1,21),(172,1,22),(173,1,23),(174,1,24),(175,1,25),(176,1,26),(177,1,27),(178,1,28),(179,1,29),(180,1,30),(181,1,31),(182,1,32),(183,1,33);
/*!40000 ALTER TABLE `myUser_auth` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-01 16:15:29
