FROM python:3.7-buster
COPY testproject/ /src
WORKDIR /src
RUN pip install -r requirements.txt
RUN ./manage.py migrate
RUN ./manage.py check
EXPOSE 8000
