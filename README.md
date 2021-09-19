# image-repo

### Shopify's developer intern challenge - Image add and filter functions

Upload images and filter uploaded images according to their types

### Check out my demo: https://fts-imagerepo.herokuapp.com/

Or set it up in your own machine!

### Setup instructions:

- Clone the repo

- Set up virtual environment using:
``` 
python3 -m venv <name_of_virtualenv>
```
- Cd to the directory where requirements.txt is located
- Activate your virtualenv and run the following command in your shell
```
pip install -r requirements.txt
```
- Dependencies from requirements.txt
  - asgiref==3.4.1
  - Django==3.2.7
  - django-environ==0.7.0
  - django-filter==2.4.0
  - gunicorn==20.1.0
  - Pillow==8.3.2
  - pytz==2021.1
  - sqlparse==0.4.2

- Go to the directory that has manage.py and run the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
- The app is ready for use! 
Open your browser and go to localhost:8000 (or any other port preferred by your PC)
