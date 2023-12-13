---
Authors : Moi
Category : B3 DEV
Tags : DCP, 2023-2024, B3_DEV, Python
Date : 0ç-11-2023
Title : Python - Django api
---

# REST API 

## A quoi sert une API

- interroger une bdd
- `Client <-> serveur`
- Client
    - requete (method + route)
    - header
    - payload ( données json)
    - cookies
- serveur 
    - code http
    - header
    - content
    - cookies

## Routes

- https://localhost/api/v1/
- https://localhost/api/v1/authors/
- https://localhost/api/v1/authors/1
- https://localhost/api/v1/authors/1/books/
- https://localhost/api/v1/authors/1/books/7
- https://localhost/api/v1/books/7
- https://localhost/api/v1/books/7/authors/

- https://localhost/api/v1/authors/?page=4&search=vernes


## Request method

| Method  | Action              | Route                 |
| ------  | ------------------- | --------------------- |
| GET     | SELECT              | authors/ ou authors/1 |
| POST    | INSERT              | authors/
| PUT     | UPDATE (tout)       | authors/1
| PATCH   | UPDATE  (selection) | authors/1
| DELETE  | DELETE              | authors/1
| OPTIONS | ?                   |


## QUI ?

- Authentification : qui es tu ?
    - Basic Auth
    - Token-based Auth
    - OAuth2
    - JSON Web Tokens (JWT)
- Autorisation : que peux tu faire ?


## Monter une API

- Flask
- FastAPI
- Django Rest Framework



# Projet 

- Django (venv, git, django...)
- Tester l'api : "Rest Client"

- Idée... "bookmarks" : Gestion des sites favoris
    - id
    - created_at
    - updated_at 
    - user_id
    - url
    - name
    - comment
    - tags


``` sh
./venv/Scripts/pip install Django 
./venv/Scripts/pip install djangorestframework
./venv/Scripts/pip freeze > requirements.txt



``` sh
django-admin startproject config .
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


django-admin startapp bookmarks
```



si cest un site `models -> views/template -> urls`

SI API `models -> Serializer -> views/template -> urls`

# Options 

- pagination
- moteur de recherche
- options tri
- sécurité

# Afficher

- Créer un fichier index.html qui charge l'api et affiche les données sous forme de ul/li/s
    - Si c'est l'index du site = créer vue + template + route
    - fichier indépendant : fetch await/async ou promesse ou axios = CORS


# FRONT 

- Créer une app "front"
 `django-admin startapp front`
  pas de migration de model
- Modifier le settings :  `INSTALLED_APPS`
- Créer un dossier  `front/template/ => index.html `
- Modifier la vue  `front/views.py`
- Modifier la route `front/urls.py` et `config/urls.py`
- Créer un dossier static pour js + cs... (et voir settings...)



# Régler les CORS

```sh
.venv/Scripts/pip3 install django-cors-headers
```

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'corsheaders'

]



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
    ]



# Sécurisation

- Avoir plusieurs utilisateurs
  http://127.0.0.1:000/admin/
  oce / a12345678a

- djoser
    - `config/settings.py` = permissions
    - `config/urls.py` = routes pour s'authentifier (qui est ouverte)


``` sh
./venv/Scripts/pip install djoser
./venv/Scripts/pip freeze > requirements.txt
python manage.py runserver

python manage.py makemigrations
python manage.py migrate


django-admin startapp bookmarks
```



- utilisation de l'api
    - récupérer un token
    - envoyer à chaque requête

# Finalisation 

- Créer dossier Static pour css + json et voir settings
    - Créer le dossier
    - le déclarer dans les settings
    - l'utiliser dans le template