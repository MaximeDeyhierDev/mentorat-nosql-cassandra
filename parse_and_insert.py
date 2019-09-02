import time
# Debut du decompte du temps
start_time = time.time()
import uuid
import re
import sys
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(username='mentorat', password='mentorat')
#instance cluster cree sur l'ip de la machine virutelle 127.0.0.1
cluster = Cluster(['127.0.0.1'],port=9042, auth_provider=auth_provider)
session = cluster.connect()

#On utilise le keyspace logs precedement creer, cf le readme.txt
session.execute("USE logs")

files = ["access_log_Jul95","access_log_Aug95"]
# Boucle pour gerer les fichiers
for fichier in files:
    myFile = open(fichier, encoding = "ISO-8859-1")
    #splitlines permet de faire un split sur les sauts de lignes
    splitedLine = myFile.read().splitlines()
    res = dict()
# Boucle pour gerer les lignes
    for line in splitedLine:
    
        
        #Regex car j'aime ca <3
        output = re.findall(r"^(.+) - - \[(.+)\] \"(\w+) (.+)\" (\d+) ([0-9|-]+)$", line)
        if not output:
            continue
            
      #  sys.exit()
        [(user, timestamp, protocole, linktarget, statuscode, endingvalue)] = output
        #On remplit le dictionnaire
        res["user_id"] = uuid.uuid1()
        res["user"] = user
        res["timestamp"] = timestamp
        res["protocole"] = protocole
        res["linktarget"] = linktarget
        res["statuscode"] = int(statuscode)
        res["endingvalue"] = endingvalue
        
        #On ecrit dans cassandra
        session.execute("""
          INSERT INTO nasa (user_id ,user, timestamp, protocole, linktarget, statuscode, endingvalue)
          VALUES (%(user_id)s, %(user)s, %(timestamp)s, %(protocole)s, %(linktarget)s, %(statuscode)s , %(endingvalue)s)
          """,
          res

        )
        
        
        
#On ferme les fichiers
    myFile.close()   

#On print le temps d'execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))
