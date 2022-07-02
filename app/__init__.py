from flask import Flask, request,render_template,redirect, url_for,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
'''
Responsável pelas configurações gerais da aplicação.
Os imports são utilizados pelos demais arquivos.
'''
app = Flask(__name__,template_folder="frontend") 
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db.'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 