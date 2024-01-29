# installation de python 3.12
FROM python:alpine3.19

# mkdir app & cd
WORKDIR /app
COPY requirements.txt .

# installation des dependances
RUN pip install -r ./requirements.txt

# copie tout le projet
COPY . .


# demarrer l'application
EXPOSE 8081
CMD ["python3","-m","uvicorn","main:app","--host","0.0.0.0","--reload","--port","8081"]