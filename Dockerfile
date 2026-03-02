# On part d'une image Python officielle
FROM python:3.9-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie le fichier des dépendances et on les installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le contenu du projet dans le conteneur
COPY . .

# La commande qui se lancera au démarrage du conteneur
CMD ["python", "evaluate.py"]