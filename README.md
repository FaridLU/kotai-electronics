# Welcome to Linkedin Crawler !

Follow the steps below:
 
 1. Install python3 and upgrade pip3

 2. Change directory to project folder

 3. Create `virtualenv` for this project, by following command:

		python3 -m venv venv
		
 4. Activate `venv` by following command:

		source venv/bin/activate


 5. Install all packages via pip3:
	
		 pip3 install -r requirements.txt

 6. Migrate the changes of Database:
	
		python3 manage.py migrate
		 
 7. Create superuser by following command:

		python3 manage.py createsuperuser

 8. Now run the django project by following command

		python3 manage.py runserver

 9. Open this url: `127.0.0.1:8000`

Now you are good to go.

*Developed by,*
***Farid Chowdhury***