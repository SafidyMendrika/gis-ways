
-- get the layers arround a damaged way
SELECT
    *
    FROM
        layer
    WHERE
        ST_DWithin(location,'POINT(dmgX dmgY)'::geopraphy,radius)

