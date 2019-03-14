# "*Distributed Database*"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Vorarbeit
### Prerequisits
- 2 virtuelle Maschinen mit PostgreSQL installiert.
- 2 Host Maschinen

### Vorbereitungsschritte
#### Datenbank
Als erstes muss die Datenbank erstellt werden. Dazu wurde eine fertige Datenbank verwendet und in das 
System integriert. Dazu wurde die Software _WinSCP_ verwendet, um das .zip File mit der Datenbank vom Host auf die VM zu verschieben.  
Anschließend hat man zwei Zip-Files __"ds21.tar.gz"__ und __"ds21_postgresql.tar.gz"__  
Diese Files werden anschließend entzippt. 
```bahs
tar -xvzf <filename>.tar.gz
```
Als nächster Schritt muss die Datenbank noch manuell erstellt werden. Das geht mit folgenden Befehlen:
```bash
psql

DROP DATABASE IF EXISTS DS2;
CREATE DATABASE DS2;
CREATE USER DS2 WITH SUPERUSER;
ALTER USER DS2 WITH PASSWORD 'ds2';
```

Um Tabellen und Einträge in die Datenbank einzufügen, kann das folgende Script verwendet werden.
```bash
sh ds2/pgsqlds2/pgsqld2_create_all.sh
```
Anschließend kann man überprüfen ob die Tabellen in der Datenbank erstellt wurden mit folgendem Befehl:
```bash
psql -d ds2

\dt
```
#### VM anpassen
Um später die VM von außen zu erreichen muss bei den Netzwerkeinstellungen __"Bridged"__ eingestellt sein.

## Implementierung
### Horizontale Fragmentierung
### Vertikale Fragmentierung
### Kombinierte Fragmentierung


## Fragestellungen
- Frage 1: _Was versteht man unter dem Begriff Allokation beim Entwurf einer verteilten Datenbank?_  
Antwort 1: Unter der Allokation versteht man die Verteilung der Fragmente auf verschiedene Stationen (Datenbanken).

- Frage 2: Beschreiben Sie die Korrektheitsanforderungen bei der Fragementierung von verteilten Datenbanken.

- Frage 3: Wie geht man bei einer horizontalen DB-Fragemtierung vor? Beantworten Sie diese Frage anhand eines Beispiels.

- Frage 4: _Die Transparenz von verteilten Datenbanken ist in mehrere Stufen gegliedert. Beschreiben Sie die Lokale-Schema-Transparenz._  
Antwort 4: Es gibt __3 Arten der Transparenz:__  
    - __Fragmentierungstransparenz:__ Dabei weiß der Benutzer nicht ob es eine Fragmentierung gibt und wo welche Daten sind. Er macht einfach eine Query und das DBMS kümmert sich um den Rest.
    - __Allokationstransparenz:__ Der Benutzer sieht, dass es verschiedene Fragmente gibt, weiß aber nicht auf welchen Servern die sich befinden.
    - __Lokale Schema-Transparenz:__ Der Benutzer sieht die verschiedenen Fragmente und wo diese gespeichert sind. Er weiß daher ganz genau was er wo selecten muss.
- Was versteht man unter dem Begriff Fragmentierung beim Entwurf einer verteilten Datenbank?  
- Wie sieht eine vertikale Fragmentierung aus? Erklären Sie die Begriffe anhand von einem Beispiel.

## Quellen
[1] - [https://stackoverflow.com/questions/658395/find-the-number-of-columns-in-a-table](https://stackoverflow.com/questions/658395/find-the-number-of-columns-in-a-table)    
[2] - [https://www.dbai.tuwien.ac.at/education/dbs/WS2010/folien/Kapitel16.pdf](https://www.dbai.tuwien.ac.at/education/dbs/WS2010/folien/Kapitel16.pdf)  