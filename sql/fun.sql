-- function who return all layers arount one pk
CREATE FUNCTION layerNear(var_idPk int,radius double precision)
RETURNS
    table(
        id int,
        layername varchar(50),
        location geography(POINT),
        value int ,
        idLayerType int,
        layerTypeLabel varchar(50)
        )
LANGUAGE plpgsql
AS $$
DECLARE
    kilPoint geography(POINT) ;

    layerRecord record;
BEGIN
    kilPoint := (SELECT coordinate FROM pk WHERE idPk = var_idPk);
    for layerRecord in (SELECT
            *
        FROM
            layer_detals ld
        WHERE ST_DWithin(ld.location,kilPoint,radius)
        )
        loop
            id := layerRecord.idlayer;
            layername := layerRecord.layername;
            location := layerRecord.location;
            value := layerRecord.value;
            idLayerType := layerRecord.layer_idlayertype;
            layerTypeLabel := layerRecord.layerlabel;
            return  next;

        end loop;
END;
$$;
--
-- function who return al layer in a Way
CREATE FUNCTION layerIn(var_idWay int,radius double precision)
RETURNS
    table(
        id int,
        layername varchar(50),
        location geography(POINT),
        value int ,
        idLayerType int,
        layerTypeLabel varchar(50)
        )
LANGUAGE plpgsql
AS $$
DECLARE
    pks record;
    layers record;
BEGIN
    for pks in (SELECT
            *
        FROM
            pk
        WHERE pk.pk_idWay = var_idWay
        )
        loop
            for layers in (select * from layerNear(pks.idpk,radius))
                loop
                    id := layers.id;
                    layername := layers.layername;
                    location := layers.location;
                    value := layers.value;
                    idLayerType := layers.idlayertype;
                    layerTypeLabel := layers.layerTypeLabel;
                    return  next;
            end loop;
        end loop;
END;
$$;
--
--layer distinct in
CREATE FUNCTION layerDistinctIn(var_idWay int,radius double precision)
RETURNS
    table(
        id int,
        layername varchar(50),
        location geography(POINT),
        value int ,
        idLayerType int,
        layerTypeLabel varchar(50)
        )
LANGUAGE plpgsql
AS $$
DECLARE
    pks record;
    layers record;
BEGIN
    for layers in (SELECT
        li.id,li.layername,li.location,li.value,li.idLayerType,li.layerTypeLabel
        FROM
            layerin(var_idWay,radius) as li
        GROUP BY li.id,li.layername,li.location,li.value,li.idLayerType,li.layerTypeLabel)
        loop
                id := layers.id;
                layername := layers.layername;
                location := layers.location;
                value := layers.value;
                idLayerType := layers.idlayertype;
                layerTypeLabel := layers.layerTypeLabel;
                return  next;
        end loop;
END;
$$;
--
--
CREATE FUNCTION wayWithLayerCount(idLayerT int,radius double precision)
RETURNS
    table(
        idway int,
        value int
        )
LANGUAGE plpgsql
AS $$
DECLARE
    ways record;
    layers record;
BEGIN

    for ways in (SELECT * FROM way)
        loop
            idway := ways.idway;
            value := 0;
            if idLayerT = 4 then
                for layers in (SELECT coalesce(sum(li.value),0) as nb from layerDistinctIn(ways.idway,radius) as li where li.idlayertype = idLayerT )
                loop
                    value := layers.nb;
                end loop;
            else
                for layers in (select count(DISTINCT(l.id)) as nb FROM layerIn(ways.idWay,radius) as l where l.idLayerType = idLayerT)
                    loop
                        value := layers.nb;
                    end loop;
            end if;
            return next;
        end loop;
END;
$$;
----

