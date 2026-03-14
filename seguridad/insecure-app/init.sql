CREATE DATABASE vulnerabledb;
USE vulnerabledb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

INSERT INTO users (username, password) VALUES
('admin', 'admin123'),
('user1', 'password1');