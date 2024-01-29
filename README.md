# API Hotel Studi

Projet effectué dans le cadre d'une série de live Studi, durée de 4 heures dans lesquels nous avons abordés : 
- les models ainsi que les ORMs (SQLAclchemy)
- les endpoints ainsi que les controllers incluant la logique métier
- la sécurité via un token JWT
- deploiement applicatif

# pré-requis

- [IDE Python](https://www.jetbrains.com/fr-fr/pycharm/) 
- [Python 3.11 or eather](https://www.python.org/downloads/)

# Installation

- git clone this project
- install dependencies with this command in root folder of the project :
```python
pip3 install -r ./requirements.txt
```

- create env file named '.env' in the root of the project
  - set value of SECRET_KEY , ALGORITHM and ACCESS_TOKEN_EXPIRE_MINUTES
- launch app with :
```python
python3 -m uvicorn main:app --reload
```

- go to http://127.0.0.1:8000/api/ and enjoy !
