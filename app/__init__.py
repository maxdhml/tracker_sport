from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy() #parler à la BDD
csrf = CSRFProtect() #Sécurité contre le piratage de formulaires

def create_app():
    app = Flask(__name__) # Création de l'application web de base
    app.config.from_object('app.config.Config') #reglages de l'app via config.py

    db.init_app(app) #active bdd a app
    csrf.init_app(app) #active csrf a app 

    with app.app_context():
        from . import routes #importe les url 

    return app #prete à démarrer