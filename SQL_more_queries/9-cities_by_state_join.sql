-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name AS name FROM cities AS c JOIN states AS s ON c.state_id = s.id;