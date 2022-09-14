Steps for run the LibraryManagementSystem project--->


1. Clone the git repository on your machine.

2. Create virtual environment usign "virtualenv my_name" this command,please check the link if any error.
( https://www.geeksforgeeks.org/python-virtual-environment/)
Activate the virtual enviornment.

3. Install all dependancies using requirement.txt file.

3. Go to the LibraryMS folder using "cd" command in you terminal.( cd LibraryMS)

4. Run commands     a. python manage.py makemigrations.
		    b. python manage.py migrate.
		    c. python manage.py runserver
5. After last command run display localhost port like http://127.0.0.1:8000/

6. open chrome browser and enter http://127.0.0.1:8000/login (Entry point of application)

Registration--> http://127.0.0.1:8000/register/
	For register new admin in applications.

7.After registration go to "http://127.0.0.1:8000/login" and login.

8.After succesfully login open "http://127.0.0.1:8000/book" page and you perform all CRUD functionality.
