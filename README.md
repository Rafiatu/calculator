# Calculator Package

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development. The latest version of python.
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description


## Getting Started

Using this package is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `` to install the package.

Change directory into the project folder `cd devsprime-api` and build the base python image used for the project that was specified in ***dockerfile*** by running ` docker build . `

Spin up other services needed for the project that are specified in ***docker-compose.yml*** file by running the command `docker-compose up`. At this moment, your project should be up and running with a warning that *you have unapplied migrations*.

Open up another terminal and run this command `docker-compose exec api python project/manage.py makemigrations` for creating new migrations based on the models defined and also run `docker compose exec api python project/manage.py migrate` to apply migrations.

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/decadevs/devsprime-api.git
2. cd devsprime-api
3. docker build .
4. docker-compose up
5. docker-compose exec api python project/manage.py makemigrations
6. docker-compose exec api python project/manage.py migrate
```

## Running Tests

Currently, truthy tests has been provided in each of the application defined in the project, before running the tests with the following command make sure that your api service is up and running.

```docker
docker-compose exec api python project/manage.py test
```

## License

The MIT License - Copyright (c) 2020 - Rafihatu Bello

