-- Creates the database hbtn_0d_usa and the table cities with some constraints

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	states_id INT NOT NULL FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256));
