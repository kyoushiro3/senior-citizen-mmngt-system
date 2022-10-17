-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2022 at 03:37 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test7`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add family', 1, 'add_family'),
(2, 'Can change family', 1, 'change_family'),
(3, 'Can delete family', 1, 'delete_family'),
(4, 'Can view family', 1, 'view_family'),
(5, 'Can add member', 2, 'add_member'),
(6, 'Can change member', 2, 'change_member'),
(7, 'Can delete member', 2, 'delete_member'),
(8, 'Can view member', 2, 'view_member'),
(9, 'Can add user profile', 3, 'add_userprofile'),
(10, 'Can change user profile', 3, 'change_userprofile'),
(11, 'Can delete user profile', 3, 'delete_userprofile'),
(12, 'Can view user profile', 3, 'view_userprofile'),
(13, 'Can add barangay user', 4, 'add_barangayuser'),
(14, 'Can change barangay user', 4, 'change_barangayuser'),
(15, 'Can delete barangay user', 4, 'delete_barangayuser'),
(16, 'Can view barangay user', 4, 'view_barangayuser'),
(17, 'Can add bookmark', 5, 'add_bookmark'),
(18, 'Can change bookmark', 5, 'change_bookmark'),
(19, 'Can delete bookmark', 5, 'delete_bookmark'),
(20, 'Can view bookmark', 5, 'view_bookmark'),
(21, 'Can add pinned application', 6, 'add_pinnedapplication'),
(22, 'Can change pinned application', 6, 'change_pinnedapplication'),
(23, 'Can delete pinned application', 6, 'delete_pinnedapplication'),
(24, 'Can view pinned application', 6, 'view_pinnedapplication'),
(25, 'Can add user dashboard module', 7, 'add_userdashboardmodule'),
(26, 'Can change user dashboard module', 7, 'change_userdashboardmodule'),
(27, 'Can delete user dashboard module', 7, 'delete_userdashboardmodule'),
(28, 'Can view user dashboard module', 7, 'view_userdashboardmodule'),
(29, 'Can add Token', 8, 'add_token'),
(30, 'Can change Token', 8, 'change_token'),
(31, 'Can delete Token', 8, 'delete_token'),
(32, 'Can view Token', 8, 'view_token'),
(33, 'Can add token', 9, 'add_tokenproxy'),
(34, 'Can change token', 9, 'change_tokenproxy'),
(35, 'Can delete token', 9, 'delete_tokenproxy'),
(36, 'Can view token', 9, 'view_tokenproxy'),
(37, 'Can add log entry', 10, 'add_logentry'),
(38, 'Can change log entry', 10, 'change_logentry'),
(39, 'Can delete log entry', 10, 'delete_logentry'),
(40, 'Can view log entry', 10, 'view_logentry'),
(41, 'Can add permission', 11, 'add_permission'),
(42, 'Can change permission', 11, 'change_permission'),
(43, 'Can delete permission', 11, 'delete_permission'),
(44, 'Can view permission', 11, 'view_permission'),
(45, 'Can add group', 12, 'add_group'),
(46, 'Can change group', 12, 'change_group'),
(47, 'Can delete group', 12, 'delete_group'),
(48, 'Can view group', 12, 'view_group'),
(49, 'Can add user', 13, 'add_user'),
(50, 'Can change user', 13, 'change_user'),
(51, 'Can delete user', 13, 'delete_user'),
(52, 'Can view user', 13, 'view_user'),
(53, 'Can add content type', 14, 'add_contenttype'),
(54, 'Can change content type', 14, 'change_contenttype'),
(55, 'Can delete content type', 14, 'delete_contenttype'),
(56, 'Can view content type', 14, 'view_contenttype'),
(57, 'Can add session', 15, 'add_session'),
(58, 'Can change session', 15, 'change_session'),
(59, 'Can delete session', 15, 'delete_session'),
(60, 'Can view session', 15, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$rmmO0GchgzdGW8sa1J61FK$TFibmbtG+93hPPmkbxT9xjwocu/eA925gFra4ea+4ho=', '2022-01-14 13:51:57.252782', 0, 'kimdarren', '', '', 'kimpopsicleee147@outlook.com', 0, 1, '2022-01-14 12:50:06.434192'),
(2, 'pbkdf2_sha256$260000$DrkVQNV6KvA170iSHh0cr6$Xl7koRzrcBb6h9zlZjlQXYaLgXIwZL2XExRb2xjWUFc=', '2022-01-14 12:52:02.137340', 0, 'admin', '', '', 'devisa1341@wolfpat.com', 0, 1, '2022-01-14 12:51:43.477291'),
(3, 'pbkdf2_sha256$260000$9jo3Y3sfypZ3tGzCyVeJ4j$v/S5eT5DT0YWBcjDKgYsbsVtC8ztsZWYBUXCat1Le0Q=', '2022-01-14 13:54:07.404651', 0, 'sanjose', '', '', 'kimpopsicleee147@outlook.com', 0, 1, '2022-01-14 12:54:43.636380'),
(4, 'pbkdf2_sha256$260000$MksxjmFOAUIQ7vbQUeebXS$CUlInF9aRZqUkeJNWG2z+CkPd7SiPTZZOx7umXAn0zk=', '2022-01-14 14:14:35.121328', 0, 'Calayan', '', '', 'devisa1341@wolfpat.com', 0, 1, '2022-01-14 13:57:56.244357');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_userdashboardmodule`
--

