-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema crimesdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema crimesdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `crimesdb` DEFAULT CHARACTER SET utf8 ;
USE `crimesdb` ;

-- -----------------------------------------------------
-- Table `crimesdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crimesdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pw_hash` VARCHAR(255) NULL,
  `name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crimesdb`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crimesdb`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  `location` VARCHAR(255) NULL,
  `updated_at` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_favorites_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `crimesdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
