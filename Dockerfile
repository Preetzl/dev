# Verwenden Sie ein offizielles Python-Image als Basis
FROM python:3.12

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE  1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc bash iputils-ping curl gawk \
    && pip install psycopg2



# Setzen Sie den Arbeitsverzeichnispfad im Container
WORKDIR /app/  
# Kopieren Sie die Anforderungen in den Container und installieren Sie sie
COPY . /app/
RUN python -m pip install -r requirements.txt

# Kopieren Sie den Rest Ihrer Django-Anwendung in den Container 


# Führen Sie migrations und sammelstatik-Kommandos aus
#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

# Definieren Sie den Port, auf dem Ihre Django-Anwendung lauschen soll
EXPOSE 8000

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


# Starten Sie Ihre Django-Anwendung
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
