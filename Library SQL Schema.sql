-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema library
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema library
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `library` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `library` ;

-- -----------------------------------------------------
-- Table `library`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`books` (
  `Accession` VARCHAR(45) NOT NULL,
  `Title` VARCHAR(1000) NOT NULL,
  `Authors` VARCHAR(45) NOT NULL,
  `ISBN` VARCHAR(45) NOT NULL,
  `Publisher` VARCHAR(45) NOT NULL,
  `PublicationYear` INT NOT NULL,
  PRIMARY KEY (`Accession`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library`.`members`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`members` (
  `MemID` VARCHAR(10) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Faculty` VARCHAR(45) NOT NULL,
  `Number` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Fines` INT NOT NULL DEFAULT '0',
  PRIMARY KEY (`MemID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library`.`fines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`fines` (
  `MemID` VARCHAR(10) NOT NULL,
  `PaymentDate` DATETIME NOT NULL,
  `PaidAmount` INT NOT NULL,
  PRIMARY KEY (`MemID`, `PaymentDate`),
  CONSTRAINT `finestomember`
    FOREIGN KEY (`MemID`)
    REFERENCES `library`.`members` (`MemID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `library`.`loans`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`loans` (
  `Accession` VARCHAR(45) NOT NULL,
  `LoanDate` DATE NOT NULL,
  `DueDate` DATE NOT NULL,
  `MemID` VARCHAR(10) NOT NULL,
  `ReturnDate` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`Accession`, `LoanDate`),
  CONSTRAINT `loanstoBook`
    FOREIGN KEY (`Accession`)
    REFERENCES `library`.`books` (`Accession`),
  CONSTRAINT `loanstoMembers`
    FOREIGN KEY (`MemID`)
    REFERENCES `library`.`members` (`MemID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `loanstoMembers_idx` ON `library`.`loans` (`MemID` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `library`.`reservations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`reservations` (
  `Accession` VARCHAR(45) NOT NULL,
  `MemID` VARCHAR(10) NOT NULL,
  `ReserveDate` DATETIME NOT NULL,
  PRIMARY KEY (`Accession`, `MemID`),
  CONSTRAINT `reservationtobooks`
    FOREIGN KEY (`Accession`)
    REFERENCES `library`.`books` (`Accession`),
  CONSTRAINT `reservationtomember`
    FOREIGN KEY (`MemID`)
    REFERENCES `library`.`members` (`MemID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `MemID_idx` ON `library`.`reservations` (`MemID` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
