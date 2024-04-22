CREATE DATABASE IF NOT EXISTS userlogin;

USE userlogin;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS playercharacter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    charname VARCHAR(255) NOT NULL,
    charhealth INT NOT NULL,
    profession VARCHAR(10) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (username, password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3');

INSERT INTO playercharacter (charname, charhealth, profession, user_id) VALUES
('Prettyelf', 100, 'Thief', 1),
('Mario', 80, 'Alchemist', 2),
('Test1', 80, 'Thief', 3),
('Test2', 90, 'Warrior', 3),
('Test3', 70, 'Mage', 3);

CREATE VIEW user_characters AS
SELECT u.username, pc.charname, pc.charhealth, pc.profession
FROM users AS u
JOIN playercharacter AS pc ON u.id = pc.user_id;

SELECT * FROM user_characters;
