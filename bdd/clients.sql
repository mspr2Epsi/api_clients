-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 13, 2024 at 01:33 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mspr2`
--

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
CREATE TABLE IF NOT EXISTS `clients` (
  `ClientID` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) DEFAULT NULL,
  `Prenom` varchar(255) DEFAULT NULL,
  `Telephone` int DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Adresse` varchar(255) DEFAULT NULL,
  `RoleID` int DEFAULT NULL,
  PRIMARY KEY (`ClientID`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`ClientID`, `Nom`, `Prenom`, `Telephone`, `Age`, `Email`, `Adresse`, `RoleID`) VALUES
(1, 'Smith', 'Alice', 1234567890, 25, 'alice.smith@example.com', '123 Main St', 1),
(2, 'Johnson', 'Bob', 2147483647, 42, 'bob.johnson@example.com', '456 Elm St', 2),
(3, 'Williams', 'Eva', 2147483647, 30, 'eva.williams@example.com', '789 Oak St', 1),
(4, 'Brown', 'Michael', 2147483647, 35, 'michael.brown@example.com', '1011 Pine St', 3),
(5, 'Jones', 'Sophie', 2147483647, 28, 'sophie.jones@example.com', '1213 Cedar St', 2),
(6, 'Garcia', 'David', 2147483647, 48, 'david.garcia@example.com', '1415 Maple St', 1),
(7, 'Miller', 'Emma', 2147483647, 33, 'emma.miller@example.com', '1617 Birch St', 2),
(8, 'Davis', 'Alex', 2147483647, 22, 'alex.davis@example.com', '1819 Walnut St', 3),
(9, 'Rodriguez', 'Laura', 2147483647, 40, 'laura.rodriguez@example.com', '2021 Cherry St', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
