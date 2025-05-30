-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema el_camino
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema el_camino
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `el_camino` DEFAULT CHARACTER SET utf8 ;
USE `el_camino` ;

-- -----------------------------------------------------
-- Table `el_camino`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`cliente` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`habitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`habitacion` (
  `idhabitacion` INT NOT NULL AUTO_INCREMENT,
  `capacidad` INT NOT NULL,
  `estado` ENUM('Ocupada', 'Disponible') NULL DEFAULT 'Disponible',
  PRIMARY KEY (`idhabitacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`empleados` (
  `idempleados` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `telefono` VARCHAR(13) NULL,
  PRIMARY KEY (`idempleados`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`fallecido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`fallecido` (
  `idfallecido` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `hora_muerte` TIMESTAMP NULL,
  `causa_muerte` VARCHAR(45) NULL,
  PRIMARY KEY (`idfallecido`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`funerales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`funerales` (
  `idfunerales` INT NOT NULL AUTO_INCREMENT,
  `fecha_funeral` TIMESTAMP NOT NULL,
  `lugar` VARCHAR(45) NOT NULL,
  `fallecido_idfallecido` INT NOT NULL,
  PRIMARY KEY (`idfunerales`),
  INDEX `fk_funerales_fallecido1_idx` (`fallecido_idfallecido` ASC) VISIBLE,
  CONSTRAINT `fk_funerales_fallecido1`
    FOREIGN KEY (`fallecido_idfallecido`)
    REFERENCES `el_camino`.`fallecido` (`idfallecido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`empleados_has_funerales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`empleados_has_funerales` (
  `idempleados` INT NOT NULL,
  `idfunerales` INT NOT NULL,
  PRIMARY KEY (`idempleados`, `idfunerales`),
  INDEX `fk_empleados_has_funerales_funerales1_idx` (`idfunerales` ASC) VISIBLE,
  INDEX `fk_empleados_has_funerales_empleados1_idx` (`idempleados` ASC) VISIBLE,
  CONSTRAINT `fk_empleados_has_funerales_empleados1`
    FOREIGN KEY (`idempleados`)
    REFERENCES `el_camino`.`empleados` (`idempleados`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_empleados_has_funerales_funerales1`
    FOREIGN KEY (`idfunerales`)
    REFERENCES `el_camino`.`funerales` (`idfunerales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`contrato` (
  `idcontrato` INT NOT NULL AUTO_INCREMENT,
  `fecha_contrato` TIMESTAMP NULL,
  `idhabitacion` INT NOT NULL,
  `empleados_has_funerales_idempleados` INT NOT NULL,
  `empleados_has_funerales_idfunerales` INT NOT NULL,
  `cliente_idcliente` INT NOT NULL,
  PRIMARY KEY (`idcontrato`),
  INDEX `fk_contrato_habitacion_idx` (`idhabitacion` ASC) VISIBLE,
  INDEX `fk_contrato_empleados_has_funerales1_idx` (`empleados_has_funerales_idempleados` ASC, `empleados_has_funerales_idfunerales` ASC) VISIBLE,
  INDEX `fk_contrato_cliente1_idx` (`cliente_idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_contrato_habitacion`
    FOREIGN KEY (`idhabitacion`)
    REFERENCES `el_camino`.`habitacion` (`idhabitacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contrato_empleados_has_funerales1`
    FOREIGN KEY (`empleados_has_funerales_idempleados` , `empleados_has_funerales_idfunerales`)
    REFERENCES `el_camino`.`empleados_has_funerales` (`idempleados` , `idfunerales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contrato_cliente1`
    FOREIGN KEY (`cliente_idcliente`)
    REFERENCES `el_camino`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `el_camino`.`factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `el_camino`.`factura` (
  `idfactura` INT NOT NULL AUTO_INCREMENT,
  `contrato_idcontrato` INT NOT NULL,
  `cliente_idcliente` INT NOT NULL,
  PRIMARY KEY (`idfactura`),
  INDEX `fk_factura_contrato1_idx` (`contrato_idcontrato` ASC) VISIBLE,
  INDEX `fk_factura_cliente1_idx` (`cliente_idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_factura_contrato1`
    FOREIGN KEY (`contrato_idcontrato`)
    REFERENCES `el_camino`.`contrato` (`idcontrato`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_factura_cliente1`
    FOREIGN KEY (`cliente_idcliente`)
    REFERENCES `el_camino`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
