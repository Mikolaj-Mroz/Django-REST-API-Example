# REST API Example

## Table of Contents

 * [Introduction](#introduction)
 * [Technologies](#technologies)
 * [Setup](#setup)
 * [How to use](#how-to-use)

## Introduction
This is an example of REST API made using Django and Django REST Framework

## Technologies

Project has been created using:

 * Django version: 4.1
 * DjangoRestFramework version: 3.13.1

# Setup

To run this project first create virtual env.

```
$ python -m venv .venv
```

Next activate that venv.

```
$ source .venv/scripts/activate
```

Next install requirements.

```
(.venv)$ pip install -r 'requirements.txt'
```

Then open django_rest_api_project folder.

```
(.venv)$ cd django_rest_api_project
```

Lastly run server.

```
(.venv)$ python manage.py runserver
```

## How to use

### Pin Boards

Go to the http://localhost:5000/pinboards

### Notes

Go to the http://localhost:5000/notes
