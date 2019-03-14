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

## Quellen
