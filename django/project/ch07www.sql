-- MySQL dump 10.13  Distrib 5.6.30, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ch07www
-- ------------------------------------------------------
-- Server version	5.6.30-1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add maker',7,'add_maker'),(20,'Can change maker',7,'change_maker'),(21,'Can delete maker',7,'delete_maker'),(22,'Can add p model',8,'add_pmodel'),(23,'Can change p model',8,'change_pmodel'),(24,'Can delete p model',8,'delete_pmodel'),(25,'Can add product',9,'add_product'),(26,'Can change product',9,'change_product'),(27,'Can delete product',9,'delete_product'),(28,'Can add p photo',10,'add_pphoto'),(29,'Can change p photo',10,'change_pphoto'),(30,'Can delete p photo',10,'delete_pphoto');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$ZnCgHmIYGShm$++0hLV9vRqcnLgICxuzPq1/tLUGKTCi9593baPly5y0=','2017-09-25 10:05:44.562052',1,'admin','','','evan886@gmail.com',1,1,'2017-09-19 09:22:25.998226'),(4,'pbkdf2_sha256$20000$cxpOV3gVZ98b$iuYu0JzTF00dzhqjX/HaA0a7PTU7DpNw4w8VUQ7jP0I=','2017-09-25 10:03:01.508820',1,'eva','','','evan886@gmail.com',1,1,'2017-09-25 10:02:48.701453'),(5,'pbkdf2_sha256$36000$Rw6Kct79COML$+l+rUm/tareFaCX179ibYk35rV96MzmVUnyCzPE7rZY=',NULL,1,'evan','','','evan886@gmail.com',1,1,'2017-09-25 10:04:27.237185');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-09-25 10:04:11.621803','3','evan',3,'',4,4),(2,'2017-09-25 10:04:56.120668','1','admin',2,'已修改 password 。',4,4);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'mysite','maker'),(8,'mysite','pmodel'),(10,'mysite','pphoto'),(9,'mysite','product'),(6,'sessions','session');
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
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-09-19 08:50:36.443642'),(2,'auth','0001_initial','2017-09-19 08:50:41.765145'),(3,'admin','0001_initial','2017-09-19 08:50:43.268812'),(4,'contenttypes','0002_remove_content_type_name','2017-09-19 08:50:44.105580'),(5,'auth','0002_alter_permission_name_max_length','2017-09-19 08:50:44.582754'),(6,'auth','0003_alter_user_email_max_length','2017-09-19 08:50:45.136845'),(7,'auth','0004_alter_user_username_opts','2017-09-19 08:50:45.175813'),(8,'auth','0005_alter_user_last_login_null','2017-09-19 08:50:45.587055'),(9,'auth','0006_require_contenttypes_0002','2017-09-19 08:50:45.619620'),(10,'mysite','0001_initial','2017-09-19 08:50:48.722686'),(11,'sessions','0001_initial','2017-09-19 08:50:49.107789'),(12,'admin','0002_logentry_remove_auto_add','2017-09-25 09:54:53.149289'),(13,'auth','0007_alter_validators_add_error_messages','2017-09-25 09:54:53.224611'),(14,'auth','0008_alter_user_username_max_length','2017-09-25 09:54:54.002213'),(15,'mysite','0002_auto_20170925_1757','2017-09-25 09:58:04.232910');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('aq8br6k6mh9a36ci8k622ruswuid83l5','ZDI3YmQzODEyZTEwNTUzYTcyMmE1NTNkODhhNmFhZDE0ZmIwMjZjNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ1ZWEwMWNhMjgxNjM0MmE1M2FkYmJkNWI3YWVhNDhkZTRjNTc3MTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-10-03 09:23:04.245823'),('pfsp67xmg71mf3ylbst0zpbkhlnux3il','NGUyZTIwMDg1N2E3NWRlODJkZGNhNDZhMWVhMWVkMjk1YjgwNWY0ODp7Il9hdXRoX3VzZXJfaGFzaCI6IjJkMWNkNWVjZGJkNGZlNGI1ODQwZTA4M2ZlNWQ3ZmE5MmE1ZmMyMjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-10-09 10:05:44.621081');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_maker`
--

DROP TABLE IF EXISTS `mysite_maker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_maker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `country` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_maker`
--

