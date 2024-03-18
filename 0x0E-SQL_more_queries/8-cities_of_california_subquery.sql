-- This script lists all the cities of carlifornia that can be found in the db
-- hbtn_0d_usa

USE `hbtn_0d_usa`;
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id;
