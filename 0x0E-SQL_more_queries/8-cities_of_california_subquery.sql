-- lists all cities of California that can be found in databse hbtn_0d_usa
-- lists all the rows of a column in a databs
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
