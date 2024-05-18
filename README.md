# EquipmentDatabase
The purpose of this repository is to design and create a database to hold information of specific helmet equipment choices for football players

## Tools
* Microsoft SQL Server used to store data
* Google diagrams used to create ERD diagram
* Python, Tkinter used to create a GUI inorder to streamline the data entry process

## Files
* EquipmentDBCreation.sql --> script to create the equipment database
* EquipmentProject.xlsx --> file that contains the information to be loaded into the database
* Equipment_ERD.png --> picture of my ERD diagram
* GUI.png --> picture of the GUI
* GUI.py --> python script for GUI
* Scripts_for_GUI.sql --> database script for GUI


## Methodology
### Database Design
The Equipment Database was designed as a relational database. It includes 12 tables which are described in more depth in *data dictionaries section*. 

### ERD Diagram
![](Equipment_ERD.png)

### Data Dictionaries 

**Table Name: Brand**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| BrandID | INT | Primary Key | Unique identifier for each brand | 1 |
| BrandName | VARCHAR | | Name of the brand | Schutt | 

**Table Name: Styles**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| StyleID | INT | Primary Kay | Unique identifier for each style | 2 |
| StyleName| VARCHAR | | Name of the style| Zero2-R |

**Table Name: Size**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| SizeID | INT | Primary Key | Unique identifier for each size | 3 |
| Size | VARCHAR | | Size of equipment | M |

**Table Name: Facemask**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| FacemaskID | INT | Primary Key | Unique identifier for each facemask | 4 |
| FacemaskName | VARCHAR | | Name of the facemask | Axiom 2BC-TI |
| BrandID | INT | Foreign Key | Reference to key in *Brand* table | 1 |

**Table Name: JawPadMaterial**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| MaterialID | INT | Primary Key | Unique identifier for each jaw pad material | 5 |
| MaterialName | VARCHAR | | Name of the jaw pad material | Leather |

**Table Name: JawPadSize**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| JawSizeID | INT | Primary Key | Unique identifier for each jaw pad size | 6 |
| SizeValue | VARCHAR | | Size of the jaw pad | 3/8" |

**Table Name: Visor**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| VisorID | INT | Primary Key | Unique identifier for each visor | 7 |
| VisorType | VARCHAR | | They type of visor | CLEAR |

**Table Name: ChinStrap**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| ChinStrapID | INT | Primary Key | Unique identifier for each chin strap | 8 |
| ChinStrapName | VARCHAR | | Name of chin strap | Riddell Hard Cup Lrg |

**Table Name: Players**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| PlayerID | INT | Primary Key | Unique identifier for each player | 9 |
| LastName | VARCHAR | | Players last name | Skywalker |
| FirstName | VARCHAR | | Players first name | Luke |
| POS | VARCHAR | | The position of the football player| QB |
| Jersey | INT | | The number of the players jersey | 81 | 
| BrandID | INT | Foreign Key | Refernce to key in *Brand* table | 1 |
| StyleID | INT | Foreign Key | Reference to key *Styles* table | 2 |
| SizeID | INT | Foreign Key | Reference to key in *Size* table | 3|
| FacemaskID | INT | Foreign Key | Reference to key in *Facemask* table | 4 | 
| MaterialID | INT | Foreign Key | Reference to key *JawPadMaterial* table | 5 |
| JawSizeID | INT | Foreign Key | Reference to key in *JawPadSize* table | 6 |
| VisorID | INT | Foreign Key | Reference to key in *Visor* table | 7 |
| ChinStrapID | INT | Foreign Key | Reference to key in *ChinStrap* table | 8 | 


**Table Name: BrandMaterial**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| BrandID | INT | Foreign Key | References key in *Brand* table | 1 |
| MaterialID | INT | Foreign Key | References key in *JawPadMaterial* table | 5 |

**Table Name: BrandSize**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| BrandID | INT | Foreign Key | References key in *Brand* table | 1 |
| SizeID | INT | Foreign Key | Reference to key in *Size* table | 3 |

**Table Name: PadMaterialSize**
|Field Name | Data Type | Constraint | Description | Example|
|-----------|-----------|------------|-------------|--------|
| MaterialID | INT | Foreign Key | References key in *JawPadMaterial* table | 5 |
| JawSizeID | INT | Foreign Key | Reference to key in *JawPadSize* table | 6 |

