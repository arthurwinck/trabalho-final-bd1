# trabalho-final-bd1
Trabalho Final da Discplina de Banco de Dados

Instalar dependências:

```pip install mysql.connector```

Para rodar a base de dados, é necessário ter o Docker e o Docker compose instalados, com eles, basta rodar, no terminal:

```docker-compose up```

Em caso de erro, tente rodar como root, nesse caso, através de

```sudo docker-compose up```

Antes de rodar os scripts presentes nesse trabalho, é preciso aguardar subir o container contendo a base de dados, ou seja, até que a linha abaixo apareça no terminal:

``` [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.27'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL. ```
