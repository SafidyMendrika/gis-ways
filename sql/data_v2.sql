
--way type
INSERT INTO wayType VALUES(default,'goudron',6000,1);
INSERT INTO wayType VALUES(default,'gravier',55000,14);
INSERT INTO wayType VALUES(default,'pavee',4570,1);
INSERT INTO wayType VALUES(default,'tany',25000,3);

--way
INSERT INTO way VALUES(default,'RN2',5,1);
INSERT INTO way VALUES(default,'RN7',7,1);
INSERT INTO way VALUES(default,'RN44',5,4);
INSERT INTO way VALUES(default,'RN5',5,1);
----



--pk
INSERT INTO pk VALUES (default,0,'POINT(-18.903647 47.521854)',1);
INSERT INTO pk VALUES (default,0.2,'POINT(-18.903230 47.522373)',1);
INSERT INTO pk VALUES (default,0.3,'POINT(-18.903192 47.522619)',1);
INSERT INTO pk VALUES (default,0.5,'POINT(-18.902726 47.522972)',1);
INSERT INTO pk VALUES (default,0.8,'POINT(-18.902552 47.523381)',1);
INSERT INTO pk VALUES (default,0.8,'POINT(-18.902165 47.523692)',1);
INSERT INTO pk VALUES (default,1.4,'POINT(-18.901538 47.525095)',1);
INSERT INTO pk VALUES (default,1.6,'POINT(-18.901712 47.526868)',1);
INSERT INTO pk VALUES (default,1.9,'POINT(-18.901910 47.528792)',1);
INSERT INTO pk VALUES (default,2,'POINT(-18.901722 47.529458)',1);
INSERT INTO pk VALUES (default,2.1,'POINT(-18.9015 47.5297)',1);
INSERT INTO pk VALUES (default,2.5,'POINT(-18.898947 47.529969)',1);
INSERT INTO pk VALUES (default,2.7,'POINT(-18.898429 47.531085)',1);
INSERT INTO pk VALUES (default,3.1,'POINT(-18.900195 47.534389)',1);
INSERT INTO pk VALUES (default,3.2,'POINT(-18.901017 47.534968)',1);
INSERT INTO pk VALUES (default,3.3,'POINT(-18.901667 47.535140)',1);
INSERT INTO pk VALUES (default,3.5,'POINT(-18.901606 47.537661)',1);
INSERT INTO pk VALUES (default,3.7,'POINT(-18.901545 47.540633)',1);
INSERT INTO pk VALUES (default,3.8,'POINT(-18.901352 47.541481)',1);
INSERT INTO pk VALUES (default,3.8,'POINT(-18.9017 47.5427)',1);
INSERT INTO pk VALUES (default,0.1,'POINT(-18.9040 47.5216)',2);
INSERT INTO pk VALUES (default,0.5,'POINT(-18.907440 47.524775)',2);
INSERT INTO pk VALUES (default,0.6,'POINT(-18.908023 47.525475)',2);
INSERT INTO pk VALUES (default,1.4,'POINT(-18.910063 47.527374)',2);
INSERT INTO pk VALUES (default,1.5,'POINT(-18.910439 47.527567)',2);
INSERT INTO pk VALUES (default,1.7,'POINT(-18.912205 47.526076)',2);
INSERT INTO pk VALUES (default,2,'POINT(-18.914245 47.524348)',2);
INSERT INTO pk VALUES (default,2.01,'POINT(-18.914621 47.524080)',2);
INSERT INTO pk VALUES (default,2.2,'POINT(-18.917117 47.524016)',2);
INSERT INTO pk VALUES (default,2.3,'POINT(-18.917594 47.523855)',2);
INSERT INTO pk VALUES (default,2.4,'POINT(-18.9181 47.5218)',2);
INSERT INTO pk VALUES (default,2.45,'POINT(-18.9187 47.5217)',2);
INSERT INTO pk VALUES (default,2.6,'POINT(-18.918942 47.521869)',2);
INSERT INTO pk VALUES (default,3.3,'POINT(-18.919630 47.521681)',2);
INSERT INTO pk VALUES (default,3.6,'POINT(-18.920965 47.521493)',2);
INSERT INTO pk VALUES (default,3.9,'POINT(-18.922072 47.520819)',2);
INSERT INTO pk VALUES (default,4.1,'POINT(-18.923421 47.520669)',2);
INSERT INTO pk VALUES (default,4.4,'POINT(-18.926162 47.519645)',2);
INSERT INTO pk VALUES (default,4.4,'POINT(-18.927617 47.519419)',2);
INSERT INTO pk VALUES (default,300,'POINT(-18.147246 49.389650)',4);
INSERT INTO pk VALUES (default,300.3,'POINT(-18.1410 49.3949)',4); --start
INSERT INTO pk VALUES (default,300.5,'POINT(-18.1434 49.3928)',4); --end
INSERT INTO pk VALUES (default,301,'POINT(-18.137295 49.397847)',4);
INSERT INTO pk VALUES (default,301.5,'POINT(-18.133624 49.399392)',4);
INSERT INTO pk VALUES (default,302,'POINT(-18.128743 49.400165)',4);
INSERT INTO pk VALUES (default,302.5,'POINT(-18.122071 49.399264)',4); --start
INSERT INTO pk VALUES (default,302.8,'POINT(-18.120686 49.398983)',4); --end
INSERT INTO pk VALUES (default,304,'POINT(-18.089796 49.393409)',4);
INSERT INTO pk VALUES (default,304.1,'POINT(-18.088225 49.392980)',4); --start
INSERT INTO pk VALUES (default,304.2,'POINT(-18.087573 49.392658)',4); --end
INSERT INTO pk VALUES (default,304.5,'POINT(-18.087573 49.392658)',4);


