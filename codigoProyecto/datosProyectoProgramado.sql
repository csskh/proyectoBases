#Proyecto 1
#Iris Bejarano
#Alejandro Guillen
#Sebastian Herrera

CREATE DATABASE datosProyectoProgramado;

USE  datosProyectoProgramado;

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

SELECT * FROM bloque;
SELECT * FROM usuario;
SELECT * FROM escuela;
select * from curso;

INSERT INTO escuela SET codigoEscuela = 'TI', nombreEscuela = 'ATI';
INSERT INTO escuela SET codigoEscuela = 'MA', nombreEscuela = 'Escuela de Matematicas';
INSERT INTO escuela SET codigoEscuela = 'CI', nombreEscuela = 'Escuela de Ciencias del Lenguajes';
INSERT INTO escuela SET codigoEscuela = 'CS', nombreEscuela = 'Escuela de Ciencias Sociales';


insert into curso set nombreEscuela='Escuela de Matematicas' ,nombreCurso= 'Matematica General',codigoEscuela= 'MA', codigoCurso='MA0101', creditos='2' , horas='5' ;
insert into curso set nombreEscuela='Escuela de Ciencias del Lenguaje' ,nombreCurso='Comunicacion Escrita' ,codigoEscuela='CI' , codigoCurso='CI1107' , creditos='1' , horas='3' ;
insert into curso set nombreEscuela='Escuela de Matematicas' ,nombreCurso= 'Matematica Discreta',codigoEscuela= 'MA', codigoCurso='MA1403', creditos='4' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Infromacion Contable',codigoEscuela= 'TI', codigoCurso='TI1102', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Modelos Organizacionales y Gestion de TI',codigoEscuela= 'TI', codigoCurso='TI1103', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Introduccion a la Programacion',codigoEscuela= 'TI', codigoCurso='TI1400', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Taller de Programacion',codigoEscuela= 'TI', codigoCurso='TI1401', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='Escuela de Ciencias del Lenguaje' ,nombreCurso= 'Comunicacion Oral',codigoEscuela= 'CI', codigoCurso='CI1107', creditos='1' , horas='3' ;
insert into curso set nombreEscuela='Escuela de Matematicas' ,nombreCurso= 'Calculo Diferencial e Integral',codigoEscuela= 'MA', codigoCurso='MA1102', creditos='4' , horas='5' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Comportamiento Organizacional y Talento Humano',codigoEscuela= 'TI', codigoCurso='TI1201', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Algoritmos y Estructuras de Datos',codigoEscuela= 'TI', codigoCurso='TI2402', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Organizacion y Arquitectura de Computadoras',codigoEscuela= 'TI', codigoCurso='TI2404', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Ingenieroa de Requirimientos',codigoEscuela= 'TI', codigoCurso='TI4500', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='Escuela de Ciencias del Lenguaje' ,nombreCurso= 'Ingles',codigoEscuela= 'CI', codigoCurso='CI3400', creditos='2' , horas='3' ;
insert into curso set nombreEscuela='Escuela de Matematicas' ,nombreCurso= 'Calculo y Algebra Lineal',codigoEscuela= 'MA', codigoCurso='MA1103', creditos='4' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Adminstracion de Proyectos I',codigoEscuela= 'TI', codigoCurso='TI2800', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Costos en Ambientes Infromaticos',codigoEscuela= 'TI', codigoCurso='TI3103', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Bases de Datos',codigoEscuela= 'TI', codigoCurso='TI3600', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Economia',codigoEscuela= 'TI', codigoCurso='TI4200', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='Escuela de Ciencias del Lenguaje' ,nombreCurso= 'Ingles II (ATI)',codigoEscuela= 'CI', codigoCurso='CI3400', creditos='2' , horas='6' ;
insert into curso set nombreEscuela='Escuela de Matematicas' ,nombreCurso= 'Probabilidades',codigoEscuela= 'MA', codigoCurso='MA2404', creditos='4' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Programacion Orientada a Objetos',codigoEscuela= 'TI', codigoCurso='TI2201', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Administracion de Proyectos II',codigoEscuela= 'TI', codigoCurso='TI3801', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Planificacion y Presupuesto',codigoEscuela= 'TI', codigoCurso='TI4101', creditos='2' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Bases de Datos Avanzados',codigoEscuela= 'TI', codigoCurso='TI3600', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='Escuela de Ciencias Sociales' ,nombreCurso= 'Seminario de Etica para la Ingenieria',codigoEscuela= 'CS', codigoCurso='CS3404', creditos='2' , horas='5' ;
insert into curso set nombreEscuela='Escuela de Matematicas' ,nombreCurso= 'Estadistica',codigoEscuela= 'MA', codigoCurso='MA3405', creditos='4' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Mercadeo en la Era Digital',codigoEscuela= 'TI', codigoCurso='TI3500', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Fundamentos de Sistemas Operativos',codigoEscuela= 'TI', codigoCurso='TI3501', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Gestion y Toma de Decisiones Financieras',codigoEscuela= 'TI', codigoCurso='TI5100', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Diseno de Software',codigoEscuela= 'TI', codigoCurso='TI5501', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='Escuela de Ciencias Sociales' ,nombreCurso= 'Derecho Laboral',codigoEscuela= 'CS', codigoCurso='CS2304', creditos='2' , horas='3' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Modelo de Toma de Decisiones',codigoEscuela= 'TI', codigoCurso='TI3601', creditos='2' , horas='6' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Produccion Logistica y Calidad',codigoEscuela= 'TI', codigoCurso='TI3602', creditos='2' , horas='6' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Calidad en Sistemas de Informacion',codigoEscuela= 'TI', codigoCurso='TI3603', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Fundamentos de Redes',codigoEscuela= 'TI', codigoCurso='TI3604', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Inteligencia de Negocios',codigoEscuela= 'TI', codigoCurso='TI6900', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Computacion y Sociedad',codigoEscuela= 'TI', codigoCurso='TI9003', creditos='2' , horas='4' ;

