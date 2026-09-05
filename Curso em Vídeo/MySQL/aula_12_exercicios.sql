# Exercícios MySQL - Aula 12 
# Nome: Italo Andrade Costa
# 06/08/2026 - Versão 1.0

# Exercício 01:
select * from gafanhotos
where sexo = 'F';

# Exercício 02:
select * from gafanhotos
where nascimento between '2000-01-01' and '2015-12-31'
order by nascimento;

# Exercício 03:
select * from gafanhotos
where sexo = 'M' and profissao = 'Programador';

# Exercício 04:
select * from gafanhotos
where sexo = 'F' and nacionalidade = 'Brasil' and nome like 'J%';

# Exercício 05:
select nome, nacionalidade from gafanhotos
where sexo = 'M' and nome like '%Silva%' and nacionalidade != 'Brasil' and peso < '100';

# Exercício 06:
select max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'Brasil';

# Exercício 07:
select avg(peso) from gafanhotos;

# Exercício 08:
select min(peso) from gafanhotos
where sexo = 'F' and nacionalidade != 'Brasil' and nascimento between '1990-01-01' and '2000-12-31';

# Exercício 09:
select count(*) from gafanhotos
where sexo = 'F' and altura > '1.90';