# Dockerfile, Image, Container
# Dockerfile is a blue print for building images
# Image is a template for running containers
# Container is actual running process where we have our process project

# FROM: baseimage
FROM python:3.8

ADD 2.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./2.py"]

# in command prompt, we have add -p which stands for port number and then type 8000
# docker run -p 5000:5000 pythonfastpi
# http://127.0.0.1:5000/