----
--layertype
INSERT INTO layertype VALUES (default,'Hospital');
INSERT INTO layertype VALUES (default,'School');
INSERT INTO layertype VALUES (default,'Restaurant');
INSERT INTO layertype VALUES (default,'Village');
INSERT INTO layertype VALUES (default,'Hotel');
----

Latitude:
Longitude:

--layer
INSERT INTO layer VALUES (default,'HJRA','POINT(-18.919850 47.519889)',1);
INSERT INTO layer VALUES (default,'Gastro Pizza','POINT(-18.909674 47.527153)',3);
INSERT INTO layer VALUES (default,'Hotel Tana Plaza','POINT(-18.904023 47.521490)',3);
INSERT INTO layer VALUES (default,'Hopital des enfants','POINT(-18.9065 47.5234)',1);
INSERT INTO layer VALUES (default,'Pharmacie de l ocean indien','POINT(-18.9052 47.5223)',1);
INSERT INTO layer VALUES (default,'Extra Pizza','POINT(-18.9076 47.5247)',3);
INSERT INTO layer VALUES (default,'Analakely','POINT(-18.906096 47.524325)',4,1200);
INSERT INTO layer VALUES (default,'Mahamasina','POINT(-18.918734 47.525065)',4,700);
INSERT INTO layer VALUES (default,'College Rasalama','POINT(-18.902055 47.533135)',2);
INSERT INTO layer VALUES (default,'Saint Michel Amparibe','POINT(-18.914436 47.526008)',2);
INSERT INTO layer VALUES (default,'Le Louvre','POINT(-18.910056 47.525257)',5);
INSERT INTO layer VALUES (default,'Tripolitsa','POINT(-18.907646 47.525210)',5);
INSERT INTO layer VALUES (default,'Behoririka','POINT(-18.902495 47.524288)',4,1500);
INSERT INTO layer VALUES (default,'Hopital Befelatanana','POINT(-18.9212 47.5230)',1);
INSERT INTO layer VALUES (default,'Toamasina','POINT(-18.142172 49.395385)',4,10000);
INSERT INTO layer VALUES (default,'EP Lovasoa','POINT(-18.140156 49.397235)',2);
INSERT INTO layer VALUES (default,'Cite Haras','POINT(-18.137324 49.395273)',4,500);
INSERT INTO layer VALUES (default,'Chez Diata','POINT(-18.131494 49.400543)',3);
----

