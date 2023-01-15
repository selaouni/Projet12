# Openclassrooms / Projet12 - parcours "Developpeur d'application python"

Date démarrage: Decembre 2022 

## Titre du projet:  
Développez une architecture back-end sécurisée en utilisant Django ORM

## Mentor:
Idriss Benjeloun

## Description:   
Ce projet concerne le  developpement d'une API  de suivi CRM utilisant le frameworke Django REST.

L'application Django fournit :
- un ensemble d’endpoints sécurisés pour l’API avec comme base de données PostgreSQL pour permettre 
- les opérations CRUD (créer, lire, mettre à jour et supprimer) appliquées aux 
divers objets CRM. 
- Une interface front-end simple à l'aide du site d'administration Django, qui permet aux 
utilisateurs autorisés de gérer l'application, d'accéder à l'ensemble des modèles et de vérifier 
la configuration de la base de données

Modèls :
1. User 
3. Event 
4. Contract 
5. Sales
6. Support
7. Event_status

## Technologies utilisées:
- framework Django REST;
- python : 3.10.5
- PostgreSQL 15 comme gestionnaire de base de données ,
- postman a été utilisé pour tester les requêtes de l'API 
- Lucidchart pour la création du Diagramme entité-relation(ERD)

 

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

Nota : 
    - IDE utilisé: pycharm V2022.2.1 (Community Edition)


## Historique des Versions: 

 *Principales versions sous Github*
 - jwt authentication serializer code - 11/01/2023
 - url.py by application - 11/01/2023
 - updated with "author_user_id" attribut for Client , Contract and Event models - 11/01/2023
 - First version of permissions - 04/01/2023
 - Updated with admin django customisation - 04/01/2023
 - Setting Update for DATABASE, REST_FRAMEWORK and AUTH_USER_MODEL - 02/01/2023
 - Updated with new installations - 02/01/2023
 - First application creation - 28/12/2022
 - First django project version  - 28/12/2022

## Acknowledgments (code inspiration): 
- https://olivierlemoigne.com/posts/django-postgres/
- https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django?gclid=CjwKCAiAkrWdBhBkEiwAZ9cdcI07zMyqUJkmC1UZye-PofhFdt640FUvQji-5Fv3jWIQlqeSZOw8lhoCjsAQAvD_BwE
- https://www.youtube.com/watch?v=HEV1PWycOuQ
- https://www.enterprisedb.com/postgres-tutorials/how-create-postgresql-database-and-users-using-psql-and-pgadmin?gclid=CjwKCAiA-8SdBhBGEiwAWdgtcA0SaXwqY8RV_WGz-0D-XcimKinYOCH1NFITezF3lqhGpNiRb3MCnBoCGyIQAvD_BwE
- https://docs.netbox.dev/en/stable/installation/1-postgresql/
- https://pullanswer.com/questions/unable-to-create-the-django_migrations-table-during-installation
- https://www.django-rest-framework.org/api-guide/permissions/
- https://docs.netbox.dev/en/stable/installation/1-postgresql/
- https://stacklima.com/personnaliser-linterface-dadministration-de-django/
- https://stackoverflow.com/questions/26906630/django-rest-framework-authentication-credentials-were-not-provided
- https://python.doctor/page-django-orm-apprendre-base-donnees-database-queryset-modeles
- https://testdriven.io/blog/built-in-permission-classes-drf/
- https://www.django-rest-framework.org/api-guide/permissions/
- https://stackoverflow.com/questions/24884245/django-rest-framework-wont-let-me-have-more-than-one-permission
- https://learnbatta.com/blog/permissions-in-django-rest-framework-82/
- https://www.revsys.com/tidbits/tip-about-drf-permissions/
- https://github.com/encode/django-rest-framework/pull/5753
- https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
- https://dev.to/ericlecodeur/votre-premiere-introduction-a-django-rest-framework-j8k
- https://www.youtube.com/watch?v=unFGJhIvHU4
- https://supertype.ai/notes/django-rest-custom-permissions/
- https://stackoverflow.com/questions/41273034/implement-roles-in-django-rest-framework
- https://pypi.org/project/rest-framework-roles/
- https://pdipesh.medium.com/django-rest-framework-permissions-example-8ed9809c432d
- https://stackoverflow.com/questions/51048348/adding-a-user-to-a-group-using-django-rest-framework-programmatically