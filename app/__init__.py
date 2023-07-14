from flask import Flask, request, jsonify, abort, redirect
from flask_cors import CORS
from models import *
from datetime import datetime

def create_app():
    app = Flask(__name__)
    CORS(app, origin="*")

    @app.route("/billetera/contactos/<minumero>", methods=["GET"])
    def get_contacts(minumero):

        user = None
        contactos = []

        for u in cuentas:
            if int(minumero) == u.numero:
                contactos = u.contactos
                user = 1
        
        if user is None:
            abort(404)

        return jsonify({
            "success": True,
            "contactos": contactos
        })
    
    @app.route("/billetera/pagar/<minumero>/<numdestino>/<valor>", methods=["POST"])
    def get_paid(minumero, numdestino, valor):

        val = False
        user1 = None
        user2 = None

        for u in cuentas:
            if int(minumero) == u.numero:
                val = u.pagar(valor,numdestino)
                user1 = 1
        
        if val is True:
            for u in cuentas:
                if int(numdestino) == u.numero:
                    val = u.recibir(valor,minumero)
                    user2 = 1
        
        if user1 is None or user2 is None:
            abort(404)
        
        if val is True:
            return jsonify({
                "success": True,
                "mensaje": "Realizado en " + str(datetime.now())
            })
        else:
            return jsonify({
                "success": True,
                "mensaje": "No realizado"
            })

    @app.route("/billetera/historial/<minumero>", methods=["GET"])
    def get_historial(minumero):

        user = None
        list = []

        for u in cuentas:
            if int(minumero) == u.numero:
                list = u.historial
                user = 1

        if user is None:
            abort(404)

        return jsonify({
            "success": True,
            "historial": list
        })  
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'statusCode': 404,
            'message': 'Resource not found'
        }), 404

    return app
