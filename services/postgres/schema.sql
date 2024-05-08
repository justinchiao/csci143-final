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
        FOREIGN KEY (id_users) REFERENCES users(id_users)
    );
