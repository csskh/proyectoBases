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

CREATE TABLE `planEstudios` (
  `numPlan` int NOT NULL,
  `fechaVigencia` datetime NOT NULL,
  `idCurso` int NOT NULL,
  `idEscuela` int NOT NULL,
  `emailUsuario` varchar(50) NOT NULL,
  PRIMARY KEY (`numPlan`),
  UNIQUE KEY `numPlan_UNIQUE` (`numPlan`),
  UNIQUE KEY `idCurso_UNIQUE` (`idCurso`),
  UNIQUE KEY `idEscuela_UNIQUE` (`idEscuela`),
  UNIQUE KEY `emailUsuario_UNIQUE` (`emailUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `escuela` (
  `idEscuela` int NOT NULL,
  `codigoEscuela` varchar(2) NOT NULL,
  `nombreEscuela` varchar(50) NOT NULL,
  `numPlan` int NOT NULL,
  PRIMARY KEY (`idEscuela`),
  UNIQUE KEY `idEscuela_UNIQUE` (`idEscuela`),
  UNIQUE KEY `codigoEscuela_UNIQUE` (`codigoEscuela`),
  UNIQUE KEY `nombreEscuela_UNIQUE` (`nombreEscuela`),
  UNIQUE KEY `numPlan_UNIQUE` (`numPlan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `curso` (
  `idCurso` int NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  `nombreCurso` varchar(50) NOT NULL,
  `creditos` int NOT NULL,
  `horas` int NOT NULL,
  `codigoEscuela` varchar(2) NOT NULL,
  `idRequisito` int NOT NULL,
  `idCorrequisito` int NOT NULL,
  `nombreEscuela` varchar(50) NOT NULL,
  `idBloque` int NOT NULL,
  PRIMARY KEY (`idCurso`),
  UNIQUE KEY `idCursos_UNIQUE` (`idCurso`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`),
  UNIQUE KEY `nombreCurso_UNIQUE` (`nombreCurso`),
  UNIQUE KEY `codigoEscuela_UNIQUE` (`codigoEscuela`),
  UNIQUE KEY `idRequisito_UNIQUE` (`idRequisito`),
  UNIQUE KEY `idCorrequisito_UNIQUE` (`idCorrequisito`),
  UNIQUE KEY `nombreEscuela_UNIQUE` (`nombreEscuela`),
  UNIQUE KEY `idBloque_UNIQUE` (`idBloque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `correquisito` (
  `idCorrequisito` int NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  PRIMARY KEY (`idCorrequisito`),
  UNIQUE KEY `idcorrequisito_UNIQUE` (`idCorrequisito`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `requisito` (
  `idRequisito` int NOT NULL,
  `codigoCurso` varchar(6) NOT NULL,
  PRIMARY KEY (`idRequisito`),
  UNIQUE KEY `idRequisito_UNIQUE` (`idRequisito`),
  UNIQUE KEY `codigoCurso_UNIQUE` (`codigoCurso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `bloque` (
  `idBloque` int NOT NULL,
  `bloque` varchar(25) NOT NULL,
  PRIMARY KEY (`idBloque`),
  UNIQUE KEY `idbloque_UNIQUE` (`idBloque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Llaves foraneas
ALTER TABLE usuario ADD CONSTRAINT `idRolFK` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE planEstudios ADD CONSTRAINT `emailUsuarioFK` FOREIGN KEY (`emailUsuario`) REFERENCES `usuario` (`emailUsuario`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE planEstudios ADD CONSTRAINT `idCursoFK` FOREIGN KEY (`idCurso`) REFERENCES `curso` (`idCurso`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE planEstudios ADD CONSTRAINT `idEscuelaFK` FOREIGN KEY (`idEscuela`) REFERENCES `escuela` (`idEscuela`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE escuela ADD CONSTRAINT `numPlanFK` FOREIGN KEY (`numPlan`) REFERENCES `planEstudios` (`numPlan`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `codigoEscuelaFK` FOREIGN KEY (`codigoEscuela`) REFERENCES `escuela` (`codigoEscuela`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `idRequisitoFK` FOREIGN KEY (`idRequisito`) REFERENCES `requisito` (`idRequisito`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `idCorrequisitoFK` FOREIGN KEY (`idCorrequisito`) REFERENCES `correquisito` (`idCorrequisito`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `nombreEscuelaFK` FOREIGN KEY (`nombreEscuela`) REFERENCES `escuela` (`nombreEscuela`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE curso ADD CONSTRAINT `idBloqueFK` FOREIGN KEY (`idBloque`) REFERENCES `bloque` (`idBloque`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- Insercion info

-- Info rol
INSERT INTO rol VALUES (1, 'admin');
INSERT INTO rol VALUES (2, 'consultor');
-- Info bloque
INSERT INTO bloque VALUES (1, 'Semestre 1');
INSERT INTO bloque VALUES (2, 'Semestre 2');
INSERT INTO bloque VALUES (3, 'Verano');

-- SELECT * FROM bloque;
-- SELECT * FROM rol;





