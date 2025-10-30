BEGIN;
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE

);
CREATE INDEX IF NOT EXISTS idx_username ON users(username);
COMMIT;


CREATE TABLE IF NOT EXISTS passwords(
    password TEXT NOT NULL,
    association TEXT NOT NULL,
    user_id INTEGER NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT user_association UNIQUE(user_id, association)
);
