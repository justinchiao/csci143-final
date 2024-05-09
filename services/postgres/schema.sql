SET max_parallel_maintenance_workers TO 80;
SET maintenance_work_mem TO '16 GB';

CREATE TABLE users (
        id_users BIGINT PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    );

CREATE TABLE user_urls (
        id_users BIGINT PRIMARY KEY,
        url TEXT UNIQUE,
        FOREIGN KEY (id_users) REFERENCES users(id_users)
    );

CREATE TABLE chirps (
        id_chirps BIGINT PRIMARY KEY,
        id_users BIGINT,
        created_at TIMESTAMP,
        text TEXT,
        a tsvector,
        FOREIGN KEY (id_users) REFERENCES users(id_users)
    );

CREATE EXTENSION IF NOT EXISTS RUM;

CREATE TRIGGER tsvectorupdate
BEFORE UPDATE OR INSERT ON chirps
FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger('a', 'pg_catalog.english', 'text');

/*
ALTER TABLE users SET (parallel_workers = 80);
ALTER TABLE user_urls SET (parallel_workers = 80);
ALTER TABLE chirps (parallel_workers = 80);
CREATE INDEX credentials1 ON users(username text_pattern_ops);
CREATE INDEX credentials2 ON users(password text_pattern_ops);
CREATE INDEX username ON users(id_users, username text_pattern_ops);
CREATE INDEX chirp_time ON chirps(created_at);
CREATE INDEX chirp_text ON chirps USING rum(a rum_tsvector_ops);*/
