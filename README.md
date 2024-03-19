About Project -
This is a basic clone of Twitter.




How to Run/Setup -

Follow the below steps and test this on your local computer.

1. Open Command Promt/Terminal
2. Check if python is installed on your system by typing python --version / pyhton3 --version
3. If installed then skip this step or get it from here. https://www.python.org/downloads/
4. Check if postgresql is installed if not then download from https://www.postgresql.org/download/ and also install pgadmin
5. Now all set go to project directory in Terminal and make a virtual environment so the package is installed as used in this project. Type python3 -m virtualenv myenv (here myenv is a random name you can type whatever you want).
6. Now activate the virtual env as per your name type - source myenv/bin/activate
7. Then install the project requirement with command  pip install -r requirements.txt
8. Open pgadmin. You can open it in browser http://127.0.0.1/pgadmin4/ or the application.
9. Now register a server ( name - localhost, address- 127.0.0.1, password -123, username - postgres ) and then in server name create a database name twitter1 (use the same credentials in settings.py file)
10. After the above is done then type python3 manage.py migrate
11. After all installations are done. Run command python3 manage.py runserver
12. Now you can check your localhost http://127.0.0.1:8000/


Addtion-
1. If you want to check django admin panel you can just type admin after the above link and that will require a credential to login. To create one you need to stop the server by pressing ctrl and C simultaniously. then type python3 manage.py createsuperuser
2. It will ask some basic input and after thats done you can start the server again by python3 manage.py runserver

