CREATE TABLE Kampaaja (\
id INTEGER,\
date_created DATE,\
date_modified DATE,\
name VARCHAR(144),\
username VARCHAR(144),\
password VARCHAR(144),\
PRIMARY KEY (id)\
); 

CREATE TABLE Asiakas (\
date_created DATE,\
date_modified DATE,\
firstName VARCHAR(144),\
lastName VARCHAR(144),\
phoneNumber INTEGER,\
PRIMARY KEY (phoneNumber)\
);

CREATE TABLE Aika (\
id INTEGER,\
pvm DATE,\
aika_h INTEGER,\
aika_min INTEGER,\
vapaa INTEGER,\
kampaaja_id INTEGER,\
PRIMARY KEY (id),\
FOREIGN KEY (kampaaja_id) REFERENCES Kampaaja(id)\
);

CREATE TABLE Varaus (\
id INTEGER,\
date_created DATE,\
date_modified DATE,\
kampaaja_id INTEGER,\
asiakas_id INTEGER,\
aika_id INTEGER,\
PRIMARY KEY (id)\
FOREIGN KEY (kampaaja_id) REFERENCES Kampaaja(id),\
FOREIGN KEY (asiakas_id) REFERENCES Asiakas(id),\
FOREIGN KEY (aika_id) REFERENCES Aika(id),\
);

