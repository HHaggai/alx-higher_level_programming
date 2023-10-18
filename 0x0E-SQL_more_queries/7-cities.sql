-- creats the databse hbtn_0d_usa and the tabl cities (in the database hbtn_0d_usa) on your MySQL servr
-- creates a databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a databse
USE hbtn_0d_usa;
-- creats a tabl
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
