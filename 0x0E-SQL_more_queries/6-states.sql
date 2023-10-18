-- creats the databse hbtn_0d_usa and the tabl states (in the database hbtn_0d_usa) on your MySQL servr
-- creats a databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a databse
USE hbtn_0d_usa;
-- creats a tabl
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
