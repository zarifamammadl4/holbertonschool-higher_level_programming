-- Create user user_0d_2 with password
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY user_0d_2_pwd;

-- Grant SELECT privilege on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

FLUSH PRIVILEGES;
