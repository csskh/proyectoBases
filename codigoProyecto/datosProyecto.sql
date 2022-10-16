#Proyecto 1
#Iris Bejarano
#Alejandro Guillen
#Sebastian Herrera

CREATE DATABASE datosProyecto;

USE  datosProyecto;

CREATE TABLE `rol` (
  `idRol` int NOT NULL,
  `detalle` varchar(50) NOT NULL,
  PRIMARY KEY (`idRol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL,
  `emailUsuario` varchar(50) NOT NULL,
  `contrasena` varchar(50) NOT NULL,
  `idRol` int NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `emailUsuario_UNIQUE` (`emailUsuario`),
  UNIQUE KEY `idUsuario_UNIQUE` (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `escuela` (
  `idEscuela` int NOT NULL AUTO_INCREMENT,
  `codigoEscuela` varchar(2) NOT NULL,
  `nombreEscuela` varchar(50) NOT NULL,
  PRIMARY KEY (`idEscuela`),
  UNIQUE KEY `idEscuela_UNIQUE` (`idEscuela`),
  UNIQUE KEY `codigoEscuela_UNIQUE` (`codigoEscuela`),
  UNIQUE KEY `nombreEscuela_UNIQUE` (`nombreEscuela`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `curso` (
  `idCurso` int NOT NULL AUTO_INCREMENT,
  `nombreEscuela` varchar(50) NOT NULL,
  `nombreCurso` varchar(50) NOT NULL,
  `codigoEscuela` varchar(2) NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  `creditos` int NOT NULL,
  `horas` int NOT NULL,
  PRIMARY KEY (`idCurso`),
  UNIQUE KEY `idCursos_UNIQUE` (`idCurso`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`),
  UNIQUE KEY `nombreCurso_UNIQUE` (`nombreCurso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `correquisito` (
  `idCorrequisito` int NOT NULL AUTO_INCREMENT,
  `nombreEscuela` varchar(50) NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  `codCorrequisito` varchar(6) NOT NULL,
  PRIMARY KEY (`idCorrequisito`),
  UNIQUE KEY `idcorrequisito_UNIQUE` (`idCorrequisito`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`),
  UNIQUE KEY `codCorrequisito_UNIQUE` (`codCorrequisito`),
  UNIQUE KEY `nombreEscuela_UNIQUE` (`nombreEscuela`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `requisito` (
  `idRequisito` int NOT NULL AUTO_INCREMENT,
  `nombreEscuela` varchar(50) NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  `codRequisito` varchar(6) NOT NULL,
  PRIMARY KEY (`idRequisito`),
  UNIQUE KEY `idRequisito_UNIQUE` (`idRequisito`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`),
  UNIQUE KEY `codRequisito_UNIQUE` (`codRequisito`),
  UNIQUE KEY `nombreEscuela_UNIQUE` (`nombreEscuela`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `bloque` (
  `idBloque` int NOT NULL,
  `detalleBloque` varchar(25) NOT NULL,
  PRIMARY KEY (`idBloque`),
  UNIQUE KEY `idbloque_UNIQUE` (`idBloque`),
  UNIQUE KEY `detalleBloque_UNIQUE` (`detalleBloque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `planEstudios` (
  `codigoPlan` int NOT NULL,
  `nombreEscuela` varchar(50) NOT NULL,
  `fechaVigencia` datetime NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  `detalleBloque` varchar(25) NOT NULL,
  PRIMARY KEY (`codigoPlan`),
  UNIQUE KEY `codigoPlan_UNIQUE` (`codigoPlan`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`),
  UNIQUE KEY `nombreEscuela_UNIQUE` (`nombreEscuela`),
  UNIQUE KEY `detalleBloque_UNIQUE` (`detalleBloque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Llaves foraneas
ALTER TABLE usuario ADD CONSTRAINT `idRolFK` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `nombreEscuelaFK` FOREIGN KEY (`nombreEscuela`) REFERENCES `escuela` (`nombreEscuela`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `codigoEscuelaFK` FOREIGN KEY (`codigoEscuela`) REFERENCES `escuela` (`codigoEscuela`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE planEstudios ADD CONSTRAINT `nombreEscuela_FK` FOREIGN KEY (`nombreEscuela`) REFERENCES `escuela` (`nombreEscuela`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE planEstudios ADD CONSTRAINT `codigoCursoFK` FOREIGN KEY (`codigoCurso`) REFERENCES `curso` (`codigoCurso`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE planEstudios ADD CONSTRAINT `bloqueFK` FOREIGN KEY (`detalleBloque`) REFERENCES `bloque` (`detalleBloque`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- Insercion info

-- Info rol
INSERT INTO rol VALUES (1, 'admin');
INSERT INTO rol VALUES (2, 'consultor');

-- Info bloque
INSERT INTO bloque VALUES (1, 'Semestre 1');
INSERT INTO bloque VALUES (2, 'Semestre 2');
INSERT INTO bloque VALUES (3, 'Verano');

-- SELECT * FROM bloque;
-- SELECT * FROM usuario;
-- SELECT * FROM escuela;
