# Django-RESTfull-API

Building APIs using Django framework

## Setup

### 1. Install Django inside Virtual environment

```bash
pipenv install django
```

### 2. Activate the Virtual env

```bash
pipenv shell
```

### 3. Select python interpreter in vscode
Copy the path to the virtual env by running 

```bash
pipenv —venv
```
Append \bin\python to the path

ctrl + shift + p and enter interpreter path

### 4. Install mySQL Server

Download it from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/) 

Make sure to include mySQL in your OS environment variables 

Run MySQL in your terminal to check if it's installed properly


### 5. Make Migration and migrate models to DB
```bash
python manage.py makemigrations && python manage.py migrate
```

### 5. Import Seed Data
From Resources/Data/seed.sql

Run the scripts inside your local SQL Database (make sure to name the DB “storefront”)




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author
[Jasim Alazzawi](https://www.innovatortechs.com/)
