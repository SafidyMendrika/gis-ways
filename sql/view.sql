
CREATE OR REPLACE VIEW dmg_way_detals as
    SELECT
        dw.id as id_dmgway,
        dw.dest_degree as dest_degree,
        way.width as way_width,
        way.name as way_name,
        dw.idpk_start
    FROM dmgway
        as dw
    JOIN  way
        ON dw.idWay = way.id
    JOIN (select pk.pk_value as pk_value ,pk.latitude as )
        ON pk.id = dw.idPK_START
    JOIN pk
        ON pk.id = dw.idPK_END

--dmgway join pk
CREATE OR REPLACE VIEW dmg_way_detals as
    SELECT
        dw.idDmgWay as idDmgWay,
        dw.degree as degree,
        pk_start.idPk as pk_start_id,
        pk_end.idPk as pk_end_id,
        pk_start.coordinate as pk_start_coord,
        pk_end.coordinate as pk_end_coord,
        pk_start.pk_value as pk_start_value,
        pk_end.pk_value as pk_end_value,
        pk_start.pk_idWay as idway ,
        st_astext(pk_start.coordinate) as pkp_start_point,
        st_astext(pk_end.coordinate) as pkp_end_point
        FROM dmgway as dw
        JOIN pk as pk_start
            ON pk_start.idPk = dw.idPk_start
        JOIN pk as pk_end
            ON pk_end.idPk = dw.idPk_end;

--layer detals
CREATE OR REPLACE VIEW layer_detals AS
    SELECT
        *,
        st_astext(location) as text_location
    FROM
        layer
    JOIN
        layertype
    ON
        layer.layer_idLayerType = layertype.idLayerType;

--way detals
CREATE OR REPLACE VIEW way_detals AS
    SELECT
        *
    FROM
        way
    JOIN
        waytype
    ON
        way.way_idWayType = waytype.idwayType;


--pk_betweens_detals
--SELECT
  --  *
    --FROM pk
    --where
    --pk_value BETWEEN
      --  (SELECT pk_value from pk where idpk = id1)
        --    and
        --(SELECT pk_value from pk where idpk = id2)