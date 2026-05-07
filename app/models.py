from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Programme(db.Model):
    __tablename__ = 'programme'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    groupes = db.relationship('GroupeMusculaire', backref='programme', lazy=True)

class GroupeMusculaire(db.Model):
    __tablename__ = 'groupe_musculaire'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    programme_id = db.Column(db.Integer, db.ForeignKey('programme.id'), nullable=False)
    exercices = db.relationship('Exercice', backref='groupe', lazy=True)

class Exercice(db.Model):
    __tablename__ = 'exercice'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    niveau_maitrise = db.Column(db.Integer, default=1, nullable=False)
    groupe_id = db.Column(db.Integer, db.ForeignKey('groupe_musculaire.id'), nullable=False)