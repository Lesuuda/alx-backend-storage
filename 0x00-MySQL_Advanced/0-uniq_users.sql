-- creates table users with some attributes
-- and inserts some data into it
CREATE TABLE IF NOT EXISTS users (
    id  INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
