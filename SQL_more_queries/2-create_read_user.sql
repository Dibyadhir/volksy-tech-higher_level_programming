-- task_2
CREATE DATABASE IF NOT EXIT 'hbtn_0d_2';
CREATE USER IF NOT EXIT 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'user_0d_2' * TO 'user_0d_2'@'localhost';
