-- LEGACY DATABASE SCHEMA
-- Code Smell: Poor naming conventions, inconsistent field names
-- Architectural Issue: Tight coupling between tables, circular dependencies
-- Issue: No proper normalization in some places

DROP DATABASE IF EXISTS airport_db;

CREATE DATABASE airport_db;

USE airport_db;

DROP TABLE IF EXISTS `Airline`;

CREATE TABLE `Airline` (
  `IATA airline designators` char(2) PRIMARY KEY,
  `Company Name` varchar(50) NOT NULL,
  `num_aircrafts_owned` int DEFAULT 0,
  `is_active` Boolean DEFAULT TRUE,
  `country_of_ownership` varchar(255)
);

DROP TABLE IF EXISTS `capacity_of_aircraft`;

CREATE TABLE `capacity_of_aircraft` (
  `Manufacturer` varchar(255) NOT NULL,
  `Model` varchar(255) NOT NULL,
  `Capacity` int NOT NULL,
  constraint capacityKey PRIMARY KEY (`Model`,`Manufacturer` )
);

DROP TABLE IF EXISTS `Aircraft`;

CREATE TABLE `Aircraft` (
  `registration_num` int PRIMARY KEY,
  `fk_to_capacity_Manufacturer` varchar(255) NOT NULL,
  `fk_to_capacity_Model` varchar(255) NOT NULL,
  `Distance Travelled` int DEFAULT 0,
  `Flight ID` varchar(10),
  `Maintanence check date` date,
  `fk_to_airline_owner_airline_IATA_code` char(2),

  FOREIGN KEY (`fk_to_capacity_Model`,`fk_to_capacity_Manufacturer`) REFERENCES `capacity_of_aircraft` (`Model`,`Manufacturer`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`fk_to_airline_owner_airline_IATA_code`) REFERENCES `Airline` (`IATA airline designators`) ON DELETE SET NULL ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Airport`;

CREATE TABLE `Airport` (
  `IATA airport codes` varchar(3) PRIMARY KEY,
  `Altitude` float,
  `Time Zone` char(6),
  `Airport Name` varchar(255),
  `City` varchar(255),
  `Country` varchar(255),
  `Latitude` float,
  `Longitude` float
);

DROP TABLE IF EXISTS `Runway`;

CREATE TABLE `Runway` (
  `fk_to_airport_IATA_airport_codes` char(3),
  `Runway ID` int,
  `length_ft` float,
  `width_ft` float,
  `Status` enum('Assigned', 'Available', 'Disfunctional') DEFAULT 'Available',
  PRIMARY KEY (`fk_to_airport_IATA_airport_codes`, `Runway ID`),

  FOREIGN KEY (`fk_to_airport_IATA_airport_codes`) REFERENCES `Airport` (`IATA airport codes`) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `Terminal`;

CREATE TABLE `Terminal` (
  `fk_to_airport_IATA_airport_codes` char(3),
  `Terminal ID` int,
  `Airplane Handling capacity` int,
  `Floor Area` float,
  PRIMARY KEY (`fk_to_airport_IATA_airport_codes`, `Terminal ID`),

  FOREIGN KEY (`fk_to_airport_IATA_airport_codes`) REFERENCES `Airport` (`IATA airport codes`) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS `boarding_pass`;

CREATE TABLE `boarding_pass` (
  `Barcode number` char(12) PRIMARY KEY,
  `fk_PNR_number` char(6) NOT NULL,
  `Seat` varchar(5) NOT NULL,
  `fk_to_passenger_Aadhar_card_number` char(12) NOT NULL,
  `fk_to_route_Route ID` int NOT NULL
);

DROP TABLE IF EXISTS `Passenger`;

CREATE TABLE `Passenger` (
  `Aadhar_card_number` char(12) PRIMARY KEY,
  `First Name` varchar(255) NOT NULL,
  `Middle Name` varchar(255),
  `Last Name` varchar(255),
  `DOB` date,
  `Gender` enum('Male', 'Female', 'Others'),
  `Email-ID` varchar(255) UNIQUE,
  `Nationality` varchar(255)
);

DROP TABLE IF EXISTS `airline_crew`;

CREATE TABLE `airline_crew` (
  `Aadhar_card_number` char(12) PRIMARY KEY,
  `First Name` varchar(255) NOT NULL,
  `Middle Name` varchar(255),
  `Last Name` varchar(255),
  `Salary` int,
  `Nationality` varchar(255),
  `DOB` date,
  `Gender` enum('Male', 'Female', 'Others'),
  `fk_to_airline_employer_IATA_code` char(2),
  FOREIGN KEY (`fk_to_airline_employer_IATA_code`) REFERENCES `Airline` (`IATA airline designators`) ON DELETE SET NULL ON UPDATE CASCADE
);