## About Project
This project is a basic clone of Twitter.

## How to Run/Setup

Follow the below steps to run the project on your local computer:

1. Open Command Prompt/Terminal.
2. Check if Python is installed on your system by typing `python --version` or `python3 --version`.
3. If Python is not installed, download it from [here](https://www.python.org/downloads/).
4. Check if PostgreSQL is installed. If not, download it from [here](https://www.postgresql.org/download/).
5. Clone the project repository by typing the following command in the terminal:
`git clone git@github.com:GaganDureja/twitter.git`
6. Navigate to the project directory. `cd twitter`
7. Create a virtual environment to manage project dependencies Install and Run:
```bash
sudo apt install python3-venv
python3 -m venv twitterEnv
```
8. Activate the virtual environment: `source twitterEnv/bin/activate`
9. Install the project requirements by running: `pip install -r requirements.txt`
10. Open pgAdmin either in the browser [pgAdmin](http://127.0.0.1/pgadmin4/) or using the application.
11. Register a server with the following details:
 - Name: localhost
 - Address: 127.0.0.1
 - Password: 123
 - Username: postgres
12. In the server, create a database named `twitter` using the same credentials as mentioned in `settings.py` file.
13. Once the database setup is complete, apply migrations by running:
`python3 manage.py migrate`
14. After all installations are done, start the server by running:
 `python3 manage.py runserver`
15. Access the application at [localhost](http://127.0.0.1:8000/).

## Admin Panel
1. To log in as an admin, you need a superuser account. Stop the server by `Ctrl+C`.
2. Create a superuser by running:` python3 manage.py createsuperuser`
3. Provide the required information (username, email, password) as prompted.
```bash
Username: admin
Email: admin@mail.com
Password: admin@123
Password (again): admin@123
```
4. You can use the above credentials for testing/development purpose but for production I recommend to use strong credentials.
5. Once the superuser is created, start the server again by running:
`python3 manage.py runserver`
6. Access the Django admin panel [here](http://127.0.0.1:8000/admin) and log in using the superuser credentials.
