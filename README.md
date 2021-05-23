# advisornetwork
FIrst u have to install python to run this project 
then install requirements.txt 
pip install requirements.txt
configure your database setup in settings.py

    'ENGINE': 'django.db.backends.x',
    where x be mysql ,postgresql,sqlite
    
        'NAME': 'advisordb',
        
        'HOST': 'localhost',
        username of the database
        'USER': '',
        password of database

        'PASSWORD': '',
        
   then run the following commands
  python manage.py makemigrations
  python manage.py migrate
    
