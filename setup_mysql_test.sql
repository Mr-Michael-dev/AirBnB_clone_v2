-- prepares a MySQL server for the Airbnb project

-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- create a new user and grant permisions
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- If hbnb_test user already exists, update the password
ALTER USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
