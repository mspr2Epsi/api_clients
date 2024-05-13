from db_connector import connect_to_database, close_connection
from flask import Flask, request, jsonify
from roles import  read_possible,update_possible,creation_possible,delete_possible

db_connection = connect_to_database()
cursor = db_connection.cursor()
app = Flask(__name__)

@app.route('/clients', methods=['GET'])
def get_clients():
    token = request.headers.get('Authorization')
    if read_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401    
    
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    return jsonify({'clients': clients})

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    token = request.headers.get('Authorization')
    if read_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401       
     
    cursor.execute("SELECT * FROM clients WHERE ClientID = %s", (client_id,))
    client = cursor.fetchone()
    if client:
        return jsonify({'client': client})
    else:
        return jsonify({'message': 'Client not found'}), 404

@app.route('/clients', methods=['POST'])
def create_client():
    token = request.headers.get('Authorization')
    if creation_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401        
    
    data = request.get_json()
    required_keys = ['Nom', 'Prenom', 'Telephone', 'Age', 'Email', 'Adresse', 'RoleID']
    if not all(key in data for key in required_keys):
        return jsonify({'message': 'Incomplete data'}), 400
    cursor.execute("""
        INSERT INTO clients (Nom, Prenom, Telephone, Age, Email, Adresse, RoleID) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (data['Nom'], data['Prenom'], data['Telephone'], data['Age'], data['Email'], data['Adresse'], data['RoleID']))
    db_connection.commit()
    return jsonify({'message': 'Client created successfully'}), 201

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    token = request.headers.get('Authorization')
    if update_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401 
           
    data = request.get_json()
    required_keys = ['Nom', 'Prenom', 'Telephone', 'Age', 'Email', 'Adresse', 'RoleID']
    if not all(key in data for key in required_keys):
        return jsonify({'message': 'Incomplete data'}), 400
    cursor.execute("""
        UPDATE clients 
        SET Nom = %s, Prenom = %s, Telephone = %s, Age = %s, Email = %s, Adresse = %s, RoleID = %s
        WHERE ClientID = %s
        """, (data['Nom'], data['Prenom'], data['Telephone'], data['Age'], data['Email'], data['Adresse'], data['RoleID'], client_id))
    db_connection.commit()
    if cursor.rowcount > 0:
        return jsonify({'message': 'Client updated successfully'}), 200
    else:
        return jsonify({'message': 'Client not found'}), 404

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    token = request.headers.get('Authorization')
    if delete_possible(token) != True:
        return jsonify({'message': 'Unauthorized'}), 401
    
    cursor.execute("SELECT * FROM clients WHERE ClientID = %s", (client_id,))
    client = cursor.fetchone()
    if client is None:
        return jsonify({'message': 'Client not found'}), 404

    cursor.execute("DELETE FROM clients WHERE ClientID = %s", (client_id,))
    db_connection.commit()

    return jsonify({'message': 'Client deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)