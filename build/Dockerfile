# Download base image ubuntu 20.04
FROM ubuntu:20.04

# Update
RUN apt-get update
# Intenta corregir las dependencias rotas
RUN apt-get install -f

# Configura la zona horaria
ENV TZ=America/Montevideo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Python 3
RUN apt-get install -y python3
RUN python3 --version
RUN apt-get update && apt-get install -y libpq-dev python-dev

RUN apt-get install -y python3-pip
RUN apt-get install -y wget

RUN apt-get update
RUN apt-get install -y --fix-missing postgresql postgresql-contrib

# Instalo librerias necesarias para el programa
RUN mkdir /build
COPY requirements.txt /build
RUN pip3 install -r /build/requirements.txt

# Zip
RUN apt install -y zip

# Chrome 114.0.5735.90-1
ENV CHROME_VERSION 114.0.5735.90-1
RUN wget --no-check-certificate https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN dpkg -i google-chrome-stable_${CHROME_VERSION}_amd64.deb || apt -y -f install
RUN apt-get install -f
RUN rm google-chrome-stable_${CHROME_VERSION}_amd64.deb

# Chrome-driver
ENV CHROME_DRIVER_VERSION 114.0.5735.90
RUN wget https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod +x chromedriver
RUN mv chromedriver /usr/local/bin
# Dependencias de chrome driver
RUN apt-get install -y libglib2.0-0  libnss3  libgconf-2-4  libfontconfig1

# Carpeta donde se va a compartir el código dentro del docker
RUN mkdir /code
