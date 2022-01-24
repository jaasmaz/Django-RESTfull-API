# Django-RESTfull-API

_Building APIs using Django framework_

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
1. Copy the path to the virtual env by running `pipenv —venv`
2. Append \bin\python to the path
3. ctrl + shift + p and enter interpreter path

### 4. Install mySQL Server

- Download it from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/) 
- Make sure to include mySQL in your OS environment variables 
- Run MySQL in your terminal to check if it's installed properly


### 5. Make Migration and migrate models to DB
```bash
python manage.py makemigrations && python manage.py migrate
```
>If using Mac or Linux Run `python3` instead of python only

### 6. Run The Server
```bash
python manage.py runserver
```
>If using Mac or Linux Run `python3` instead of python only

## Important Notes

- Import Seed Data From `Resources/Data/seed.sql`
- Run the scripts inside your local SQL Database (make sure to name the DB “storefront”)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author
[Jasim Alazzawi](https://www.linkedin.com/in/jazazzawi/)
