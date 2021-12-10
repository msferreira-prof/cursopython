# cursopython
Este exercicio representa uma lista de chamadas para turmas com professores, turmas e alunos.
A pasta "docs" contem as tabelas envolvidas no aplicativo e um script MySQL para criacao do banco.
A aplicacao utiliza o SQLite. Caso queira utilizar o MySQL, realizar o ajuste da configuracao do DB no arquivo "settings.py" na pasta "ges".
Professores ao serem cadastrados, precisam de uma titularidade.
Turmas podem ser cadastradas sem professores.
Alunos podem ser cadastrados sem turma.
Caso queira carregar as tabelas com alguns registros, executar a url localhost:8000/utils/carga. Em seguida, utilizar o aplicativo como desejar.
Se quiser cadastrar mais Titularidades, fazer diretamente na tabela através da url localhost:8000/admin.
