# fastapi-test
Building a user registration API

## Context

Building a user registration API :
User is able to :
- Create an account
- Receeive code OTP by email to verify the account.
- Login into account


## Specifications
You have to manage a user registration and his activation.

## Architecture schema
![Architecture schema](images/architecture_scema.png)

Global Architecture : 

```
.
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── api
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── auth
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schemas.py
│   ├── otps
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schemas.py
│   ├── exceptions
│   │   └── business.py
│   └── utils
│       ├── constantUtil.py
│       ├── cryptoUtil.py
│       ├── dateUtil.py
│       ├── dbUtil.py
│       ├── emailUtil.py
│       ├── jwtUtil.py
│       └── otpUtil.py
├── mvenv
├── images
│   └── architecture_scema.png
├── tree.txt
└── README.md
```

Containerize application :

```
├── docker-compose.yml
├── Dockerfile
```

In this Application, we have created 2 services:

1. Database Service (db)
* It is a docker image of postgres (postgres:13-alpine). 
* This layer is responsible for all database operations.
* Any user don't have direct access to this layer.

2. Backend/Python API Service (api)
* It uses docker image of fastapi-test.
* This layer interacts with the database.
* This layer is also responsible for creating various API routes for interacting with the database service.

**requirements.txt** : All the dependencies needed to install

API Structure 
```
├── api
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── auth
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schemas.py
│   ├── otps
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schemas.py
│   ├── exceptions
│   │   └── business.py
│   └── utils
│       ├── constantUtil.py
│       ├── cryptoUtil.py
│       ├── dateUtil.py
│       ├── dbUtil.py
│       ├── emailUtil.py
│       ├── jwtUtil.py
│       └── otpUtil.py
```

1. Config API :

```
├── api
│   ├── config.py
│   ├── main.py
│   ├── models.py
```
* **config.py** file will have the configurations and Environment Variables necessary for the project to be validated with Pydantic
* **main.py** file is the root level file of our project from where the project will run
* **models.py** file will contain the models needed for database

2. Routers API :

Folder will contain all the apps which are going to be used in our project, each app file will contain all the APIs needed for that app

Our API contains 2 routers `auth` (for registraion user) and `otps` (for generating code otp):
```
│   ├── auth
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schemas.py
│   ├── otps
│   │   ├── crud.py
│   │   ├── router.py
│   │   └── schemas.py
```

Every Router Contains : 

* **crud.py** : file will contain the database queries for evrey request
* **router.py** : file will have the specific requests
* **schemas.py** : file will have the schema pydantic schema for the requests

```
│   ├── exceptions
│   │   └── business.py
│   └── utils
│       ├── constantUtil.py
│       ├── cryptoUtil.py
│       ├── dateUtil.py
│       ├── dbUtil.py
│       ├── emailUtil.py
│       ├── jwtUtil.py
│       └── otpUtil.py
```
* **exceptions** : Folder for Handle exceptions
* **utils** : Folder for some utilities

## Settings For Sending Emails

1. Add your own Credentials in `api/.env` : 

```
# Email Configuration:
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_TLS=True
MAIL_SSL=False
USE_CREDENTIALS=True
```

## Lunch & Test App

For Test : 

```
docker-compose up --build
```
For Prod : 
```
docker-compose up -d
```

## Licence

* Copyright (c) 2022 Tayssir Boubaker

## Thanks