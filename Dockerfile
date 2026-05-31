FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier requirements.txt d'abord (meilleur caching Docker)
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copier tout le code source
COPY . .

# Exposer le port
EXPOSE 5000

# Démarrer avec Gunicorn (serveur de production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]