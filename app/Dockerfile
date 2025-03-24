# For more information, please refer to https://aka.ms/vscode-docker-python
# Usé bookworm porque  ni alpine ni slim instalaban la lib. mariadb, 
# le faltaban cosas: MariaDB Connector/C
FROM python:3.12.9-bookworm

# Puerto que usará la web
EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# # Install required MariaDB Connector/C
# WORKDIR /app/dwnl
# COPY . /app/dwnl

# COPY mdb_connector_c.sh .
# RUN chmod 755 ./mdb_connector_c.sh
# RUN ./mdb_connector_c.sh

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Cambiar el directorio de trabajo y copiarlo todo
WORKDIR /app
COPY *.py /app
COPY ./static /app/static
COPY ./templates /app/templates

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app && chmod u+x *.py
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "vsearchweb:app"]
CMD ["python", "vsearchweb.py"]
