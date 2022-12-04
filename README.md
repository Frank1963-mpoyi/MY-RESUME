# Mpoyi Resume app

Mpoyi Resume app, API & Frontend technology for mobile App. 

Please follow the following steps to set up and run the project on your local environment.


Steps:

1. Clone the repository onto your local environment.

2. Create a virtual environment (using virtualenv or pipenv).
	- pip install virtualenv or 
	- pip install pipenv

3. Install the requirements located in requirements.txt in requirements directory.

4. Create a postgres database in your local environment or Database server.
	- name : hospital_dev
	- user : hptl_user
	- password : hPTl@ppUS3R!

(Could be restored from the existing copy if needs be - Ask Mpoyi Tshibuyi).

5. Request .env file from Mpoyi Tshibuyi which contains remaining sensitive settings' info.

6. Create a directory named .env  in the root project's directory. 
   
7. Then run "python manage.py runserver localhost:8000 --settings=config.settings.dev".
