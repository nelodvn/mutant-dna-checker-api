# Ultimate Mutant DNA Checker API

This is the ultime mutant DNA checker API, built for Magneto to rule the world.

## Requirements

- Docker (https://docs.docker.com/get-started/)
- docker-compose (https://docs.docker.com/compose/install/)
- Linux (not tested on windows, please see https://docs.docker.com/docker-for-windows/install/. Apprecieate feedbacks about windows compatibility.)

## Getting Started

### building the project

First, pull the necessary images and build the project with docker:

> $ docker-compose pull ;  docker-compose build

### testing and test coverage
To check the project health, we can now run the tests with:

> $ docker-compose run mutants python manage.py test

Also, we can check the test coverage with Coverage.py (please check https://coverage.readthedocs.io/en/v4.5.x/ for mor details about Coverage.py)

> $ docker-compose run mutants python manage.py cov

The coverage should be printed on the terminal session. It could be viewed in HTML format by checking the file (./services/mutants/htmlcov/index.html)

### getting up and running

To get the api up and running locally, we can use docker-compose:

> $ docker-compose up

If everything works as expected, you should open the documentation at http://localhost:8080.

Available endpoints are:
- GET http://localhost:8080
- POST http://localhost/mutant
- GET http://localhost/stats

### live test

The app is running live @ http://159.65.36.164/ :)
Check swagger specs: http://159.65.36.164:8080
Mutant check url: http://159.65.36.164/mutant
Stats url: http://159.65.36.164/stats
