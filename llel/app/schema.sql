DROP TABLE IF EXISTS users;

    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    ext TEXT NOT NULL,
    email TEXT
    );
    