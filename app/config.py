import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Informations du profil (fichier de configuration facile à manipuler)
PROFILE = {
    "nom": "Maxime",
    "objectif": "Sèche et définition musculaire",
    "niveau": "Intermédiaire",
    "poids_actuel": "78 kg"
}

# Niveaux d'acquisition (conformes au cahier des charges)
NIVEAUX = {
    1: "Non acquis",
    2: "En cours d'acquisition",
    3: "Presque acquis",
    4: "Acquis",
    5: "Expert"
}