import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gabrieldyna@1",
  database="entreprise"
)

# Créer un curseur pour exécuter des requêtes SQL
mycursor = mydb.cursor()

# Exécuter la requête SQL pour récupérer tous les employés et leur service
mycursor.execute("SELECT e.nom, e.prenom, e.salaire, s.nom AS service FROM employes e JOIN services s ON e.id_service = s.id")

# Afficher le résultat en console
for (nom, prenom, salaire, service) in mycursor:
  print("{} {} - Salaire : {} € - Service : {}".format(nom, prenom, salaire, service))

# Fermer la connexion à la base de données
mydb.close()
