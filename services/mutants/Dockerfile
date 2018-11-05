FROM python:3.6.4

# set working directory
RUN mkdir -p /src/
WORKDIR /src

# add requirements
COPY ./requirements.txt /src/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /src

# run container entrypoint
RUN ["chmod", "+x", "./docker-entrypoint.sh"]
CMD ["./docker-entrypoint.sh"]
