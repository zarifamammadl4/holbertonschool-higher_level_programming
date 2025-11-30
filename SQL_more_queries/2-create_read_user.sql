-- Create database (no fail)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user (fallback for older MySQL/MariaDB)
CREATE USER user_0d_2@localhost IDENTIFIED BY user_0d_2_pwd;

-- Give SELECT permission
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

FLUSH PRIVILEGES;
