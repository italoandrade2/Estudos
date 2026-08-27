# Exercícios MySQL - Aula 13
# Nome: Italo Andrade Costa
# 06/08/2026 - Versão 1.0

# Exercício 01:
select profissao, count(*) from gafanhotos
group by profissao
order by profissao;

# Exercício 02:
select sexo, count(*) from gafanhotos
where nascimento > '2005-01-01'
group by sexo;

# Exercício 03:
select nacionalidade, count(*) from gafanhotos
where nacionalidade != 'Brasil'
group by nacionalidade having count(*) > 3;

# Exercício 04:
select altura, count(*) from gafanhotos
where peso > 100
group by altura having altura > (select avg(altura) from gafanhotos);