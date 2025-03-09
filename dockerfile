
#Use an official Python runtime as a parent image
FROM python:3.7-slim
 
#set working directory into the container
WORKDIR /app

#Install required packages for system
RUN apt-get update \
&& apt-get upgrade \
&& apt-get install -y gcc \
&& apt-get clean
&& rm -rf /var/lib/apt/lists/*

#copy the requirements file into the container
COPY requirements.txt requirements.txt

#Install app dependencies
RUN pip install postgresql
RUN pip install --no-cache-dir -r requirements.txt

#Copy the application code
COPY ..

CMD["python", "app.py"]