CREATE TABLE `dashboard_userdashboardmodule` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `app_label` varchar(255) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `column` int(10) UNSIGNED NOT NULL CHECK (`column` >= 0),
  `order` int(11) NOT NULL,
  `settings` longtext NOT NULL,
  `children` longtext NOT NULL,
  `collapsed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(10, 'admin', 'logentry'),
(12, 'auth', 'group'),
(11, 'auth', 'permission'),
(13, 'auth', 'user'),
(8, 'authtoken', 'token'),
(9, 'authtoken', 'tokenproxy'),
(14, 'contenttypes', 'contenttype'),
(7, 'dashboard', 'userdashboardmodule'),
(5, 'jet', 'bookmark'),
(6, 'jet', 'pinnedapplication'),
(15, 'sessions', 'session'),
(4, 'user', 'barangayuser'),
(1, 'user', 'family'),
(2, 'user', 'member'),
(3, 'user', 'userprofile');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-01-14 12:47:38.841397'),
(2, 'auth', '0001_initial', '2022-01-14 12:47:39.527001'),
(3, 'admin', '0001_initial', '2022-01-14 12:47:39.879364'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-01-14 12:47:39.891333'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-01-14 12:47:39.903055'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-01-14 12:47:39.979266'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-01-14 12:47:40.039469'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-01-14 12:47:40.062138'),
(9, 'auth', '0004_alter_user_username_opts', '2022-01-14 12:47:40.073099'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-01-14 12:47:40.136043'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-01-14 12:47:40.140030'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-01-14 12:47:40.152041'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-01-14 12:47:40.176540'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-01-14 12:47:40.199344'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-01-14 12:47:40.222364'),
(16, 'auth', '0011_update_proxy_permissions', '2022-01-14 12:47:40.235128'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-01-14 12:47:40.257853'),
(18, 'authtoken', '0001_initial', '2022-01-14 12:47:40.364577'),
(19, 'authtoken', '0002_auto_20160226_1747', '2022-01-14 12:47:40.394526'),
(20, 'authtoken', '0003_tokenproxy', '2022-01-14 12:47:40.400640'),
(21, 'dashboard', '0001_initial', '2022-01-14 12:47:40.446898'),
(22, 'dashboard', '0002_auto_20201228_1929', '2022-01-14 12:47:40.667279'),
(23, 'dashboard', '0003_alter_userdashboardmodule_id', '2022-01-14 12:47:40.736162'),
(24, 'jet', '0001_initial', '2022-01-14 12:47:40.885933'),
(25, 'jet', '0002_delete_userdashboardmodule', '2022-01-14 12:47:40.904907'),
(26, 'jet', '0003_auto_20201228_1540', '2022-01-14 12:47:41.175170'),
(27, 'jet', '0004_auto_20201228_1802', '2022-01-14 12:47:41.531128'),
(28, 'jet', '0005_auto_20220111_0940', '2022-01-14 12:47:41.751669'),
(29, 'sessions', '0001_initial', '2022-01-14 12:47:41.836442'),
(30, 'user', '0001_initial', '2022-01-14 12:47:42.430033'),
(31, 'user', '0002_auto_20220114_0924', '2022-01-14 12:47:42.640335'),
(32, 'user', '0003_alter_member_managers', '2022-01-14 12:47:42.653151'),
(33, 'user', '0004_auto_20220114_1209', '2022-01-14 12:47:42.854965'),
(34, 'user', '0005_auto_20220114_1214', '2022-01-14 12:47:42.912806'),
(35, 'user', '0006_auto_20220114_1240', '2022-01-14 12:47:43.177103'),
(36, 'user', '0007_auto_20220114_1437', '2022-01-14 12:47:43.645500'),
(37, 'user', '0008_member_password', '2022-01-14 12:47:43.711356'),
(38, 'user', '0009_alter_member_user_status', '2022-01-14 12:47:43.797332'),
(39, 'user', '0010_barangayuser_barangayid', '2022-01-14 12:47:43.936440'),
(40, 'user', '0011_auto_20220114_1725', '2022-01-14 12:47:44.444791'),
(41, 'user', '0012_alter_member_barangay', '2022-01-14 12:47:44.594753'),
(42, 'user', '0013_alter_userprofile_user_role', '2022-01-14 12:53:47.501235');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5wo432anvilbreqyyd1528jsh1x0gvwj', 'e30:1n8NKP:KH-RgamB7ffFQTMy4wb6xONUW9PN1pkp8XWgamGsZZc', '2022-01-28 14:13:17.105476'),
('8lzarv2ijiogwdzk44khi4jpidgeh2cs', 'e30:1n8NBR:xNNWn9TvfkD-uOqcpBQgFjHvfYfgUkWYov8Qqr24bBE', '2022-01-28 14:04:01.682406'),
('czi5yz14tpaa1fr8acxob7cxmgxn1kp0', 'e30:1n8NJ0:UDJjxCln85wttmm3qW3GYnp3mcaoAD3QheH_cfqdlek', '2022-01-28 14:11:50.036596'),
('eco7bn4azooktec6j8m4czvge6hrtq51', 'e30:1n8M2A:-R9T6XWSnxh2AZPKFOdp2bDu780tfAqzZmO3JfIT26c', '2022-01-28 12:50:22.455836'),
('enylozohdso2j4qpej6dujr3u07q8s68', 'e30:1n8M6b:aDmh51Wdxdj2HSoRDwr0KLbfbRydNdBK1eMU7NdS6B0', '2022-01-28 12:54:57.638572'),
('fmre9xqzhhfkqq3fpc4a92no8bd86p9g', 'e30:1n8N5n:kKozqEva32GMX46QOGXcZ1NH83MA8gY963NtBnx-IFE', '2022-01-28 13:58:11.805675'),
('fwdlhsepsvx1lwbksansqavzpbhj0q8l', 'e30:1n8MAZ:6z7alHPN9abQb75wvorSxFGu2_GY2SF7AYNxyDOgzBM', '2022-01-28 12:59:03.201104'),
('trglxvwatm6w4io3mlagtoqnxpumup6f', 'e30:1n8M3m:qdqIsmAzsgWInDKrMTo8doCWZsTe4Z6a3qZxNj27xYg', '2022-01-28 12:52:02.132605'),
('uiy8gdmzbjd9ehf0l7erb4phynfmizxi', '.eJxVjEsOwiAUAO_C2pCW78Ol-56BwHsgVQNJaVfGuxuSLnQ7M5k38-HYiz962vxK7MoUu_yyGPCZ6hD0CPXeOLa6b2vkI-Gn7XxplF63s_0blNDL2EaY0AJFSc6qBGaSzjhwDkmQlUrbaEFI0goDwhzQYhJzzoayUpA1-3wB0-E30A:1n8NLf:mM4hSgSTv-M7FI37lz2TuYLKC_KKMkvDbIFnW_5zaMM', '2022-01-28 14:14:35.133721'),
('xgxoc9z9bkr2zbgj9iqv0eiz1edb4866', 'e30:1n8N80:tqyeLxODedDo-AhJoaxzSJDQbdglNl0_U1uTHercPNM', '2022-01-28 14:00:28.177041');

-- --------------------------------------------------------

--
-- Table structure for table `jet_bookmark`
--

CREATE TABLE `jet_bookmark` (
  `id` bigint(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `title` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_add` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `jet_pinnedapplication`