--dmgways
INSERT INTO dmgway VALUES (default,2,3,50);
INSERT INTO dmgway VALUES (default,4,5,45);
INSERT INTO dmgway VALUES (default,7,8,30);
INSERT INTO dmgway VALUES (default,9,10,80);
INSERT INTO dmgway VALUES (default,21,22,40);
INSERT INTO dmgway VALUES (default,25,26,40);
INSERT INTO dmgway VALUES (default,28,29,25);
INSERT INTO dmgway VALUES (default,41,42,30);
INSERT INTO dmgway VALUES (default,46,47,62);
INSERT INTO dmgway VALUES (default,49,50,79);
----


-- DONNÉES

INSERT INTO way VALUES(default,'RN2',7,1);
INSERT INTO way VALUES(default,'RN7',7,1);

INSERT INTO pk VALUES (default,1,'point(-18.8768764 48.0467218)',1);--deb1
INSERT INTO pk VALUES (default,2,'point(-18.8725314 48.0519575)',1);--fin1

INSERT INTO pk VALUES (default,3,'point(-18.8873931 47.9894283)',1);--deb2
INSERT INTO pk VALUES (default,4,'point(-18.8915144 47.9991486)',1);--fin2

INSERT INTO pk VALUES (default,5,'point(-18.9085121 48.1629958)',1);--deb3
INSERT INTO pk VALUES (default,6,'point(-18.9155357 48.1721582)',1);--fin3


INSERT INTO pk VALUES (default,1,'point(-19.7917772 47.0975661)',2);--deb4
INSERT INTO pk VALUES (default,2,'point(-19.7959843 47.0953075)',2);--fin4

INSERT INTO pk VALUES (default,3,'point(-20.0669718 47.0587143)',2);--deb5
INSERT INTO pk VALUES (default,4,'point(-20.0775529 47.0626196)',2);--fin5

INSERT INTO pk VALUES (default,5,'point(-19.9137168 47.0450248)',2);--deb6
INSERT INTO pk VALUES (default,6,'point(-19.9268152 47.045116)',2);--fin6

INSERT INTO dmgway VALUES (default,1,2,50);
INSERT INTO dmgway VALUES (default,3,4,50);
INSERT INTO dmgway VALUES (default,5,6,50);
INSERT INTO dmgway VALUES (default,7,8,50);
INSERT INTO dmgway VALUES (default,9,10,50);
INSERT INTO dmgway VALUES (default,11,12,50);


INSERT INTO layer VALUES (default,'SEKOLY 1','point(-18.8921933 47.9995262)',2);
INSERT INTO layer VALUES (default,'SEKOLY 2','point(-18.8878385 47.989484)',2);
INSERT INTO layer VALUES (default,'SEKOLY 3','point(-18.9107643 48.1631291)',2);
INSERT INTO layer VALUES (default,'SEKOLY 4','point(-19.9156356 47.0606723)',2);
INSERT INTO layer VALUES (default,'SEKOLY 5','point(-19.9255611 47.0605435)',2);
INSERT INTO layer VALUES (default,'SEKOLY 6','point(-20.0647593 47.0789636)',2);
INSERT INTO layer VALUES (default,'SEKOLY 7','point(-20.0755622 47.081796)',2);
INSERT INTO layer VALUES (default,'SEKOLY 8','point(-19.7966552 47.0966332)',2);
INSERT INTO layer VALUES (default,'SEKOLY 9','point(-19.7966148 47.1104734)',2);





    (default, 1, 'point(-18.8921933 47.9995262)', default, 'SEKOLY 1'),
    (default, 1, 'point(-18.8878385 47.989484)', default, 'SEKOLY 2'),
    (default, 1, 'point(-18.9107643 48.1631291)', default, 'SEKOLY 3'),
    (default, 1, 'point(-19.9156356 47.0606723)', default, 'SEKOLY 4'),
    (default, 1, 'point(-19.9255611 47.0605435)', default, 'SEKOLY 5'),
    (default, 1, 'point(-20.0647593 47.0789636)', default, 'SEKOLY 6'),
    (default, 1, 'point(-20.0755622 47.081796)', default, 'SEKOLY 7'),
    (default, 1, 'point(-19.7966552 47.0966332)', default, 'SEKOLY 8'),
    (default, 1, 'point(-19.7966148 47.1104734)', default, 'SEKOLY 9')