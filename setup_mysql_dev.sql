-- create a new database and user
-- Grant all privileges to user only on the new database
-- Grant select privilege to user on perfomance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev_pwd@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev_pwd@localhost;
