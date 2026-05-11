import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

PROFILE = {
    "nom": "Maxime",
    "objectif": "Sèche et définition musculaire",
    "niveau": "Intermédiaire",
    "poids_actuel": "78 kg"
}