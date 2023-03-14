import mysql.connector

# Connectez-vous à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Gabrieldyna@1",
  database="LaPlateforme"
)

# Récupérez les données de la table "etudiants"
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM salles")
resultats = mycursor.fetchall()

# Affichez les résultats de la requête
for resultat in resultats:
  print(resultat)