insert into curso set nombreEscuela='Escuela de Ciencias Sociales' ,nombreCurso= 'Derecho Informatico y Mercantil',codigoEscuela= 'CS', codigoCurso='CS3405', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Seguridad Sistemas de Informacion',codigoEscuela= 'TI', codigoCurso='TI4701', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Arquitectura de Aplicaciones',codigoEscuela= 'TI', codigoCurso='TI7503', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Negocios Electronicos',codigoEscuela= 'TI', codigoCurso='TI7901', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Formulacion y Evaluacion de Proyectos de TI',codigoEscuela= 'TI', codigoCurso='TI8109', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Adquisicion de TI',codigoEscuela= 'TI', codigoCurso='TI8902', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Administracion de Procesos de Negocios',codigoEscuela= 'TI', codigoCurso='TI8904', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Administracion de Servicios de TI ',codigoEscuela= 'TI', codigoCurso='TI8905', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Auditoria de TI',codigoEscuela= 'TI', codigoCurso='TI9805', creditos='3' , horas='4' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Sistemas de Informacion Empresarial',codigoEscuela= 'TI', codigoCurso='TI9905', creditos='3' , horas='4' ;

insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Espiritu Emprendedor y Creacion de Empresas',codigoEscuela= 'TI', codigoCurso='TI5901', creditos='3' , horas='13' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Analitica Empresarial',codigoEscuela= 'TI', codigoCurso='TI5902', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Planificacion Estrategica de TI',codigoEscuela= 'TI', codigoCurso='TI5903', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Investigacion en Sistemas de Informacion',codigoEscuela= 'TI', codigoCurso='TI5904', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Fundamentos de Arquitectura Empresarial',codigoEscuela= 'TI', codigoCurso='TI5905', creditos='3' , horas='9' ;
insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Administracion de Servicios de TI II',codigoEscuela= 'TI', codigoCurso='TI9004', creditos='3' , horas='9' ;

insert into curso set nombreEscuela='ATI' ,nombreCurso= 'Trabajo Final de Graduación',codigoEscuela= 'TI', codigoCurso='TI9000', creditos='10' , horas='0' ;

