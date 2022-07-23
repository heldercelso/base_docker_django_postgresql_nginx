# command to build:
# - docker build .\web_project\ -t heldercelso/my_repo:django_app
# or use the docker-compose.yml with the build parameter
FROM python:3.7.6-alpine

# some features needed to install requirements.txt on the alpine linux:
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev bash

# defining the working directory which will receive the web_project files
WORKDIR /code

# creating virtual environment and adding to path
ENV VIRTUAL_ENV=/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# check if necessary for production version
#EXPOSE 8000

# avoid pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# python output is sent straight to terminal (container log) without being buffered
# so the output of the application (django logs) can be seen in real time.
ENV PYTHONUNBUFFERED 1

# copy the whole django project into /code and installing the requirements
COPY . .
RUN pip install -r requirements.txt
#RUN mkdir templates
#RUN echo "yes" | python /code/manage.py collectstatic