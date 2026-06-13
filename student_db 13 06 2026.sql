-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 13, 2026 at 11:33 AM
-- Server version: 9.1.0
-- PHP Version: 8.1.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `course`, `created_at`) VALUES
(5, 'asdfsadfsdfasdfa', 'fsd@adf.dfhdgh', 'dsfgsdfgdfg', '2026-06-12 12:47:43'),
(2, 'Rahullll', 'rahulllll@gmail.com', 'Python', '2026-06-12 12:05:36'),
(3, 'Akash', 'Akash@gmail.com', 'Web Developement', '2026-06-12 12:05:36'),
(6, 'bb', 'bb@gmail.com', 'Java', '2026-06-12 12:47:57'),
(7, 'cc', 'cc@gmail.com', 'PHP', '2026-06-12 12:48:10'),
(8, 'asdf', 'asdf@gmail.com', 'Java', '2026-06-12 12:50:10');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'abc', 'abc@gmail.com', 'scrypt:32768:8:1$UY5bDZOiqV3v1pHt$87cb35603265c1e5238fff4443259d6f4c68dcd90598012082062fe5b6c8d2dc47077668f0c2193bcb35b9684639a88a496a067c3c308a02aabff844984eb85f'),
(2, 'pqr', 'prq@gmail.com', 'scrypt:32768:8:1$pkKfUlxX6KWF8ZFm$e54cd2d94c739090f7ee272c2451c8f5b29314f59fea9e9b772966a123618a6f94a03f0f01deb976c73cfd47141f5857e740f68a30c233932bb997b594ea8258'),
(3, 'xyz', 'xyz@gmail.com', 'scrypt:32768:8:1$lOfVygQN4Tz4yFs1$a2575f5cdcca0b5b956c00445dd5cc2a068c233a25c9babeda58fbf5c145b63e362d4692224690d0fc48430cd30dc11da6024a9ab32aca0f85898ebb867c5504'),
(4, 'ram', 'ram@gmail.com', 'scrypt:32768:8:1$rEXTpdFgTo8fgUEq$8dbc2d1756efd3762567d79b9c8b031a327e58e967d10aab03f3aa7c3bab9194f27275e373a82ad1c28dc6a4666b164aad509e9f575e6ffb9e75d992fc033ece'),
(5, 'shyam', 'shyam@gmail.com', 'scrypt:32768:8:1$HbxexycS8yybq5mn$5b8e623c604f21e4ca827da05de2dc8d576a8aede5b1edf0b7295c71d4d0648d8b1494e140b76e2c8540b341ac667019ec1d18d4ec555e8efbd18eba88b2954e');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
