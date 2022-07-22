INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("José alencar", "Luana alencar", "99900099098", DATE '2000-01-09');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Camila Forte", "Carolina Forte Filha", "98900099098", DATE '2002-12-29');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Paulo Pedro", "Pedro Paulo", "29900099098", DATE '1999-01-18');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Carlos Tanos", "Carlos Tanos filho", "39900099098", DATE '2010-03-20');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("José alencar", "Lucas alencar", "94900099098", DATE '2012-04-03');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Paula Cabral", "Felipe Kettl", "34400099098", DATE '2000-05-05');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Mariana Dick", "Andres Farias", "11100099098", DATE '2002-05-06');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Larissa Rosa", "Luiza Rosa", "77700099098", DATE '2000-02-07');
INSERT INTO Paciente(paciente_resp, Nome, cpf, data_nascimento) VALUES ("Roberto Rozário", "Antonia Paola", "88880099098", DATE '2000-01-19');

INSERT INTO Profissional(nome, cns, cpf) VALUES ("Camila Lucas", "2000", "19922500993");
INSERT INTO Profissional(nome, cns, cpf) VALUES ("Calma Vida", "3000", "89890489844");
INSERT INTO Profissional(nome, cns, cpf) VALUES ("Matheus Beirão", "4000", "11223345689");
INSERT INTO Profissional(nome, cns, cpf) VALUES ("Larissa Gremelmaier", "5000", "00000000000");
INSERT INTO Profissional(nome, cns, cpf) VALUES ("Lucas Barzan", "6000", "89765093345");

INSERT INTO Medico (CFM, idprofissional) VALUES ("30000", 1);
INSERT INTO Medico (CFM, idprofissional) VALUES ("30001", 2);
INSERT INTO Medico (CFM, idprofissional) VALUES ("30002", 3);

INSERT INTO Dentista (CFO, idProfissional) VALUES ("20000", 4);
INSERT INTO Dentista (CFO, idProfissional) VALUES ("20001", 5);

INSERT into Especialidade(titulo) VALUES ("cirurgia geral");
INSERT into Especialidade(titulo) VALUES ("ginecologia");
INSERT into Especialidade(titulo) VALUES ("Endodontia");
INSERT into Especialidade(titulo) VALUES ("medicina geral");
INSERT into Especialidade(titulo) VALUES ("Implantodontia");

INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (1, 1);
INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (1, 4);
INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (2, 1);
INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (2, 3);
INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (3, 1);
INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (4, 2);


INSERT into Profissional_especialidade (idprofissional, idEspecialidade) VALUES (5, 4);

insert into Fabricante(nome) VALUES ("Bayer");
insert into Fabricante(nome) VALUES ("Farma farmacias");
insert into Fabricante(nome) VALUES ("ABC farma");

INSERT INTO Medicamento(nome, idfabricante) values ("Dipirona", 1);
INSERT INTO Medicamento(nome, idfabricante) values ("Paracetamol", 1);
INSERT INTO Medicamento(nome, idfabricante) values ("Antibiótico ABX", 2);
INSERT INTO Medicamento(nome, idfabricante) values ("Anti-inflamatório UUU", 3);

INSERT into Equipe(nome, ine) values ("time 1", "xxx");
INSERT into Equipe(nome, ine) values ("time 2", "yyy");

INSERT into Lotado(id_departamento, id_profissional) values(1, 1);
INSERT into Lotado(id_departamento, id_profissional) values(1, 2);
INSERT into Lotado(id_departamento, id_profissional) values(1, 4);
INSERT into Lotado(id_departamento, id_profissional) values(2, 3);
INSERT into Lotado(id_departamento, id_profissional) values(2, 5);

INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-10', 1, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-12', 2, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-13', 1, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-14', 3, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-08-10', 4, 2);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-16', 1, 2);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-17', 4, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-12', 4, 3);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-07-30', 1, 3);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-07-10', 5, 3);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-07-09', 5, 3);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-07-15', 2, 4);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-10-12', 5, 4);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-18', 6, 4);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-10-10', 7, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-11-24', 8, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-08-21', 7, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-08-20', 6, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-10-14', 6, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-10-15', 1, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-16', 2, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-11-10', 2, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-11-18', 2, 3);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-11-10', 1, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-10', 1, 5);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-12', 1, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-13', 3, 1);
INSERT into Consulta(data_hora, idpaciente, idprofissional) values (DATE '2022-09-10', 1, 3);

INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 1);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 5, 2);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 7, 3);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 6, 4);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 5);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 6);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 10);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 11);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 12);
INSERT INTO Receita(orientacoes, qtd_medicamento, idconsulta) VALUES ("Tomar durante 5 dias, 2 comprimidos por dia", 10, 7);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (1, 1);
INSERT into Receita_medicamento(id_medicamento, id_receita) values (1, 2);
INSERT into Receita_medicamento(id_medicamento, id_receita) values (1, 3);
INSERT into Receita_medicamento(id_medicamento, id_receita) values (2, 4);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (2, 5);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (3, 6);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (3, 7);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (4, 8);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (4, 9);

INSERT into Receita_medicamento(id_medicamento, id_receita) values (2, 10);

/*CONSULTAS*/
/* Essa consulta busca pela quantidade de vezes que uma especialidade médica estava presente em uma consulta. Para estar presente, considera-se que o médico atendente
possui essa especialidade como uma das suas. Note também que um médico pode ter N especialidades, por isso, esse número é maior que o número de consultas realizadas*/
SELECT Especialidade.titulo, COUNT(*) from Profissional JOIN Profissional_especialidade on Profissional.idProfissional = Profissional_especialidade.idProfissional JOIN Especialidade
on Especialidade.idEspecialidade = Profissional_especialidade.idEspecialidade JOIN Consulta on Consulta.idProfissional = Profissional.idProfissional GROUP by Especialidade.idEspecialidade
ORDER BY COUNT(*) DESC;


/*mostra o número de consultas feitas por profissionais membros de cada equipe do hospital*/
SELECT Equipe.nome, COUNT(*) FROM Equipe join Lotado on Equipe.id_departamento = Lotado.id_departamento JOIN Profissional on Profissional.idProfissional = Lotado.id_profissional JOIN
Consulta on Consulta.idProfissional = Profissional.idProfissional GROUP by Equipe.id_departamento ORDER by COUNT(*) DESC;

/* média de doses receitadas para cada medicamento*/
SELECT Medicamento.nome, AVG(Receita.qtd_medicamento) from Medicamento NATURAL JOIN Receita_medicamento NATURAL JOIN Receita GROUP by Medicamento.id_medicamento DESC;

