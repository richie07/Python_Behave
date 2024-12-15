# Project Behave - Python in Wordpress
Project for test concept of framework test on python with Behave over Wordpress with docker.

## Getting Started
These instrucions will get you a copy of the project up and running on your local machine for development and testing purposes.See deployment for notes on how to deploy the project on a live system.

### Prerequisites
For local execution you must have the following installed:
- Pycharm
- Docker Desktop

### Local installation Wordpress by Docker Compose
```
1. In the directory where your docker-compose.yml file is, run:
    $ docker compose up -d
2. Verify that the containers are running:
    $ docker ps
3. Open your browser and go to http://localhost:8080. You should see the WordPress installer    
4. When you no need enviroment docker, you can stop it
    $ docker compose down -v 
    
```
### Local installation Python Project:
```
1. First , Go to the folder where you want to install it
2. Create environment
    $ /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv venv_bdd_py3_s3
3. Seleccionar enviroment and activate the virtual environment
    $ source venv_bdd_py3_s3/bin/activate
4. Show ubication python3 in venv 
    $ which python3
5. Review installed plugins in python
    $ pip freeze
6. Install Behave and Selenium
    $ pip install selenium 
    $ pip install behave
7. Install in section Project interpretet on Pychart (Seleniun and Behave)

```

### Running tests in local
```
$ behave --tags=@Regression
```

### To view the reports
By Implement

## Built with
* [Python](https://www.python.org/) - Programming language
* [Behave](https://behave.readthedocs.io/en/latest/) - behave is behaviour-driven development, Python style
* [Docker](https://docs.docker.com) - Docker
* [PyCharm](https://www.jetbrains.com/pycharm-edu/) - Pycharm

## Versioning
We use [Github](https://github.com/) - for versioning.For the versions available, see the [tags on this repository](https://github.com/richie07/projectKarate)

## Author
* **Richard Francisco**

## Acknowledgments
* Hat tip to anyone who's code was used
* Inspiration
* etc