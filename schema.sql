CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    visible BOOLEAN,
    category_id INTEGER REFERENCES categories,
    user_id INTEGER REFERENCES users
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name TEXT,
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    message_id INTEGER REFERENCES messages
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    liker_id INTEGER REFERENCES users,
    message_id INTEGER REFERENCES messages
);