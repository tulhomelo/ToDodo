/* Excluir a tabela se ela existir */
DROP TABLE IF EXISTS todo;

/* Cria a tabela */
CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titulo CHAR(50) NOT NULL,
    descricao CHAR(100) NOT NULL,
    limite TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    concluido BOOLEAN NOT NULL DEFAULT false
);

/* Insere as tarefas desse próprio projeto */
INSERT INTO todo(titulo, descricao) VALUES 
('Tarefa 01 - Criar repositório', 'Como primeira tarefa vamos criar o ambiente.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 02', 'Criar ambiente virtual.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 03', 'Criar estrutura do BD.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 04', 'Subir os dockers.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 05', 'Instalar dependências do projeto.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 06', 'Configurar o Postgres.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 07', 'Configurar o Pgadmin.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 08', 'Criar as templates Jinja.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 09', 'Estruturar a UI com Bootstrap.');
INSERT INTO todo (titulo, descricao) VALUES 
('Tarefa 10', 'Finalizar o README do projeto.');
