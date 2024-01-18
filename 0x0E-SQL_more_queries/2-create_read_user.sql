-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create or update user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%' WITH GRANT OPTION;
