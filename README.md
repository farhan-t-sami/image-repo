# image-repo

Shopify's developer intern challenge - Image add and search functions

Check out the my demo: https://fts-imagerepo.herokuapp.com/

Or set it up in your own machine!

Setup instructions:

- Clone the repo

- Run python3 -m venv <name_of_virtualenv> (or equivalent)

- Install compatible dependencies from requirements.txt
-> asgiref==3.4.1
-> Django==3.2.7
-> django-environ==0.7.0
-> django-filter==2.4.0
-> gunicorn==20.1.0
-> Pillow==8.3.2
-> pytz==2021.1
-> sqlparse==0.4.2

- Go to the directory that has settings.py and run the following commands:
-> python3 manage.py makemigrations
-> python3 manage.py migrate (if there are migrations)
-> python3 manage.py runserver

- The app is ready for use! 
Go to localhost:8000 (or any other port preferred by your PC)
