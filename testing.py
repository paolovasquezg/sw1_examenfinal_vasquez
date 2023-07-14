import unittest
from app import create_app
from flask_cors import CORS
from flask import Flask
import json

class TestMensajeria(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

    def test_get_contacts(self):
        response = self.client().get("/billetera/contactos/444") # Get contacts normal
        data = json.loads(response.data)
        self.assertEqual(data["success"], True)

    def test_get_contacts_no_number(self):
        response = self.client().get("/mensajeria/contactos/300")  # Get contacts pero la cuenta no existe
        data = json.loads(response.data)
        self.assertEqual(data["statusCode"], 404)

    def test_get_paid(self):
        response = self.client().post("/billetera/pagar/444/500/100") # Hacer un pago normal
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_historial(self):
        response = self.client().get("/billetera/historial/444") # Obtener el historial de una cuenta
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)
