import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') #sécurisé la session avec la clé
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #URL de connexion vers bdd
    SQLALCHEMY_TRACK_MODIFICATIONS = False #désactive suivi (économie)

# Informations de la page d'accueil
PROFILE = {
    "nom": "Maxime",
    "objectif": "Sèche et définition musculaire",
    "niveau": "Intermédiaire",
    "poids_actuel": "78 kg"
}

# Bareme (modifiable)
NIVEAUX = {
    1: "Non acquis",
    2: "En cours d'acquisition",
    3: "Presque acquis",
    4: "Acquis",
    5: "Expert"
}