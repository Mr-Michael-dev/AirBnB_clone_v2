-- prepares a MySQL server for the Airbnb project

-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;

-- create a new user and grant permisions
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- If hbnb_dev user already exists, update the password
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
