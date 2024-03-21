## About Project -
This is a basic clone of Twitter.




## How to Run/Setup -

Follow the below steps and test this on your local computer.

1. Open Command Promt/Terminal
2. Check if python is installed on your system by typing `python --version` / `pyhton3 --version`
3. If installed then skip this step or get it from here. [Download Python](https://www.python.org/downloads/)
4. Check if postgresql is installed if not then download from [Download postgresql](https://www.postgresql.org/download/)
5. Open terinal and type `git clone git@github.com:GaganDureja/twitter.git` and after download is finished type `cd twitter`.
6. Now all set you're in the project directory, make a virtual environment so the package is installed as used in this project. Type `python3 -m virtualenv twitterEnv` (here twitterEnv is our virtua environment name).
7. Now activate the virtual env type - `source twitterEnv/bin/activate`
8. Then install the project requirement with command  `pip install -r requirements.txt`
9. Open pgadmin. You can open it in browser [pgadmin](http://127.0.0.1/pgadmin4/) or the application.
10. Now register a server ( name - localhost, address- 127.0.0.1, password -123, username - postgres ) and then in server name create a database name twitter (use the same credentials in settings.py file)
11. After the above is done then type `python3 manage.py migrate`
12. After all installations are done. Run command `python3 manage.py runserver`
13. Now you can check your [localhost](http://127.0.0.1:8000/)


## Admin Panel Access-
1. If you want to check django admin panel you can just type admin after the above link [click here](http://127.0.0.1:8000/admin) and that will require a credential to login. To create one you need to stop the server by pressing ctrl and C simultaniously. then type `python3 manage.py createsuperuser`
2. It will ask some basic input and after thats done you can start the server again by `python3 manage.py runserver`