--

CREATE TABLE `jet_pinnedapplication` (
  `id` bigint(20) NOT NULL,
  `app_label` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `date_add` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_members`
--

CREATE TABLE `tbl_members` (
  `id` bigint(20) NOT NULL,
  `fscap_no` varchar(10) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `middle_name` varchar(25) NOT NULL,
  `name_ext` varchar(5) DEFAULT NULL,
  `date_of_birth` date NOT NULL,
  `place_of_birth` varchar(30) NOT NULL,
  `contact_number` bigint(20) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `civil_status` varchar(10) NOT NULL,
  `occupation` varchar(30) NOT NULL,
  `skills` varchar(1000) NOT NULL,
  `annual_income` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_status` varchar(1) DEFAULT NULL,
  `password` varchar(10) NOT NULL,
  `barangay_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_barangayuser`
--

CREATE TABLE `user_barangayuser` (
  `id` bigint(20) NOT NULL,
  `barangay_user_id` int(11) NOT NULL,
  `barangay` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_barangayuser`
--

INSERT INTO `user_barangayuser` (`id`, `barangay_user_id`, `barangay`) VALUES
(1, 3, '2');

-- --------------------------------------------------------

--
-- Table structure for table `user_family`
--

CREATE TABLE `user_family` (
  `id` bigint(20) NOT NULL,
  `name` varchar(25) NOT NULL,
  `age` int(11) NOT NULL,
  `relationship` varchar(15) NOT NULL,
  `civil_status` varchar(10) NOT NULL,
  `occupation` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_userprofile`
--

CREATE TABLE `user_userprofile` (
  `id` bigint(20) NOT NULL,
  `user_role` varchar(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_userprofile`
--

INSERT INTO `user_userprofile` (`id`, `user_role`, `user_id`) VALUES
(1, '0', 1),
(2, '1', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `dashboard_userdashboardmodule`
--
ALTER TABLE `dashboard_userdashboardmodule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dashboard_userdashboardmodule_user_id_97c13132` (`user_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jet_bookmark_user_id_8efdc332` (`user_id`);

--
-- Indexes for table `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jet_pinnedapplication_user_id_7765bcf9` (`user_id`);

--
-- Indexes for table `tbl_members`
--
ALTER TABLE `tbl_members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tbl_members_barangay_id_7b07e7c3_uniq` (`barangay_id`);

--
-- Indexes for table `user_barangayuser`
--
ALTER TABLE `user_barangayuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `barangay_user_id` (`barangay_user_id`);

--
-- Indexes for table `user_family`
--
ALTER TABLE `user_family`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_userprofile`
--
ALTER TABLE `user_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dashboard_userdashboardmodule`
--
ALTER TABLE `dashboard_userdashboardmodule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_members`
--
ALTER TABLE `tbl_members`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_barangayuser`
--
ALTER TABLE `user_barangayuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_family`
--
ALTER TABLE `user_family`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_userprofile`
--
ALTER TABLE `user_userprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `dashboard_userdashboardmodule`
--
ALTER TABLE `dashboard_userdashboardmodule`
  ADD CONSTRAINT `dashboard_userdashboardmodule_user_id_97c13132_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  ADD CONSTRAINT `jet_bookmark_user_id_8efdc332_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  ADD CONSTRAINT `jet_pinnedapplication_user_id_7765bcf9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_members`
--
ALTER TABLE `tbl_members`
  ADD CONSTRAINT `tbl_members_barangay_id_7b07e7c3_fk_user_barangayuser_id` FOREIGN KEY (`barangay_id`) REFERENCES `user_barangayuser` (`id`);

--
-- Constraints for table `user_barangayuser`
--
ALTER TABLE `user_barangayuser`
  ADD CONSTRAINT `user_barangayuser_barangay_user_id_a6d2a65c_fk_auth_user_id` FOREIGN KEY (`barangay_user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `user_userprofile`
--
ALTER TABLE `user_userprofile`
  ADD CONSTRAINT `user_userprofile_user_id_2474538d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
