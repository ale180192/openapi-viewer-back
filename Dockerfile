FROM python:3.6
RUN mkdir /code
RUN apt-get update
WORKDIR /code
COPY . /code/
COPY requirements.txt /code/

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", ":8000", "app.wsgi"]
   
# docker build --rm -t openapi-backend .
# docker run -d -p 8000:8000 --name openapi-backend openapi-backend
# docker exec -it ID-CONTAINER bash
# docker ps
# docker container stop 3426914376a2
# docker container rm 3426914376a2
# docker tag openapi-backend:latest alejandro180192/openapi-back:latest
# docker login
# docker push alejandro180192/openapi-back:latest