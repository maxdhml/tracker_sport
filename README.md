# Tracker Sport 

Projet scolaire d'une application web dynamique de suivi d'entraînement sportif. L'application est développée avec **Python (Flask)**, **PostgreSQL** et conteneurisée avec **Docker**.

---

## Démarrer le Projet

Pour lancer l'application et la base de données :

```bash
docker-compose up --build
```
L'application sera alors accessible à l'adresse : [http://localhost:5000](http://localhost:5000)

Pour arrêter les conteneurs en cours d'exécution :
```bash
docker-compose down
```

---

## Gestion du Proxy (Université vs Maison)

Si vous êtes à l'IUT / Université et que vous devez passer par un proxy pour installer les dépendances Python, ou si vous êtes à la maison :

Pour basculer automatiquement la configuration du proxy dans le `Dockerfile` :
```bash
python switch_proxy.py
```
*Note : Après avoir exécuté ce script, relancez les conteneurs avec `docker-compose up --build`.*

---

## Gestion de la Base de Données

### 1. Importer la base de données existante (`database.sql`)
Si vous souhaitez importer manuellement le fichier de sauvegarde `database.sql` dans la base de données du conteneur en cours d'exécution :

* **Sous PowerShell (Windows) :**
  ```powershell
  Get-Content database.sql | docker exec -i sport_db psql -U athlete -d tracker_db
  ```
* **Sous CMD (Windows) ou Bash (Linux/macOS) :**
  ```bash
  docker exec -i sport_db psql -U athlete -d tracker_db < database.sql
  ```

### 2. Exporter / Sauvegarder la base de données
Pour exporter l'état actuel de votre base de données dans le fichier `database.sql` :

```bash
docker exec -t sport_db pg_dump -U athlete -d tracker_db > database.sql
```

### 3. Se connecter au terminal interactif PostgreSQL (CLI)
Pour exécuter des requêtes SQL directement sur la base de données :

```bash
docker exec -it sport_db psql -U athlete -d tracker_db
```

### 4. Réinitialiser complètement la base de données
Si vous voulez supprimer toutes les données, vider le volume de stockage de PostgreSQL pour repartir de zéro, et recharger les données :

```bash
# Arrêter les conteneurs et supprimer les volumes de stockage associés
docker-compose down -v

# Relancer et reconstruire (le fichier database.sql sera automatiquement exécuté à l'initialisation)
docker-compose up --build
```

---

## Structure principale du Projet

* `app/` : Code source de l'application Flask (routes, modèles, templates HTML, fichiers statiques CSS)
* `database.sql` : Fichier de sauvegarde contenant le schéma SQL et les données initiales
* `Dockerfile` : Instructions de build de l'image de l'application Flask
* `docker-compose.yml` : Configuration des conteneurs pour Flask et PostgreSQL
* `switch_proxy.py` : Script utilitaire pour activer/désactiver le proxy de l'IUT
* `run.py` : Point d'entrée de l'application Flask
