#version python allégée
FROM python:3.10-slim 

#création du dossier /app dans le conteneur
WORKDIR /app

#pour enregistrer dans le cache du conteneur
COPY requirements.txt requirements.txt

# installation des dépendances
RUN pip install -r requirements.txt

#copie le reste du code
COPY . .

#demarrage python run.py
CMD ["python", "run.py"]