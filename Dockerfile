# Verwenden Sie ein offizielles Python-Image als Basis
FROM python:3.12

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE  1
ENV PYTHONUNBUFFERED 1


# Setzen Sie den Arbeitsverzeichnispfad im Container
WORKDIR /DEV/  

# Kopieren Sie die Anforderungen in den Container und installieren Sie sie
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopieren Sie den Rest Ihrer Django-Anwendung in den Container
COPY . .

# Führen Sie migrations und sammelstatik-Kommandos aus
#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

# Definieren Sie den Port, auf dem Ihre Django-Anwendung lauschen soll
#EXPOSE 8000

# Starten Sie Ihre Django-Anwendung
#CMD [, "python", "manage.py", "runserver", "0.0.0.0:8000"]