LOCK TABLES `mysite_maker` WRITE;
/*!40000 ALTER TABLE `mysite_maker` DISABLE KEYS */;
INSERT INTO `mysite_maker` VALUES (1,'ASUS','Taiwan'),(2,'HTC','Taiwan'),(3,'SONY','Japan'),(4,'Apple','USA'),(5,'Nokia','Finland'),(6,'Infocus','Taiwan'),(7,'Samsung','Korea');
/*!40000 ALTER TABLE `mysite_maker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_pmodel`
--

DROP TABLE IF EXISTS `mysite_pmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_pmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `maker_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mysite_pmodel_maker_id_4a25f5379a47611_fk_mysite_maker_id` (`maker_id`),
  CONSTRAINT `mysite_pmodel_maker_id_4a25f5379a47611_fk_mysite_maker_id` FOREIGN KEY (`maker_id`) REFERENCES `mysite_maker` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_pmodel`
--

LOCK TABLES `mysite_pmodel` WRITE;
/*!40000 ALTER TABLE `mysite_pmodel` DISABLE KEYS */;
INSERT INTO `mysite_pmodel` VALUES (1,'XM 5800','http://www.sogi.com.tw/products/NOKIA_5800_XpressMusic/4464',5),(2,'Zenfone 2','https://www.asus.com/tw/Phone/ZenFone_2_ZE551ML/',1),(3,'M370','http://www.infocusphone.com/tw/product/M370/',6),(4,'DUOS','http://www.samsung.com/hk/consumer/mobile/mobile-phones/smartphone/GT-S7562UWATGY',7),(5,'Xperia TX','http://store.sony.com.tw/product/LT29i',3),(6,'S3','http://www.eprice.com.tw/mobile/intro/c01-p4555-samsung-galaxy-s3-16gb/',7),(7,'Xperia Z3','http://www.sonymobile.com/tw/products/phones/xperia-z3/',3);
/*!40000 ALTER TABLE `mysite_pmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_pphoto`
--

DROP TABLE IF EXISTS `mysite_pphoto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_pphoto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `produce_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mysite_pphoto_b1256499` (`produce_id`),
  CONSTRAINT `mysite_pphoto_produce_id_67e67eae831fb0fe_fk_mysite_product_id` FOREIGN KEY (`produce_id`) REFERENCES `mysite_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_pphoto`
--

LOCK TABLES `mysite_pphoto` WRITE;
/*!40000 ALTER TABLE `mysite_pphoto` DISABLE KEYS */;
INSERT INTO `mysite_pphoto` VALUES (1,'S3正面照片','http://i.imgur.com/zamweOK.jpg',1),(2,'S3背面照片','http://i.imgur.com/vg34aYM.jpg',1),(3,'Nokia 5800正面照','http://i.imgur.com/qDbAzoe.jpg',4),(4,'Nokia 5800背面照','http://i.imgur.com/9rFsffi.jpg',4),(5,'SONY TX正面照','http://i.imgur.com/OEOTvmy.jpg',5),(6,'SONY TX背面照(含保護殻）','http://i.imgur.com/uX2Kmpy.jpg',5);
/*!40000 ALTER TABLE `mysite_pphoto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_product`
--

DROP TABLE IF EXISTS `mysite_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(15) NOT NULL,
  `description` longtext NOT NULL,
  `year` int(10) unsigned NOT NULL,
  `price` int(10) unsigned NOT NULL,
  `pmodel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mysite_product_pmodel_id_5ac6d1ac_fk_mysite_pmodel_id` (`pmodel_id`),
  CONSTRAINT `mysite_product_pmodel_id_5ac6d1ac_fk_mysite_pmodel_id` FOREIGN KEY (`pmodel_id`) REFERENCES `mysite_pmodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_product`
--

LOCK TABLES `mysite_product` WRITE;
/*!40000 ALTER TABLE `mysite_product` DISABLE KEYS */;
INSERT INTO `mysite_product` VALUES (1,'S3零件機便宜賣','功能正常，但是螢幕摔裂了，十分可惜。',2010,500,6),(2,'4G不錯用備用機','暫無說明',2015,1000,3),(3,'古董二手機三星雙卡機','功能正常，便宜賣',2013,100,4),(4,'Nokia舊機俗俗賣','功能均正常，可當備用機使用。\r\n支援3G SIM小卡',2010,150,1),(5,'SONY TX白色舊機','老旗艦機，但功能正常，而且有6成新的保護殻',2013,2500,5);
/*!40000 ALTER TABLE `mysite_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-27 14:24:39
