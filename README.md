# Openclassrooms / Projet12 - parcours "Developpeur d'application python"

Date démarrage: Decembre 2022 

## Titre du projet:  
Développez une architecture back-end sécurisée en utilisant Django ORM

## Mentor:
Idriss Benjeloun

## Description:   
Ce projet concerne le  developpement d'une API en utilisant Django REST.

les fonctionnalités du projet sont comme suit:

- Il s'agit d'une application de suivi CRM

Le type des champs est indiqué dans un modèle Django. 
1. User : 
3. Event : 
4. Contract : 
5. Sales: 
6. Support:

## Technologies utilisées:
- framework Django REST;
- PostgreSQL comme gestionnaire de base de données ,

 

## Exécution du programme
    - installer la derniere version de django (https://docs.djangoproject.com/en/4.1/topics/install/)
    - Créer un dossier projet sur votre machine comme repository local
    - Clonner le repo distant dans votre repository local
    - Se positionner dans le  répertoire "Projet12" avec:
        >> cd Projet12
    - Créer l'environnement virtuel avec:
        >> env python -m venv env
    - Activer l'environnement virtuel avec :
        >> source env/bin/activate
    - Installez les modules necessaires à l'aide du fichier requirement.txt avec:   
        >> pip install -r requirements.txt  
    - Exécuter la migration de la base de données (les modèles) avec: 
        >> python manage.py migrate
    - Lancer le serveur (en fonction de votre version de python) avec :
        >>python manage.py runserver ou >> python3 manage.py runserver
    - Lancer le site à partir de l'URL:  http://127.0.0.1:8000
      ou via un outil comme Postman.
    - l'administration de Django est accessible via le lien http://127.0.0.1:8000/admin/

Remarque: Assurez-vous que votre version de Python est l'une de celles prises 
en charge par la dernière version de Django :
https://docs.djangoproject.com/en/4.1/faq/install/#faq-python-version-support

Nota : les versions appliquées pour ce projet: 
    
    - python : 3.10.5
    - Django : 4.1.1
    - IDE utilisé: pycharm V2022.2.1 (Community Edition)
    - postman a été utilisé pour tester les requêtes de l'API
    - Lucidchart pour la création du Diagramme entité-relation

## Historique des Versions:    

 *Principales versions sous Github*

 - PEP8 verification - 19/11/2022
 - update

 - First version - 28/12/2022

## Acknowledgments (code inspiration): 
- https://olivierlemoigne.com/posts/django-postgres/
- https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django?gclid=CjwKCAiAkrWdBhBkEiwAZ9cdcI07zMyqUJkmC1UZye-PofhFdt640FUvQji-5Fv3jWIQlqeSZOw8lhoCjsAQAvD_BwE
- https://www.youtube.com/watch?v=HEV1PWycOuQ
- https://www.enterprisedb.com/postgres-tutorials/how-create-postgresql-database-and-users-using-psql-and-pgadmin?gclid=CjwKCAiA-8SdBhBGEiwAWdgtcA0SaXwqY8RV_WGz-0D-XcimKinYOCH1NFITezF3lqhGpNiRb3MCnBoCGyIQAvD_BwE
- https://docs.netbox.dev/en/stable/installation/1-postgresql/
- https://pullanswer.com/questions/unable-to-create-the-django_migrations-table-during-installation