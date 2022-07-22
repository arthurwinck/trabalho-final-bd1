CREATE SCHEMA IF NOT EXISTS db_trabalho1;

CREATE DATABASE IF NOT EXISTS db_trabalho1;

USE db_trabalho1;


CREATE TABLE `Paciente` 
( 
 `idPaciente` INT AUTO_INCREMENT, 
 `paciente_resp` VARCHAR(50),   
 `Nome` VARCHAR(50),  
 `cpf` VARCHAR(11),  
 `data_nascimento` DATE, 
 PRIMARY KEY (`idPaciente`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Profissional`
( 
 `idProfissional` INT PRIMARY KEY AUTO_INCREMENT,  
 `nome` VARCHAR(50),  
 `cns` VARCHAR(50),  
 `cpf` VARCHAR(11)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Medico` 
( 
 `CFM` VARCHAR(50),  
 `idProfissional` INT PRIMARY KEY
)ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Dentista` 
( 
 `CFO` VARCHAR(50),  
 `idProfissional` INT PRIMARY KEY
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Equipe` 
( 
 `id_departamento` INT PRIMARY KEY AUTO_INCREMENT,  
 `nome` VARCHAR(50),  
 `ine` VARCHAR(50)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Consulta` 
( 
 `data_hora` DATE,  
 `idConsulta` INT PRIMARY KEY AUTO_INCREMENT,  
 `idPaciente` INT,  
 `idProfissional` INT  
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Receita` 
( 
 `id_receita` INT PRIMARY KEY AUTO_INCREMENT,  
 `orientacoes` VARCHAR(500),  
 `qtd_medicamento` INT,  
 `idConsulta` INT  
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Medicamento` 
( 
 `id_medicamento` INT PRIMARY KEY AUTO_INCREMENT,  
 `nome` VARCHAR(50),  
 `idFabricante` INT
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Especialidade` 
( 
 `titulo` VARCHAR(50),  
 `idEspecialidade` INT PRIMARY KEY AUTO_INCREMENT 
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Fabricante` 
( 
 `idFabricante` INT PRIMARY KEY AUTO_INCREMENT,  
 `nome` VARCHAR(50)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Lotado` 
( 
 `id_departamento` INT,  
 `id_profissional` INT,  
 `id_lotado` INT PRIMARY KEY AUTO_INCREMENT
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Receita_medicamento` 
( 
 `id_medicamento` INT,  
 `id_receita` INT,  
 `possui_id` INT PRIMARY KEY AUTO_INCREMENT
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

CREATE TABLE `Profissional_especialidade` 
( 
 `idEspecialidade` INT,  
 `idProfissional` INT,  
 `possui_id` INT PRIMARY KEY AUTO_INCREMENT  
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4; 

ALTER TABLE `Medico` ADD FOREIGN KEY(`idProfissional`) REFERENCES `Profissional` (`idProfissional`);
ALTER TABLE `Dentista` ADD FOREIGN KEY(`idProfissional`) REFERENCES `Profissional` (`idProfissional`);
ALTER TABLE `Consulta` ADD FOREIGN KEY(`idPaciente`) REFERENCES `Paciente` (`idPaciente`);
ALTER TABLE `Consulta` ADD FOREIGN KEY(`idProfissional`) REFERENCES `Profissional` (`idProfissional`);
ALTER TABLE `Receita` ADD FOREIGN KEY(`idConsulta`) REFERENCES `Consulta` (`idConsulta`);
ALTER TABLE `Medicamento` ADD FOREIGN KEY(`idFabricante`) REFERENCES `Fabricante` (`idFabricante`);
ALTER TABLE `Lotado` ADD FOREIGN KEY(`id_departamento`) REFERENCES `Equipe` (`id_departamento`);
ALTER TABLE `Lotado` ADD FOREIGN KEY(`id_profissional`) REFERENCES `Profissional` (`idProfissional`);
ALTER TABLE `Receita_medicamento` ADD FOREIGN KEY(`id_medicamento`) REFERENCES `Medicamento` (`id_medicamento`);
ALTER TABLE `Receita_medicamento` ADD FOREIGN KEY(`id_receita`) REFERENCES `Receita` (`id_receita`);
ALTER TABLE `Profissional_especialidade` ADD FOREIGN KEY(`idEspecialidade`) REFERENCES `Especialidade` (`idEspecialidade`);
ALTER TABLE `Profissional_especialidade` ADD FOREIGN KEY(`idProfissional`) REFERENCES `Profissional` (`idProfissional`);
