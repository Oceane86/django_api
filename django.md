---
Authors : Moi
Category : B3 DEV
Tags : DCP, 2023-2024, B3_DEV, Python
Date : 02-11-2023
Title : Python - Créer un site avec Django
---

# On y va 

## Installation et ligne de commandes

# Créer un projet Python / Django
```sh
- Git : Configurer un Github
- Dossier
    - .gitignore :
        - venv : python -m venv venv ensuite source venv/Scripts/activate
        - installer django : ./venv/Scripts/pip install django
        - ./venv/Scripts/django-admin --version
        - sqlite (sauf si interro)


- Créer in fichier requirements.txt avec toutes les dépendances (mettre à jour à chaque "pip install") 
`venv/Scripts/pip freeze > requirements.txt`
Pour info : installer depuis le fichier : `venv/Scripts/pip install -r > requirements.txt`
```

```sh
# Démarrage du projet 

django-admin startproject config .

# Modifier la config pour la base de données
# config/settings.py : DATABASE = {}

# Configurer la base de données : tables systèmes
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Ajouter l'app ou plusieurs
django-admin startapp www

# Lancer le serveur
python manage.py runserver

# Pour arrêter le serveur
Ctrl + C

# SI MODIF des models
python manage.py makemigrations
python manage.py migrate

# De temps à autre... (import de données)
python manage.py...

# Porter une base de données en format json
venv/Scripts/python manage.py dumpdata > db.json

venv/Scripts/python manage.py dumpdata www.categories > www.categories.json
venv/Scripts/python manage.py dumpdata --exclude auth.permission > db.json

venv/Scripts/python manage.py loadata user.json

# Pour changer le mots de passe
venv/Scripts/python manage.py changepassword ringo

```


## Le projet et ses fichiers

| fichier             | rôle                            |
| ------------------- | ------------------------------- |
| configs/settings.py | réglages globaux                |
| configs/urls.py     | routes                          |
| templates/          | templates globaux               |
| wwww/               | notre app                       |
| www/models.py       | ORM classes "base de données    |
| www/admin.py        | déclarer pour l'interface admin |
| www/views.py        | les vues (liée au modèle)       |
| www/urls.py         | routes (liée aux vues)          |
| www/templates/      | les templates locaux            |


models -> views/template -> urls



### Les règlages globaux

### Routes

- routes globales `config/urls.py`
    - chemin vers l'admin
    - gestion des MEDIA_URL
    - importer les routes locales

## Models

- Définition des `class Categories(models.Model):`
- liste des "attributs"
    `content = model.TextField("Contenu", blank=True)`
    - Types :
        - Champs "standard" : TextField, CharField, DateTimeField,SlugField, ...
        - Champs "automatique" : id, DateTimeField (auto_now_add, auto_now)
        - Champs "pièces jointes" : images, fichiers (nécessite une configuration en +)
        - Champs "relations" : 
            - Créer le "model" de la table "étrangère"
            - ForeignKey : clef étrangère, 1-N vers table de ref
            - ManyToManyField : table de jointure, N-N vers table de ref
            - OneToOne : 1-1
    - Options
        - Dépendent du type (voir la doc)
        - blank=True
        - on_delete (gestion des relations)
          CASCADE, PROTECT, SET_NULL, DO_NOTHING...
        - max_length = 255
- Méthodes
    - `__str__(self)` : représentation textuelle
- class
    - `class Meta:` : verbose name 
- Si modifs : MIGRATION...


# Vues

- 2 parties : 
    - python : class dans `views.py`
    - html : jinja + templates
 
- python (class)
    - Standard (simplifié) : ListView, DetailView 
    - Sur mesure (fonctions)

http://127.0.0.1:8000/api/v1/
http://127.0.0.1:8000/api/v1/bookmarks
http://127.0.0.1:8000/api/v1/bookmarks/1



# OPTIONS

- Pagination
- Moteur de recherche
- Option Tri
- Sécurité

