USE EquipmentProject;

DROP TABLE IF EXISTS Brand;

CREATE TABLE Brand (
	BrandID INT PRIMARY KEY,
	BrandName VARCHAR(30) NOT NULL
);

INSERT INTO Brand (BrandID, BrandName)
VALUES (1,'Schutt'), (2,'Riddell'),(3,'VICIS');

SELECT * FROM Brand;

DROP TABLE IF EXISTS Styles;

CREATE TABLE Styles(
	StylesID INT PRIMARY KEY,
	StyleName VARCHAR(30) NOT NULL,
	BrandID INT,
	FOREIGN KEY (BrandID) REFERENCES Brand(BrandID)
);

INSERT INTO Styles (StylesID, StyleName, BrandID)
VALUES (1, 'F7UR1', 1), (2, 'F7UR2', 1), (3, 'F7UR1 2.0', 1),
(4, 'F7 2.0', 1), (5, 'F7 VTD ll', 1), (6, 'AIR XP Pro Q11 LTD', 1),
(7, 'Axiom', 2), (8, 'Speedflex', 2),(9, 'Speedflex P-Fit', 2),(10, 'Speedflex Diamond', 2),
(11, 'Speedflex Diamond P-Fit', 2),(12, 'Speedflex True', 2),(13, 'Zero2 matrix QB', 3),(14, 'Zero2-R', 3)
;


DROP TABLE IF EXISTS Facemask;

CREATE TABLE Facemask (
	FacemaskID INT PRIMARY KEY,
	FacemaskName VARCHAR(30) NOT NULL,
	BrandID INT,
	FOREIGN KEY (BrandID) REFERENCES Brand(BrandID)
);

INSERT INTO Facemask (FacemaskID, FacemaskName, BrandID)
VALUES (1, 'TROPO-SW', 1), (2, 'TROPO', 1),(3, 'TROPO-DW', 1),(4, 'TEGOP', 1),(5, 'TEGOPll', 1),(6, 'TEGOPll-DW', 1),
(7, 'TRJOP-DW ', 1),(8, 'TRJOP-DW UB', 1),(9, 'TRKOP', 1),(10, 'SF-3BD RR', 1),
(11, 'Axiom 2B- SW-TI', 2), (12, 'Axiom 2BC-TI', 2), (13, 'SF-2BD', 2), (14, 'SF-2BD-SW', 2), (15, 'SF-2BDC', 2), (16, 'SF-2BDC-HD', 2), 
(17, 'SF-2EG-SW', 2), (18, 'SF-2EG-SW-HD', 2),(19, 'SF-2EG-ll', 2), (20, 'SF-2EG-ll-HD', 2), (21, 'SF-3BD', 2), 
(22, 'SF-Kicker', 2), (23, 'CU-SF-2B-SW', 2), (24, 'CU-SF-2B-PW', 2),
(25, 'Z02-SO-212E', 3), (26, 'Z02-SO-212', 3), (27, 'Z02-SO-223E', 3), (28, 'Z02-SO-223', 3), 
(29, 'Z02-SC-223E', 3), (30, 'Z02-SC-223', 3), (31, 'Z02-SK-212', 3), (32, 'Z02-SO-213E', 3), (33, 'Z02-SO-215T', 3)
;

DROP TABLE IF EXISTS Size;

CREATE TABLE Size(
	SizeID INT PRIMARY KEY,
	Size VARCHAR(30) NOT NULL,
);

SELECT * FROM Size;


INSERT INTO Size (SizeID, Size)
VALUES (1,'M'), (2,'L'), (3,'L+'), (4,'XL'), (5,'Custom'),
(6, 'Standard'), (7,'Trench');

DROP TABLE IF EXISTS BrandSize;

CREATE TABLE BrandSize(
	SizeID INT ,
	BrandID INT,
	FOREIGN KEY (SizeID) REFERENCES Size(SizeID),
	FOREIGN KEY (BrandID) REFERENCES Brand(BrandID)
);

INSERT INTO BrandSize (SizeID, BrandID)
VALUES (1,1), (2,1), (3,1), (4,1), (5,1), (5,2), (1,2), (2,2), (4,2),
(6,3), (7,3);

SELECT * FROM BrandSize;

SELECT Brand.BrandName, Size.Size
FROM BrandSize
INNER JOIN Size ON Size.SizeID = BrandSize.SizeID
INNER JOIN Brand ON Brand.BrandID = BrandSize.BrandID;


DROP TABLE IF EXISTS JawPadMaterial;

CREATE TABLE JawPadMaterial (
	MaterialID INT PRIMARY KEY,
	MaterialName VARCHAR(30)
);

INSERT INTO JawPadMaterial (MaterialID, MaterialName)
VALUES (1, '2.0'), (2, 'Leather'), 
(3, 'SF'), (4, '');

SELECT * FROM JawPadMaterial;


DROP TABLE IF EXISTS BrandMaterial;

CREATE TABLE BrandMaterial (
	MaterialID INT,
	BrandID INT,
	FOREIGN KEY (BrandID) REFERENCES Brand(BrandID),
	FOREIGN KEY (MaterialID) REFERENCES JawPadMaterial(MaterialID)
);

INSERT INTO BrandMaterial (MaterialID, BrandID)
VALUES (1,1), (2,1), (1,2), (3,2), (4,3);

SELECT Brand.BrandName, JawPadMaterial.MaterialName
FROM BrandMaterial
INNER JOIN Brand ON Brand.BrandID = BrandMaterial.BrandID
INNER JOIN JawPadMaterial ON JawPadMaterial.MaterialID = BrandMaterial.MaterialID;


DROP TABLE IF EXISTS JawPadSize;

