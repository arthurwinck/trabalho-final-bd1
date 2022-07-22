CREATE TABLE Paciente 
( 
 paciente_resp VARCHAR(50),  
 id_paciente INT PRIMARY KEY AUTO_INCREMENT,  
 Nome VARCHAR(50),  
 cpf VARCHAR(11),  
 data_nascimento DATE,  
); 

CREATE TABLE Profissional 
( 
 id_profissional INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(50),  
 cns VARCHAR(50),  
 cpf VARCHAR(11),  
); 

CREATE TABLE Médico 
( 
 CFM VARCHAR(50),  
 idProfissional INT PRIMARY KEY,  
); 

CREATE TABLE Dentista 
( 
 CFO VARCHAR(50),  
 idProfissional INT PRIMARY KEY,  
); 

CREATE TABLE Equipe 
( 
 id_departamento INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(50),  
 ine VARCHAR(50),  
); 

CREATE TABLE Consulta 
( 
 data_hora DATE,  
 id_consulta INT PRIMARY KEY AUTO_INCREMENT,  
 idPaciente INT,  
 idProfissional INT,  
); 

CREATE TABLE Receita 
( 
 id_receita INT PRIMARY KEY AUTO_INCREMENT,  
 orientacoes VARCHAR(500),  
 qtd_medicamento INT,  
 idConsulta INT,  
); 

CREATE TABLE Medicamento 
( 
 id_medicamento INT PRIMARY KEY,  
 nome VARCHAR(50),  
 idFabricante INT,  
); 

CREATE TABLE Especialidade 
( 
 Titulo VARCHAR(50) AUTO_INCREMENT,  
 id_especialidade INT PRIMARY KEY AUTO_INCREMENT,  
); 

CREATE TABLE Fabricante 
( 
 id_fabricante INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(50),  
); 

CREATE TABLE Lotado 
( 
 id_departamento INT,  
 id_profissional INT,  
 id_lotado INT PRIMARY KEY AUTO_INCREMENT,  
); 

CREATE TABLE Receita_medicamento 
( 
 id_medicamento INT,  
 id_receita INT PRIMARY KEY,  
 possui_id INT PRIMARY KEY AUTO_INCREMENT,  
); 

CREATE TABLE Profissional_especialidade 
( 
 idEspecialidade INT,  
 id_profissional INT,  
 possui_id INT PRIMARY KEY AUTO_INCREMENT,  
); 

ALTER TABLE Médico ADD FOREIGN KEY(idProfissional) REFERENCES Profissional (idProfissional)
ALTER TABLE Dentista ADD FOREIGN KEY(idProfissional) REFERENCES Profissional (idProfissional)
ALTER TABLE Consulta ADD FOREIGN KEY(idPaciente) REFERENCES Paciente (idPaciente)
ALTER TABLE Consulta ADD FOREIGN KEY(idProfissional) REFERENCES Profissional (idProfissional)
ALTER TABLE Receita ADD FOREIGN KEY(idConsulta) REFERENCES Consulta (idConsulta)
ALTER TABLE Medicamento ADD FOREIGN KEY(idFabricante) REFERENCES Fabricante (idFabricante)
ALTER TABLE Lotado ADD FOREIGN KEY(id_departamento) REFERENCES Equipe (id_departamento)
ALTER TABLE Lotado ADD FOREIGN KEY(id_profissional) REFERENCES Profissional (id_profissional)
ALTER TABLE Receita_medicamento ADD FOREIGN KEY(id_medicamento) REFERENCES Medicamento (id_medicamento)
ALTER TABLE Receita_medicamento ADD FOREIGN KEY(id_receita) REFERENCES Receita (id_receita)
ALTER TABLE Profissional_especialidade ADD FOREIGN KEY(idEspecialidade) REFERENCES Especialidade (idEspecialidade)
ALTER TABLE Profissional_especialidade ADD FOREIGN KEY(id_profissional) REFERENCES Profissional (id_profissional)
