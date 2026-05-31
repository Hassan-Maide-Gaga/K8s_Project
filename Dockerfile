FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copier le code source
COPY . .

# Exposer le port
EXPOSE 5000

# Utiliser Gunicorn en production (stable)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]