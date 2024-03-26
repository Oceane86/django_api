# django_api

Python - Créer un site avec Django pour afficher des listes de jobs

Installation
Django
Prérequis
Python 3.x
pip
Étapes d'installation

Installer les dépendances :
bash
Copy code
pip install -r requirements.txt
Démarrage du projet
Créer un projet Django :
bash
Copy code
django-admin startproject config .
Modifier la configuration de la base de données dans config/settings.py :
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Appliquer les migrations initiales :
bash

python manage.py migrate
Créer un superutilisateur :
bash

python manage.py createsuperuser
Lancer le serveur de développement :
bash

python manage.py runserver
Structure du projet
Fichiers importants
config/settings.py: Réglages globaux
config/urls.py: Routes
www/: Notre application
www/models.py: Définition des modèles
www/views.py: Les vues
www/templates/: Les templates
Gestion de la base de données
Créer un fichier de migration
bash

python manage.py makemigrations
Appliquer les migrations
bash

python manage.py migrate
Importer/exporter des données
Exporter la base de données en format JSON :
bash

python manage.py dumpdata > db.json
Importer des données :
bash
Copy code
python manage.py loaddata user.json
