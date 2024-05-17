USE EquipmentProject;

DROP TABLE IF EXISTS Test;

CREATE TABLE Test (
	PlayerID INT PRIMARY KEY IDENTITY,
	LastName VARCHAR(30),
	FirstName VARCHAR(30),
	POS VARCHAR(30),
	Jersey INT,
	BrandID INT,
	StylesID INT,
	SizeID INT,
	FacemaskID INT,
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

SELECT * FROM Test;


SELECT Test.PlayerID, Test.LastName, Test.FirstName, Test.POS, Test.Jersey,
Brand.BrandName, Styles.StyleName, Size.Size ,Facemask.FacemaskName, JawPadMaterial.MaterialName, JawPadSize.SizeValue,
Visor.VisorType, ChinStrap.ChinStrapName
FROM Test
INNER JOIN Brand ON Brand.BrandID = Test.BrandID
INNER JOIN Styles ON Styles.StylesID = Test.StylesID
INNER JOIN Size ON Size.SizeID = Test.SizeID
INNER JOIN Facemask ON Facemask.FacemaskID = Test.FacemaskID
INNER JOIN JawPadMaterial ON JawPadMaterial.MaterialID = Test.MaterialID
INNER JOIN JawPadSize ON JawPadSize.JawSizeID = Test.JawSizeID
INNER JOIN Visor ON Visor.VisorID = Test.VisorID
INNER JOIN ChinStrap ON ChinStrap.ChinStrapID = Test.ChinStrapID ; 


