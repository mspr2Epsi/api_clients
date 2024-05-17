from db_connector import connect_to_database, close_connection
from flask import Flask, request, jsonify
from roles import  read_possible,update_possible,creation_possible,delete_possible
import pika
from datetime import datetime

# Connection à RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
channel = connection.channel()

# Assurer que la queue existe
channel.queue_declare(queue='message_broker_client')

# Connexion à la base de données
db_connection = connect_to_database()
cursor = db_connection.cursor()

app = Flask(__name__)

@app.route('/clients', methods=['GET'])
def get_clients():
    begin_time = datetime.now()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  get_clients")
    token = request.headers.get('Authorization')
    if read_possible(token) != True:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement get_clients termine")
        return jsonify({'message': 'Unauthorized'}), 401    
    
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)}  - Code 200 traitement get_clients termine")
    return jsonify({'clients': clients})

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    begin_time = datetime.now()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  get_clients by ID")
    token = request.headers.get('Authorization')
    if read_possible(token) != True:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement get_clients by ID termine")
        return jsonify({'message': 'Unauthorized'}), 401       
     
    cursor.execute("SELECT * FROM clients WHERE ClientID = %s", (client_id,))
    client = cursor.fetchone()
    if client:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)}  - Code 200 traitement get_clients by ID termine")
        return jsonify({'client': client})
    else:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)}  - Code 404 traitement get_clients by ID termine")
        return jsonify({'message': 'Client not found'}), 404

@app.route('/clients', methods=['POST'])
def create_client():
    begin_time = datetime.now()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  create_client")    
    token = request.headers.get('Authorization')
    if creation_possible(token) != True:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement create_client termine")        
        return jsonify({'message': 'Unauthorized'}), 401        
    
    data = request.get_json()
    required_keys = ['Nom', 'Prenom', 'Telephone', 'Age', 'Email', 'Adresse']
    if not all(key in data for key in required_keys):
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 400 traitement create_client termine")          
        return jsonify({'message': 'Incomplete data'}), 400
    cursor.execute("""
        INSERT INTO clients (Nom, Prenom, Telephone, Age, Email, Adresse) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (data['Nom'], data['Prenom'], data['Telephone'], data['Age'], data['Email'], data['Adresse']))
    db_connection.commit()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 201 traitement create_client termine")      
    return jsonify({'message': 'Client created successfully'}), 201

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    begin_time = datetime.now()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  update_client")        
    token = request.headers.get('Authorization')
    if update_possible(token) != True:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement update_client termine")    
        return jsonify({'message': 'Unauthorized'}), 401 
           
    data = request.get_json()
    required_keys = ['Nom', 'Prenom', 'Telephone', 'Age', 'Email', 'Adresse']
    if not all(key in data for key in required_keys):
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 400 traitement update_client termine")           
        return jsonify({'message': 'Incomplete data'}), 400
    cursor.execute("""
        UPDATE clients 
        SET Nom = %s, Prenom = %s, Telephone = %s, Age = %s, Email = %s, Adresse = %s
        WHERE ClientID = %s
        """, (data['Nom'], data['Prenom'], data['Telephone'], data['Age'], data['Email'], data['Adresse'], client_id))
    db_connection.commit()
    if cursor.rowcount > 0:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 200 traitement update_client termine")           
        return jsonify({'message': 'Client updated successfully'}), 200
    else:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 404 traitement update_client termine")           
        return jsonify({'message': 'Client not found'}), 404

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    begin_time = datetime.now()
    channel.basic_publish(exchange='', routing_key='message_broker_client', body=f" {begin_time.strftime("%Y-%m-%d %H:%M:%S")} Debut du traitement  delete_client")      
    token = request.headers.get('Authorization')
    if delete_possible(token) != True:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 401 traitement delete_client termine")           
        return jsonify({'message': 'Unauthorized'}), 401
    
    cursor.execute("SELECT * FROM clients WHERE ClientID = %s", (client_id,))
    client = cursor.fetchone()
    if client is None:
        channel.basic_publish(exchange='', routing_key='message_broker_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 404 traitement delete_client termine")         
        return jsonify({'message': 'Client not found'}), 404

    cursor.execute("DELETE FROM clients WHERE ClientID = %s", (client_id,))
    db_connection.commit()
    channel.basic_publish(exchange='', routing_key='./_client', body=f"Temps d'execution {(datetime.now()-begin_time)} - Code 200 traitement delete_client termine") 
    return jsonify({'message': 'Client deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)