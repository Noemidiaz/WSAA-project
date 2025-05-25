# Web Services and Applications

![Introimage](https://cdn.pixabay.com/photo/2023/01/03/08/12/bitcoin-7693848_1280.png)

## About this repository

 This respository contains my project for the module Web Services and Applications module at ATU.

It is a simple web aspp built using Flask. The app lets create, read , update and delete (CRUD) information which is stored in a database (MySQL)


 ## Project aims


- Create a database with at least one table to store's app data (using MySQL)

- Build a backend server (Flask) to handle request through a REST API routes

- Develop a frontend with basic HTML to interact with the data

- Interact with the app to perform CRUD operations (create, read, update and delete)

- Hosting/ deploy the app online so others can acces and test it (currently in progress)


 ## Tool used
 
In this project is used the following tools:

 #### Python & Flask
 Python is a programming language and Flask is web framework for Python that makes it easy to build web servers and APIs. Flask processes requests from the frontend or API clients.

 #### MySQL
 It is a database system that stores the app data in organized and clean tables.

 #### HTML
 It is the language used to build the structure of web pages. It is the interface where users interact with the app.

 #### PythonAnywhere: 
 Hosting platform where the app is upload and anyone can access it online. It is use for small and beginner Python projects.

## Key Flask Imports 

- **Flask**: Create the Flask application

- **render_template**: Flask function that loads and returns HTML page from templates of the folder of the app/project

-**request**: It allows access to data by users (via forms or API calls)

-**redirect**: Redirects users to another page actions. (Ex. after form submission)

-**url_for**: Generates URLs to routes within the app dynamically

-**flash**: pop up messages for the user (Ex. To indicate success or error notification). 



## How to run the App Locally

1. **Clone the repository:**

```python
git clone  https://github.com/YourUsername/YourRepo.git

```
2. **Install dependencies:**

```python
pip install -r requirements.txt
```

Inside requirements.txt are for example:
flask
mysql-connector-python

3. **Set up the database:**
- Download MySQL
- Create a schema and a table
- Private credentials in dbconfig.py file keep in .gitignore for safety reasons
create dbconfig.py with this format:

```python
host = 'your-database-host'
user = 'your-database-username'
password = 'your-database-password'
database = 'your-database-name'
```
4. **Run the  Flask app:**

 ```python
 python mental_health_app.py
```


 ## Get help
 
Below, you will find some references from official websites with tutorials videos, examples and theoretical explanation.These resources complement and expand upon the knowledge covered in these project.

 ## Contribute
You can submit a pull request regarding my code if you discover an error or if It should be updated.

 ## Author
 
 I am Noemi Diaz and I am currently studying Science in Computing in Data Analytics at ATU.


 ## References


- How to install MySQL : https://www.youtube.com/watch?v=BxdSUGBs0gM

- How to reset the root password MySQL: https://dev.mysql.com/doc/refman/8.4/en/resetting-permissions.html

- Flask tutorial beginners: https://www.youtube.com/watch?v=5aYpkLfkgRE&t=129s

- Flask URL Helper Function: https://www.geeksforgeeks.org/flask-url-helper-function-flask-url_for/

- Host application online. Python anywhere: https://www.pythonanywhere.com/
- Message Flashing: https://flask.palletsprojects.com/en/stable/patterns/flashing/

- HTML basic examples: https://www.w3schools.com/html/html_basic.asp

- HTML Introduccion: https://www.w3schools.com/html/html_intro.asp

- Templates: https://flask.palletsprojects.com/en/stable/tutorial/templates/

- Flask : https://tedboy.github.io/flask/tutorial/index.html

- request in Flask: https://www.geeksforgeeks.org/python-flask-request-object/

- Flask templates: https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html

***
End