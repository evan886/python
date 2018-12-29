-- MySQL dump 10.13  Distrib 5.6.32, for Linux (x86_64)
--
-- Host: localhost    Database: hcmdb
-- ------------------------------------------------------
-- Server version	5.6.32-log

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
-- Table structure for table `alarm`
--

DROP TABLE IF EXISTS `alarm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alarm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `level` int(11) NOT NULL,
  `way` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group` (`group`,`level`,`availabity`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alarm`
--

LOCK TABLES `alarm` WRITE;
/*!40000 ALTER TABLE `alarm` DISABLE KEYS */;
/*!40000 ALTER TABLE `alarm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alarm_user`
--

DROP TABLE IF EXISTS `alarm_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alarm_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alarm_id` int(11) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alarm_id` (`alarm_id`,`myuser_id`),
  KEY `alarm_user_b1f918f6` (`alarm_id`),
  KEY `alarm_user_8b14fb18` (`myuser_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alarm_user`
--

LOCK TABLES `alarm_user` WRITE;
/*!40000 ALTER TABLE `alarm_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `alarm_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app`
--

DROP TABLE IF EXISTS `app`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `another_name` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `architecture` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_name_381dd79f05628d9b_uniq` (`name`,`another_name`,`availabity`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app`
--

LOCK TABLES `app` WRITE;
/*!40000 ALTER TABLE `app` DISABLE KEYS */;
INSERT INTO `app` VALUES (1,'sdkweb','','',1),(2,'sdk redis for inland','','',1),(3,'sdb_db','','',1),(4,'广告流量','广告流量','',1),(5,'数据分析','数据分析','',1);
/*!40000 ALTER TABLE `app` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appRole`
--

DROP TABLE IF EXISTS `appRole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appRole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `appRole_name_3cf460a6e8d67331_uniq` (`name`,`availabity`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appRole`
--

LOCK TABLES `appRole` WRITE;
/*!40000 ALTER TABLE `appRole` DISABLE KEYS */;
INSERT INTO `appRole` VALUES (1,'web1',1),(2,'db1',1),(3,'web2',1),(4,'redis',1),(5,'db2',1),(6,'web',1),(7,'后台管理',1),(8,'cdb(mysql)',1);
/*!40000 ALTER TABLE `appRole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_roles`
--

DROP TABLE IF EXISTS `app_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `appid_id` int(11) NOT NULL,
  `roleid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_roles_7f950d3b` (`appid_id`),
  KEY `app_roles_f60990d5` (`roleid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_roles`
--

LOCK TABLES `app_roles` WRITE;
/*!40000 ALTER TABLE `app_roles` DISABLE KEYS */;
INSERT INTO `app_roles` VALUES (1,1,1),(2,1,3),(3,2,4),(4,3,2),(5,3,5),(6,4,6),(7,4,7),(8,4,8),(9,5,6),(10,5,8);
/*!40000 ALTER TABLE `app_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset`
--

DROP TABLE IF EXISTS `asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_type` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `ip` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `other_ip` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `port` int(11) NOT NULL,
  `is_monitoring` tinyint(1) NOT NULL,
  `is_backup` tinyint(1) NOT NULL,
  `editor` longtext COLLATE utf8_unicode_ci,
  `availabity` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `intraip` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asset_ip_59850975c1d2f626_uniq` (`ip`,`availabity`),
  KEY `asset_0e939a4f` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset`
--

LOCK TABLES `asset` WRITE;
/*!40000 ALTER TABLE `asset` DISABLE KEYS */;
INSERT INTO `asset` VALUES (1,'云服务器','119.29.234.240','',22,1,1,'redis for 国内sdk平台',1,1,'10.104.197.215'),(2,'云服务器','119.29.221.58','内网ip 10.104.197.215',22,1,1,'web for 国内sdk平台',1,1,'10.104.197.215'),(3,'云服务器','119.29.194.112','内网IP 10.104.161.221',22,1,1,'sdb web2服务器',1,1,'0'),(4,'云服务器','119.29.221.18','内网IP 10.104.227.251',22,1,1,'',1,1,'0'),(5,'云服务器','119.29.216.29','内网IP  10.104.101.97',22,1,1,'',1,1,'0'),(6,'云服务器','118.89.30.202','10.135.131.241',22,1,1,'',1,2,'0'),(7,'云服务器','118.89.28.39','10.135.154.24',22,1,1,'',1,2,'0'),(8,'云数据库mysql','10.66.202.80','',22,1,1,'',1,2,'0'),(9,'云数据库mysql','10.66.208.6','',22,1,1,'',1,3,'0'),(10,'云服务器','123.207.227.123','10.135.68.219 过期时间:07-28',22,1,1,'过期时间:07-28',1,3,'0'),(11,'云服务器','122.168.30.56','',22,1,1,'test',1,1,'192.168.30.56 '),(12,'云服务器','12.16.30.56','',22,1,1,'test2',1,1,'192.168.30.59');
/*!40000 ALTER TABLE `asset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset_app_name`
--

DROP TABLE IF EXISTS `asset_app_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset_app_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asset_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asset_id` (`asset_id`,`app_id`),
  KEY `asset_app_name_51c6d5db` (`asset_id`),
  KEY `asset_app_name_f382adfe` (`app_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_app_name`
--

LOCK TABLES `asset_app_name` WRITE;
/*!40000 ALTER TABLE `asset_app_name` DISABLE KEYS */;
INSERT INTO `asset_app_name` VALUES (24,2,1),(8,3,1),(23,1,2),(11,4,3),(12,5,3),(14,6,4),(15,7,4),(16,8,4),(17,9,5),(20,10,5),(21,11,1),(22,12,1);
/*!40000 ALTER TABLE `asset_app_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset_config`
--

DROP TABLE IF EXISTS `asset_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asset_id` int(11) NOT NULL,
  `config_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asset_id` (`asset_id`,`config_id`),
  KEY `asset_config_51c6d5db` (`asset_id`),
  KEY `asset_config_d1738a90` (`config_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_config`
--

LOCK TABLES `asset_config` WRITE;
/*!40000 ALTER TABLE `asset_config` DISABLE KEYS */;
/*!40000 ALTER TABLE `asset_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset_role_name`
--

DROP TABLE IF EXISTS `asset_role_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asset_role_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asset_id` int(11) NOT NULL,
  `app_roles_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asset_id` (`asset_id`,`app_roles_id`),
  KEY `asset_role_name_51c6d5db` (`asset_id`),
  KEY `asset_role_name_75472616` (`app_roles_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_role_name`
--

LOCK TABLES `asset_role_name` WRITE;
/*!40000 ALTER TABLE `asset_role_name` DISABLE KEYS */;
INSERT INTO `asset_role_name` VALUES (21,2,1),(7,3,2),(20,1,3),(9,4,4),(10,5,5),(12,6,7),(13,7,6),(14,8,8),(15,9,10),(18,10,9),(19,11,2);
/*!40000 ALTER TABLE `asset_role_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add department',6,'add_department'),(17,'Can change department',6,'change_department'),(18,'Can delete department',6,'delete_department'),(19,'Can add my user',7,'add_myuser'),(20,'Can change my user',7,'change_myuser'),(21,'Can delete my user',7,'delete_myuser'),(22,'Can add data center',8,'add_datacenter'),(23,'Can change data center',8,'change_datacenter'),(24,'Can delete data center',8,'delete_datacenter'),(25,'Can add asset',9,'add_asset'),(26,'Can change asset',9,'change_asset'),(27,'Can delete asset',9,'delete_asset'),(28,'Can add config',10,'add_config'),(29,'Can change config',10,'change_config'),(30,'Can delete config',10,'delete_config'),(31,'Can add app role',11,'add_approle'),(32,'Can change app role',11,'change_approle'),(33,'Can delete app role',11,'delete_approle'),(34,'Can add app',12,'add_app'),(35,'Can change app',12,'change_app'),(36,'Can delete app',12,'delete_app'),(37,'Can add app_roles',13,'add_app_roles'),(38,'Can change app_roles',13,'change_app_roles'),(39,'Can delete app_roles',13,'delete_app_roles'),(40,'Can add domain name',14,'add_domainname'),(41,'Can change domain name',14,'change_domainname'),(42,'Can delete domain name',14,'delete_domainname'),(43,'Can add alarm',15,'add_alarm'),(44,'Can change alarm',15,'change_alarm'),(45,'Can delete alarm',15,'delete_alarm'),(46,'Can add api access',16,'add_apiaccess'),(47,'Can change api access',16,'change_apiaccess'),(48,'Can delete api access',16,'delete_apiaccess'),(49,'Can add api key',17,'add_apikey'),(50,'Can change api key',17,'change_apikey'),(51,'Can delete api key',17,'delete_apikey'),(52,'Can add menu',18,'add_menu'),(53,'Can change menu',18,'change_menu'),(54,'Can delete menu',18,'delete_menu');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `config_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `config_type` int(11) NOT NULL,
  `config_dir` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `config_config_name_5615281ad70664bb_uniq` (`config_name`,`availabity`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataCenter`
--

DROP TABLE IF EXISTS `dataCenter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dataCenter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_number` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `area` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `editor` longtext COLLATE utf8_unicode_ci,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dataCenter_name_39b099e1311ba65e_uniq` (`name`,`area`,`availabity`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataCenter`
--

LOCK TABLES `dataCenter` WRITE;
/*!40000 ALTER TABLE `dataCenter` DISABLE KEYS */;
INSERT INTO `dataCenter` VALUES (1,'国内sdk','国内sdk','华南','',1),(2,'广州广告流量','广州广告流量','华南','',1),(3,'广州数据分析','广州数据分析','华南','',1);
/*!40000 ALTER TABLE `dataCenter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

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
-- Table structure for table `department_auth`
--

DROP TABLE IF EXISTS `department_auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department_auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_id` (`department_id`,`menu_id`),
  KEY `department_auth_bf691be4` (`department_id`),
  KEY `department_auth_93e25458` (`menu_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department_auth`
--

LOCK TABLES `department_auth` WRITE;
/*!40000 ALTER TABLE `department_auth` DISABLE KEYS */;
/*!40000 ALTER TABLE `department_auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(6,'accounts','department'),(7,'accounts','myuser'),(8,'assets','datacenter'),(9,'assets','asset'),(10,'configManager','config'),(11,'project','approle'),(12,'project','app'),(13,'project','app_roles'),(14,'domainNameManager','domainname'),(15,'alarm','alarm'),(16,'tastypie','apiaccess'),(17,'tastypie','apikey'),(18,'menuAuth','menu');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'menuAuth','0001_initial','2017-06-12 09:02:46'),(2,'contenttypes','0001_initial','2017-06-12 09:02:46'),(3,'contenttypes','0002_remove_content_type_name','2017-06-12 09:02:46'),(4,'auth','0001_initial','2017-06-12 09:02:46'),(5,'auth','0002_alter_permission_name_max_length','2017-06-12 09:02:46'),(6,'auth','0003_alter_user_email_max_length','2017-06-12 09:02:46'),(7,'auth','0004_alter_user_username_opts','2017-06-12 09:02:46'),(8,'auth','0005_alter_user_last_login_null','2017-06-12 09:02:46'),(9,'auth','0006_require_contenttypes_0002','2017-06-12 09:02:46'),(10,'accounts','0001_initial','2017-06-12 09:02:48'),(11,'admin','0001_initial','2017-06-12 09:02:48'),(12,'project','0001_initial','2017-06-12 09:02:49'),(13,'configManager','0001_initial','2017-06-12 09:02:49'),(14,'assets','0001_initial','2017-06-12 09:02:51'),(15,'domainNameManager','0001_initial','2017-06-12 09:02:51'),(16,'sessions','0001_initial','2017-06-12 09:02:51'),(17,'tastypie','0001_initial','2017-06-12 09:02:51'),(18,'assets','0002_auto_20170926_1502','2017-09-26 07:03:48');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('rr20x8yzq9hwz9vdrdtppv3s3713aa1q','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-06-26 09:00:18'),('ktpbsxndvj6i1eozadj0usuob2xl63s9','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-06-26 09:15:58'),('pxdgli6l9jfthtncb1qhyrw024pgfwwe','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-06-27 07:12:31'),('0d5xutesrp8l5h4l7ny07y78lsf99am9','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-06-28 05:52:15'),('x47yskbuizj23f8m6ujs6i2l1zqj1lcw','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-07-12 06:33:44'),('twua9oa2aly2br8ehno8a68l3vjku9j7','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-08-10 01:44:56'),('95lv3wfaapnvj5wv4wgmnj8tu0t9hpp4','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-08-26 03:14:16'),('8gdwb82r3zooqrqpngoufir5fjesgvd1','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-10-10 06:48:21'),('hyvhl3gukf4k6u8zxfq9vqknmrzw8n53','ZWNmYTNlNmQ2YTZkYzEwNjZhYTY1ZTIxODEwZDY5MGUxYzU3YTBmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NDc0YTVmYjhhYTNhZmU3YzlkNjNjZDRkZmQ3YzI0Njk1N2JlY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxNiIsIm1lbnVBdXRoIjpbeyJmaWVsZHMiOnsibmFtZSI6Ilx1OGQ0NFx1NGVhN1x1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFzc2V0cyIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRzIiwiaWNvbiI6ImZhLWRlc2t0b3AifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjJ9LHsiZmllbGRzIjp7Im5hbWUiOiJcdThiYmVcdTU5MDdcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhc3NldExpc3QiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0TGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXNzZXRMaXN0IGFzc2V0QWRkIiwiaWNvbiI6ImFycm93In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4YmJlXHU1OTA3IiwiaHRtbElEIjoiYXNzZXRBZGQiLCJ1cmwiOiIvYXNzZXRzL2Fzc2V0QWRkLyIsImZhdGhlcklEIjozLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhc3NldExpc3QgYXNzZXRBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo1fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiaWRjTGlzdCIsInVybCI6Ii9hc3NldHMvaWRjTGlzdC8iLCJmYXRoZXJJRCI6MiwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiaWRjTGlzdCBpZGNBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjo3fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU2NTcwXHU2MzZlXHU0ZTJkXHU1ZmMzIiwiaHRtbElEIjoiaWRjQWRkIiwidXJsIjoiL2Fzc2V0cy9pZGNBZGQvIiwiZmF0aGVySUQiOjcsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImlkY0xpc3QgaWRjQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6OX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImFwcCIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYXBwIiwiaWNvbiI6ImZhLW1vbmV5In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxMH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NWU5NFx1NzUyOFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImFwcExpc3QiLCJ1cmwiOiIvYXBwL2FwcExpc3QvIiwiZmF0aGVySUQiOjEwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjExfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoiYXBwQWRkIiwidXJsIjoiL2FwcC9hcHBBZGQvIiwiZmF0aGVySUQiOjExLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhcHBMaXN0IGFwcEFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyIiwiaHRtbElEIjoicm9sZUxpc3QiLCJ1cmwiOiIvYXBwL3JvbGVMaXN0LyIsImZhdGhlcklEIjoxMCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoicm9sZUxpc3Qgcm9sZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjEzfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU1ZTk0XHU3NTI4XHU4OWQyXHU4MjcyXHU2ZGZiXHU1MmEwIiwiaHRtbElEIjoicm9sZUFkZCIsInVybCI6Ii9hcHAvcm9sZUFkZC8iLCJmYXRoZXJJRCI6MTMsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6InJvbGVMaXN0IHJvbGVBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxNH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImRvbWFpbk5hbWVNYW5hZ2VyIiwidXJsIjoiIyIsImZhdGhlcklEIjowLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJkb21haW5OYW1lTWFuYWdlciIsImljb24iOiJmYS1mb250In0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoxN30seyJmaWVsZHMiOnsibmFtZSI6Ilx1NTdkZlx1NTQwZFx1NTIxN1x1ODg2OCIsImh0bWxJRCI6ImRvbWFpbk5hbWVMaXN0IiwidXJsIjoiL2RvbWFpbk5hbWVNYW5hZ2VyL2RvbWFpbk5hbWVMaXN0LyIsImZhdGhlcklEIjoxNywiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE4fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU1N2RmXHU1NDBkIiwiaHRtbElEIjoiZG9tYWluTmFtZUFkZCIsInVybCI6Ii9kb21haW5OYW1lTWFuYWdlci9kb21haW5OYW1lQWRkLyIsImZhdGhlcklEIjoxOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiZG9tYWluTmFtZUxpc3QgZG9tYWluTmFtZUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjE5fSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU3YmExXHU3NDA2IiwiaHRtbElEIjoiY29uZmlnTWFuYWdlciIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTWFuYWdlciIsImljb24iOiJmYS13cmVuY2gifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIwfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU5MTRkXHU3ZjZlXHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiY29uZmlnTGlzdCIsInVybCI6Ii9jb25maWdNYW5hZ2VyL2NvbmZpZ0xpc3QvIiwiZmF0aGVySUQiOjIwLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJjb25maWdMaXN0IGNvbmZpZ0FkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjIxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU5MTRkXHU3ZjZlIiwiaHRtbElEIjoiY29uZmlnQWRkIiwidXJsIjoiL2NvbmZpZ01hbmFnZXIvY29uZmlnQWRkLyIsImZhdGhlcklEIjoyMSwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiY29uZmlnTGlzdCBjb25maWdBZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyMn0seyJmaWVsZHMiOnsibmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsImh0bWxJRCI6ImF1dGgiLCJ1cmwiOiIjIiwiZmF0aGVySUQiOjAsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImF1dGgiLCJpY29uIjoiZmEtYmFuIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOH0seyJmaWVsZHMiOnsibmFtZSI6Ilx1ODNkY1x1NTM1NVx1NTIxN1x1ODg2OCIsImh0bWxJRCI6Im1lbnVBZG1pbkxpc3QiLCJ1cmwiOiIvYXV0aC9tZW51QWRtaW5MaXN0LyIsImZhdGhlcklEIjoyOCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoibWVudUFkbWluTGlzdCBtZW51QWRtaW5BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjoyOX0seyJmaWVsZHMiOnsibmFtZSI6Ilx1NmRmYlx1NTJhMFx1ODNkY1x1NTM1NSIsImh0bWxJRCI6Im1lbnVBZG1pbkFkZCIsInVybCI6Ii9hdXRoL21lbnVBZG1pbkFkZC8iLCJmYXRoZXJJRCI6MjksImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6Im1lbnVBZG1pbkxpc3QgbWVudUFkbWluQWRkIiwiaWNvbiI6IiJ9LCJtb2RlbCI6Im1lbnVBdXRoLm1lbnUiLCJwayI6MzB9LHsiZmllbGRzIjp7Im5hbWUiOiJcdTU0NGFcdThiNjZcdTdiYTFcdTc0MDYiLCJodG1sSUQiOiJhbGFybSIsInVybCI6IiMiLCJmYXRoZXJJRCI6MCwiYXZhaWxhYml0eSI6MSwiaHRtbENsYXNzIjoiYWxhcm0iLCJpY29uIjoiZmEtYnVsbGhvcm4ifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMxfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU4OWM0XHU1MjE5XHU1MjE3XHU4ODY4IiwiaHRtbElEIjoiYWxhcm1MaXN0IiwidXJsIjoiL2FsYXJtL2FsYXJtTGlzdC8iLCJmYXRoZXJJRCI6MzEsImF2YWlsYWJpdHkiOjEsImh0bWxDbGFzcyI6ImFsYXJtTGlzdCBhbGFybUFkZCIsImljb24iOiIifSwibW9kZWwiOiJtZW51QXV0aC5tZW51IiwicGsiOjMyfSx7ImZpZWxkcyI6eyJuYW1lIjoiXHU2ZGZiXHU1MmEwXHU4OWM0XHU1MjE5IiwiaHRtbElEIjoiYWxhcm1BZGQiLCJ1cmwiOiIvYWxhcm0vYWxhcm1BZGQvIiwiZmF0aGVySUQiOjMyLCJhdmFpbGFiaXR5IjoxLCJodG1sQ2xhc3MiOiJhbGFybUxpc3QgYWxhcm1BZGQiLCJpY29uIjoiIn0sIm1vZGVsIjoibWVudUF1dGgubWVudSIsInBrIjozM31dfQ==','2017-10-10 07:38:27');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `domainName`
--

DROP TABLE IF EXISTS `domainName`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domainName` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `nameDistributor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `exptresDate` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `user` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `organization` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `availabity` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domainName_name_136698b4b4d59d4_uniq` (`name`,`availabity`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domainName`
--

LOCK TABLES `domainName` WRITE;
/*!40000 ALTER TABLE `domainName` DISABLE KEYS */;
INSERT INTO `domainName` VALUES (1,'9187.cn','','','','','',1);
/*!40000 ALTER TABLE `domainName` ENABLE KEYS */;
UNLOCK TABLES;

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
  `htmlClass` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
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

--
-- Table structure for table `myUser`
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
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myUser`
--

LOCK TABLES `myUser` WRITE;
/*!40000 ALTER TABLE `myUser` DISABLE KEYS */;
INSERT INTO `myUser` VALUES (1,'pbkdf2_sha256$20000$DYS1J412ozE5$8jxicCjxDxS7SO+nD0nv5pZAbn4kwIsgHECLtfK2h/0=','2017-06-12 08:59:23',1,'cmdbAdmin','系统管理员','','',1,1,'2017-03-28 08:12:21','','','',1,1),(16,'pbkdf2_sha256$20000$PilUSAwLBlKh$4IeaJRkgAWwbTNGOYLpy+uNiq59v0USSYMp1IMQfC1E=','2017-09-26 07:38:27',1,'dkm','','','evan886@gmail.com',1,1,'2017-06-12 08:44:30','','','',1,1);
/*!40000 ALTER TABLE `myUser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myUser_auth`
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
) ENGINE=MyISAM AUTO_INCREMENT=206 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myUser_auth`
--

LOCK TABLES `myUser_auth` WRITE;
/*!40000 ALTER TABLE `myUser_auth` DISABLE KEYS */;
INSERT INTO `myUser_auth` VALUES (153,1,1),(154,1,34),(155,1,2),(156,1,3),(157,1,5),(158,1,7),(159,1,9),(160,1,10),(161,1,11),(162,1,12),(163,1,13),(164,1,14),(165,1,15),(166,1,16),(167,1,17),(168,1,18),(169,1,19),(170,1,20),(171,1,21),(172,1,22),(173,1,23),(174,1,24),(175,1,25),(176,1,26),(177,1,27),(178,1,28),(179,1,29),(180,1,30),(181,1,31),(182,1,32),(183,1,33),(184,16,2),(185,16,3),(186,16,5),(187,16,7),(188,16,9),(189,16,10),(190,16,11),(191,16,12),(192,16,13),(193,16,14),(194,16,17),(195,16,18),(196,16,19),(197,16,20),(198,16,21),(199,16,22),(200,16,28),(201,16,29),(202,16,30),(203,16,31),(204,16,32),(205,16,33);
/*!40000 ALTER TABLE `myUser_auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myUser_groups`
--

DROP TABLE IF EXISTS `myUser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myUser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`group_id`),
  KEY `myUser_groups_8b14fb18` (`myuser_id`),
  KEY `myUser_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myUser_groups`
--

LOCK TABLES `myUser_groups` WRITE;
/*!40000 ALTER TABLE `myUser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `myUser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myUser_user_permissions`
--

DROP TABLE IF EXISTS `myUser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `myUser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myuser_id` (`myuser_id`,`permission_id`),
  KEY `myUser_user_permissions_8b14fb18` (`myuser_id`),
  KEY `myUser_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myUser_user_permissions`
--

LOCK TABLES `myUser_user_permissions` WRITE;
/*!40000 ALTER TABLE `myUser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `myUser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tastypie_apiaccess`
--

DROP TABLE IF EXISTS `tastypie_apiaccess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tastypie_apiaccess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifier` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `request_method` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `accessed` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apiaccess`
--

LOCK TABLES `tastypie_apiaccess` WRITE;
/*!40000 ALTER TABLE `tastypie_apiaccess` DISABLE KEYS */;
/*!40000 ALTER TABLE `tastypie_apiaccess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tastypie_apikey`
--

DROP TABLE IF EXISTS `tastypie_apikey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tastypie_apikey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `tastypie_apikey_3c6e0b8a` (`key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apikey`
--

LOCK TABLES `tastypie_apikey` WRITE;
/*!40000 ALTER TABLE `tastypie_apikey` DISABLE KEYS */;
/*!40000 ALTER TABLE `tastypie_apikey` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-26 16:33:58
