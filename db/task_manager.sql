-- createdb task_manager
-- psql -d task_manager -f db/task_manager.sql

DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  assignee VARCHAR(255),
  duration INT,
  completed BOOLEAN
);

INSERT INTO tasks (description, assignee, duration, completed) VALUES ('Walk Dog', 'Jack Jarvis', 60, false);
INSERT INTO tasks (description, assignee, duration, completed) VALUES ('Clean The House', 'John Johnson', 120, false);