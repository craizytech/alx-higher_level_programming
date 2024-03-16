-- UPDATES the value of bob score
UPDATE second_table
SET (SELECT id FROM second_table WHERE name="Bob") = 10;
