import unittest
from unittest.mock import  patch
from api_clients import app


class TestClients(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    #récupérer client avec token valide
    def test_get_clients_with_valid_token(self):
        with unittest.mock.patch('api_clients.read_possible', return_value=True):
            response = self.app.get('/clients', headers={'Authorization': 'valid_token'})
            self.assertEqual(response.status_code, 200)

    #récupérer client avec token invalide
    def test_get_clients_with_invalid_token(self):
        with unittest.mock.patch('api_clients.read_possible', return_value=False):
            response = self.app.get('/clients', headers={'Authorization': 'invalid_token'})
            self.assertEqual(response.status_code, 401)

    #créer un client en précisant toutes les info obligatoire
    def test_create_client_with_valid_data(self):
        with patch('api_clients.creation_possible', return_value=True):
            data = {
                'Nom': 'John',
                'Prenom': 'Doe',
                'Telephone': '1234567890',
                'Age': 30,
                'Email': 'john@example.com',
                'Adresse': '123 Street',
                'RoleID': 1
            }
            response = self.app.post('/clients', json=data, headers={'Authorization': 'valid_token'})
            self.assertEqual(response.status_code, 201)
            data = response.get_json()
            self.assertEqual(data['message'], 'Client created successfully')    

    #créer un client avec token invalide
    def test_create_client_with_invalid_token(self):
        with patch('api_clients.creation_possible', return_value=False):
            data = {
                'Nom': 'John',
                'Prenom': 'Doe',
                'Telephone': '1234567890',
                'Age': 30,
                'Email': 'john@example.com',
                'Adresse': '123 Street',
                'RoleID': 1
            }
            response = self.app.post('/clients', json=data, headers={'Authorization': 'invalid_token'})
            self.assertEqual(response.status_code, 401)
            data = response.get_json()
            self.assertEqual(data['message'], 'Unauthorized')

    #créer un client qans préciser toutes les données obligatoires
    def test_create_client_with_incomplete_data(self):
        with patch('api_clients.creation_possible', return_value=True):
            data = {
                'Nom': 'John',
                'Prenom': 'Doe',
                'Telephone': '1234567890',
            }
            response = self.app.post('/clients', json=data, headers={'Authorization': 'valid_token'})
            self.assertEqual(response.status_code, 400)
            data = response.get_json()
            self.assertEqual(data['message'], 'Incomplete data')


    def test_update_client_with_invalid_token(self):
        with patch('api_clients.update_possible', return_value=False):
            client_id = 1
            data = {
                'Nom': 'Updated Name',
                'Prenom': 'Updated Firstname',
                'Telephone': '1234567890',
                'Age': 30,
                'Email': 'updated_email@example.com',
                'Adresse': 'Updated Address',
                'RoleID': 1
            }
            response = self.app.put(f'/clients/{client_id}', json=data, headers={'Authorization': 'invalid_token'})
            self.assertEqual(response.status_code, 401)
            data = response.get_json()
            self.assertEqual(data['message'], 'Unauthorized')

    def test_update_client_with_incomplete_data(self):
        with patch('api_clients.update_possible', return_value=True):
            client_id = 1
            data = {
                'Nom': 'Updated Name',
                'Prenom': 'Updated Firstname',
                'Telephone': '1234567890',
                'Age': 30,
                'Email': 'updated_email@example.com'
            }
            response = self.app.put(f'/clients/{client_id}', json=data, headers={'Authorization': 'valid_token'})
            self.assertEqual(response.status_code, 400)
            data = response.get_json()
            self.assertEqual(data['message'], 'Incomplete data')



    def test_delete_client_with_invalid_token(self):
        with patch('api_clients.delete_possible', return_value=False):
            client_id = 1
            response = self.app.delete(f'/clients/{client_id}', headers={'Authorization': 'invalid_token'})
            self.assertEqual(response.status_code, 401)
            data = response.get_json()
            self.assertEqual(data['message'], 'Unauthorized')

    def test_delete_nonexistent_client(self):
        with patch('api_clients.delete_possible', return_value=True):
            client_id = 999  # assuming a non-existent client ID
            response = self.app.delete(f'/clients/{client_id}', headers={'Authorization': 'valid_token'})
            self.assertEqual(response.status_code, 404)
            data = response.get_json()
            self.assertEqual(data['message'], 'Client not found')






if __name__ == '__main__':
    unittest.main()