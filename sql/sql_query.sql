DROP TABLE IF EXISTS todo;

CREATE TABLE todo(
id SERIAL PRIMARY KEY,
task VARCHAR(100)
);

INSERT INTO todo (task) VALUES ('Buy groceries');
INSERT INTO todo (task) VALUES ('Finish resume');
INSERT INTO todo (task) VALUES ('Learn PostgreSQL');
INSERT INTO todo (task) VALUES ('relax');
INSERT INTO todo (task) VALUES ('be happy');

select * from todo