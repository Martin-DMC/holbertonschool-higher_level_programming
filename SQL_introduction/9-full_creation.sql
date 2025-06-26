-- create a table second_table and add multiples rows
CREATE TABLE IF NOT EXISTS second_table(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256), score INT);
INSERT INTO second_table(name, score) VALUES('John', 10);
INSERT INTO second_table(name, score) VALUES('Alex', 3);
INSERT INTO second_table(name, score) VALUES('Bob', 14);
INSERT INTO second_table(name, score) VALUES('George', 8);
