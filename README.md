# mentorat-nosql-cassandra
Premiers pas avec cassandra. Dans ce repo ce trouve le script de nettoyage et d'ingesion des données ainsi que les fichiers sources.

*J'ai eu pas mal de probleme avec la version 2.7 de python, donc je suis passé a la v3*\n
sudo apt-get install python3

*installation de pip pour les imports*
sudo apt install python3-pip

*installation de cassandra-driver*
pip3 install cassandra-driver


*Pour acceder au shell de Cassandra, il faut taper **cqlsh** dans le terminal*


# 1/ Créer un Keyspace

Il s'agit d'une étape obligatoire. Si on pouvait faire une comparaison avec le SQL, il s'agit d'une base.
cqlsh.> CREATE KEYSPACE monKeySpace
WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};

source:
https://www.tutorialspoint.com/cassandra/cassandra_create_keyspace.htm

# 2/ Créer une table

Maintenant que notre keyspace existe ( on peut lister les keyspaces avec DESCRIBE keyspaces;)
Il faut créer une table...
La syntaxe est très proche du SQL
CREATE TABLE monKeySpace.maTable ( id UUID PRIMARY KEY, lastname text, birthday timestamp);

Pour le TP logs nasa : create table logs.nasa(user_id UUID PRIMARY KEY, user text, timestamp text, protocole text, linkTarget text, statusCode int, endingValue text);

note : UUID s'importe en general ( sur python par exemple) et celui ci va se charger de créer des clés seul)

source:
https://docs.datastax.com/en/archived/cql/3.3/cql/cql_using/useCreateTable.html

# 3/ CRUD
Pour toutes les commandes CRUD, c'est très proche du SQL
