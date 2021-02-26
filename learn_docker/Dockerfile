# Dockerfile, Image, Container
# Dockerfile is a blue print for building images
# Image is a template for running containers
# Container is actual running process where we have our process project

# FROM: baseimage
FROM python:3.8

ADD 1.py .

# Install depeendencies
# RUN pip install requests beautifulsoup4

# specify the entry the command, on where we start the container
CMD [ "python", "./1.py"]

# creation of image: docker build -t name_of_image specify_the_location
# docker build -t py_calculator .

# To start the docker container: docker run py_calculator

# If user input required
# docker run -t -i py_calculator
# -t will give pseudo terminal
# -i stands for interactive mode