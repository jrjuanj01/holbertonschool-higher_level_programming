-- Block
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    states_id INT NOT NULL,
    FOREIGN KEY (states_id) REFERENCES states (id),
    name VARCHAR(256) NOT NULL
);