/* criar bd ou esquema - MYSQL */
create SCHEMA lista_chamadas_v2;

/* conecto ou abro o bd ou esquema */
use lista_chamadas_v2;

/* tabelas */
/* tabela de professores */
create table if not exists lista_chamadas_v2.professores (
  matricula INT(11) not null auto_increment,
  nome VARCHAR(50) not null,
  foto VARCHAR(100) null default null,
  primary key (matricula)
) default character set = utf8;

/* tabela de turmas */
create table turmas (
  codigo CHAR(3) not null,
  serie CHAR(10) not null,
  sala INT not null,
  hora_inicial TIME not null,
  hora_final TIME not null,
  professores_matricula INT null,
  primary key (codigo),
  constraint fk_professores_matricula foreign key (professores_matricula) references professores (matricula)
) default character set = utf8;

/* tabela de alunos */
create table alunos (
  matricula INT not null auto_increment,
  nome VARCHAR(50) not null,
  turmas_codigo CHAR(3) null,
  primary key (matricula),
  constraint fk_turmas_codigo foreign key (turmas_codigo) references turmas (codigo)
) default character set = utf8;

/* criar indices para as chaves estrangeiras das tabelas */
create index fk_professores_matricula_idx on turmas (professores_matricula asc);
create index fk_turmas_codigo_idx on alunos (turmas_codigo asc);