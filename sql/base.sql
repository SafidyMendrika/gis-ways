CREATE DATABASE lalana ;

DROP TABLE IF EXISTS way cascade;
DROP TABLE IF EXISTS  dmgway cascade;
DROP TABLE IF EXISTS entity cascade;

CREATE TABLE way(
    idway SERIAL primary key ,
    width double precision not null,
    name varchar(100) not null
);
CREATE TABLE  dmgway(
    iddmgway SERIAL primary key ,
    idWay int REFERENCES way(idway),
    dest_degree int check ( dest_degree between 0 and 100),

    PK_START double precision not null,
    PK_END double precision not null,
    PK_START_Coordinate geography(POINT) not null,
    PK_END_Coordinate geography(POINT) not null
);
-- hospital
-- high human trafic
-- police station
-- school
CREATE TABLE entity(
    identity SERIAL primary key ,
    coordinate geography(POINT) not null,
    type varchar(100) not null,
    value double precision default 1
);

--NEW DATABASE