CREATE TABLE JawPadSize (
	JawSizeID INT PRIMARY KEY,
	SizeValue VARCHAR(30) NOT NULL
);

INSERT INTO JawPadSize (JawSizeID, SizeValue)
VALUES (1, '1/2"'), (2, '3/8"'), (3, '3/4"'), (4, '1"'),
(5, 'SF 3/4"'), (6, 'SF 1"'),
(7, '2.0 J0'), (8, '2.0 J1'), (9, '2.0 J2'), (10, '2.0 J3'),
(11, '2.0 J4'), (12, '2.0 J5'), (13, '2.0 J6'), (14, '2.0 J7'),(15, '2.0 J8'),
(16, '.625"'), (17, '0.75"')
;

SELECT * FROM JawPadSize;

DROP TABLE IF EXISTS PadMaterialSize ;

CREATE TABLE PadMaterialSize (
	MaterialID INT,
	JawSizeID INT,
	FOREIGN KEY (JawSizeID) REFERENCES JawPadSize(JawSizeID),
	FOREIGN KEY (MaterialID) REFERENCES JawPadMaterial(MaterialID)
);

INSERT INTO PadMaterialSize (MaterialID, JawSizeID)
VALUES 
(1,1),(1,2), (1,3),(1,4), (2,1),(2,2), (2,3), (2,4), (1,7), (1,8), (1,9), (1,10),(1,11),(1,12),
(1,13), (1,14), (1,15), (3,5) , (3,6), (4,16) ,(4,17), (4,4)
;


SELECT JawPadMaterial.MaterialName, JawPadSize.SizeValue
FROM PadMaterialSize
INNER JOIN JawPadMaterial ON JawPadMaterial.MaterialID = PadMaterialSize.MaterialID
INNER JOIN JawPadSize ON JawPadSize.JawSizeID = PadMaterialSize.JawSizeID;

DROP TABLE IF EXISTS Visor;

CREATE TABLE Visor (
	VisorID INT PRIMARY KEY,
	VisorType VARCHAR(30)
);

INSERT INTO Visor (VisorID, VisorType)
VALUES (1, 'PRIZM'), (2, 'CLEAR'), (3, 'DARK'), (4, '');

SELECT * FROM Visor;

DROP TABLE IF EXISTS ChinStrap;

CREATE TABLE ChinStrap (
	ChinStrapID INT PRIMARY KEY,
	ChinStrapName VARCHAR(30) NOT NULL
);

INSERT INTO ChinStrap (ChinStrapID, ChinStrapName)
VALUES (1, 'Sports Star'), (2,'Sports Star XD'), (3,'Riddell Hard Cup Lrg'), 
(4,'Riddell Hard Cup Med'), (5,'Sports Star Leather');

SELECT * FROM ChinStrap;

DROP TABLE IF EXISTS Players;

CREATE TABLE Players (
	PlayerID INT PRIMARY KEY,
	LastName VARCHAR(30),
	FirstName VARCHAR(30),
	POS VARCHAR(30),
	Jersey INT,
	BrandID INT,
	StylesID INT,
	FacemaskID INT,
	SizeID INT,
	MaterialID INT,
	JawSizeID INT,
	VisorID INT,
	ChinStrapID INT,
	FOREIGN KEY (BrandID) REFERENCES Brand(BrandID),
	FOREIGN KEY (StylesID) REFERENCES Styles(StylesID),
	FOREIGN KEY (FacemaskID) REFERENCES Facemask (FacemaskID),
	FOREIGN KEY (SizeID) REFERENCES Size(SizeID),
	FOREIGN KEY (MaterialID) REFERENCES JawPadMaterial (MaterialID),
	FOREIGN KEY (JawSizeID) REFERENCES JawPadSize(JawSizeID),
	FOREIGN KEY (VisorID) REFERENCES Visor(VisorID),
	FOREIGN KEY (ChinStrapID) REFERENCES ChinStrap(ChinStrapID)	   	 
);

INSERT INTO Players (PlayerID, LastName, FirstName, POS, Jersey, BrandID, StylesID,  SizeID, FacemaskID, MaterialID, JawSizeID, VisorID, ChinStrapID)
VALUES (1, 'Vader',	'Darth', 'QB', 9, 3, 14, 6, 31, 4, 17, 2, 5),
(2, 'Skywalker', 'Luke', 'LB', 15, 1, 6, 4, 2, 2, 2, 1, 3),
(3,	'Solo', 'Han', 'CB', 31, 2, 7, 2, 15, 3, 6, 3, 2),
(4, 'Kenobi', 'ObiWan', 'WR', 81, 1, 5, 4, 7, 1, 9, 4, 5)
;

SELECT * FROM Players;

SELECT Players.PlayerID, Players.LastName, Players.FirstName, Players.POS, Players.Jersey,
Brand.BrandName, Styles.StyleName, Size.Size ,Facemask.FacemaskName, JawPadMaterial.MaterialName, JawPadSize.SizeValue,
Visor.VisorType, ChinStrap.ChinStrapName
FROM Players
INNER JOIN Brand ON Brand.BrandID = Players.BrandID
INNER JOIN Styles ON Styles.StylesID = Players.StylesID
INNER JOIN Size ON Size.SizeID = Players.SizeID
INNER JOIN Facemask ON Facemask.FacemaskID = Players.FacemaskID
INNER JOIN JawPadMaterial ON JawPadMaterial.MaterialID = Players.MaterialID
INNER JOIN JawPadSize ON JawPadSize.JawSizeID = Players.JawSizeID
INNER JOIN Visor ON Visor.VisorID = Players.VisorID
INNER JOIN ChinStrap ON ChinStrap.ChinStrapID = Players.ChinStrapID ; 





