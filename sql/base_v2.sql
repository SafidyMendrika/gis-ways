DROP DATABASE lalana;
CREATE DATABASE lalana;
ALTER DATABASE lalana OWNER TO postgres;
\c lalana

CREATE TABLE wayType(
    idWayType SERIAL PRIMARY KEY,
    wayTypeName varchar(50) not null,
    cost double precision not null,
    duration float not null
);
--duration : h

CREATE TABLE way(
    idWay SERIAL PRIMARY KEY,
    wayName varchar(50) not null,
    width double precision not null,
    way_idWayType int REFERENCES wayType(idWayType)
);

CREATE TABLE pk(
    idPk SERIAL PRIMARY KEY,
    pk_value double precision not null,
    coordinate geography(POINT) not null,
    pk_idWay int REFERENCES way(idWay)
);

CREATE TABLE dmgWay(
    idDmgWay SERIAL PRIMARY KEY,
    idPk_start int REFERENCES pk(idPk),
    idPk_end int REFERENCES pk(idPk),
    degree int check(degree BETWEEN 0 AND 101)
);

CREATE TABLE layertype(
    idLayerType SERIAL PRIMARY KEY ,
    layerLabel varchar(50) not null
);

CREATE TABLE layer(
    idLayer SERIAL PRIMARY KEY,
    layername varchar(50) not null,
    location geography(POINT) not null,
    layer_idLayerType int REFERENCES layertype(idLayerType),
    value int default 0
);

DROP TABLE layertype cascade ;
DROP TABLE layer cascade ;
DROP TABLE dmgway cascade ;
DROP TABLE pk cascade ;
DROP TABLE way cascade ;
DROP TABLE wayType cascade ;


