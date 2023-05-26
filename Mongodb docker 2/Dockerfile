FROM python:3.10

# RUN mkdir -p /usr/src

WORKDIR /app

COPY  ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 3000

# CMD ["ls", "-la"]
CMD ["python", "src/testmongopy.py"]

#docker build -t testdockerpy . command to create the image
#docker stop $(docker ps -a -q) stop container
#docker rm $(docker ps -a -q) delete stoped containers
#docker rmi  delete image
#docker run -p 4000:3000 testdockerpy  run container

