BEGIN;
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE

);
CREATE INDEX IF NOT EXISTS idx_username ON users(username);
COMMIT;


CREATE TABLE IF NOT EXISTS passwords(
    password TEXT NOT NULL,
    association TEXT NOT NULL UNIQUE,
    user_id INTEGER,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);