from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://administrateur:progtr00@localhost:5432/nom_de_la_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Programme(db.Model) : 
    __tablename__ = 'programme'

    id = db.Column(db.Integer , primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)

class Groupe_Musculaire(db.Model) : 
    __tablename__ = 'groupe_musculaire'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100),nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    programme_id = db.Column(db.Integer, db.ForeignKey('programme.id'), nullable=False)

class Exercice(db.Model) :
    __tablename__ = 'exercice'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    niveau_maitrise = db.Column(db.Integer, default=1, nullable=False)
    groupe_musculaire_id = db.Column(db.Integer, db.ForeignKey('groupe_musculaire.id'))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "le serveur flask et la base de données communiquent !"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')