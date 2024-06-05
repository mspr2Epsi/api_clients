import mysql.connector
import os

def connect_to_database():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    database = os.getenv('DB_NAME')
    password = os.getenv('DB_PASSWORD')

    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            database=database,
            password=password,
        )

        if connection.is_connected():
            print("Connexion à la base de données réussie.")
            return connection

    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

    return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée.")