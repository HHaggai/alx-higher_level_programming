-- lists all the cities contained in database hbtn_0d_usa
-- lists all the rows of a particulr column in a databse
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
