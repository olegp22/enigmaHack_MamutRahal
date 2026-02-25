CREATE TABLE IF NOT EXISTS user (
id serial PRIMARY KEY,
name varchar(150),
email varchar(150) UNIQUE NOT NULL,
password text
);

CREATE TABLE IF NOT EXISTS emotion(
id serial PRIMARY KEY,
emotion VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS object(
id VARCHAR(100) PRIMARY KEY,
type text
);



CREATE TABLE IF NOT EXISTS message(
id serial PRIMARY KEY,
date timestamp,
name_from varchar(150),
email varchar(150) NOT NULL,
phone varchar(17),
object VARCHAR(100) REFERENCES object(id),
emotion int REFERENCES emotion(id),
part text
);


