-- This script creates a table with id and name fields where fields cant be null

CREATE TABLE IF NOT EXISTS force_name(id INTEGER, name VARCHAR(256) NOT NULL);
