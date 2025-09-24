DROP TABLE IF EXISTS todo;

CREATE TABLE todo(
id SERIAL PRIMARY KEY,
task VARCHAR(100),
completed BOOL DEFAULT FALSE
);

INSERT INTO todo (task) VALUES ('Buy groceries');
INSERT INTO todo (task) VALUES ('Learn PostgreSQL');
INSERT INTO todo (task) VALUES ('Read a book');
INSERT INTO todo (task) VALUES ('Exercise for 30 minutes');
INSERT INTO todo (task) VALUES ('Call Mom');
INSERT INTO todo (task) VALUES ('Clean the house');
INSERT INTO todo (task) VALUES ('Update LinkedIn profile');
INSERT INTO todo (task) VALUES ('Relax and unwind');

select * from todo