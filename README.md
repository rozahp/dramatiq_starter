# Dramatiq Starter Barebone App

Simple dramatiq starter app with Redis as broker, Flask web framework and with a docker-compose file for easy testing.

The Flask app runs a watcher (built on the watchdog library) that submitts filenames to a tasks. There is also the dramatiq_dashbord running under Flask. The workers are started by the simple dramatiq command: dramatiq application.tasks. 

The full stack includes following docker instances:

1. redis:latest
2. nginx:latest     - built with file: dockerfiles/Dockerfile.nginx
3. dramatiq_worker  - built with file: dockerfiles/Dockerfile.worker
4. dramatiq_web     - built with file: dockerfiles/Dockerfile.web
5. prometheus 
6. grafana (optional)

You could also run a mini-version: flask-tasks, dramatiq-workers and redis. See below under installation. 

Nginx acts as proxy for the following internal docker services:

dramatiq_web:

- http://localhost:8080/esperanto/dashboard/   - for dramatiq_dashboard
- http://localhost:8080/esperanto/api/         - for flask main api

prometheus:

- http://localhost:8080/esperanto/prometheus/  - for prometheus dashboard

This program should work on any Linux system with Python 3.x.

## AUTHOR OF THIS COMPILATION 

Phazor / Cascade 1733 

## INSPIRATION

Got inspiration from other coders on Github.

## LICENSE

Please feel free to copy, distribute and change this program in any way you like.

## INSTALLATION 

Method used is docker-compose, you could use Python virtualenv for testing just the flask app and dramatiq workers. Note that the application starts in debug mode. See configuartion for how to change that. 

### 1. Docker

#### Terminal 1

    docker-compose -f docker-compose.yml build
    docker-compose -f docker-compose.yml up        

running the mini version:

    docker-compose -f docker-compose-mini.yml build
    docker-compose -f docker-compose-mini.yml up        

Note: the dramatiq dashbord is now found on: http://localhost:5000/dashboard/

running with grafana:

    docker-compose -f docker-compose-grafana.yml build
    docker-compose -f docker-compose-grafana.yml up        

Note: the grafana dashbord is found on: http://localhost:3000/
You have to add prometheus as datasource and hit manage to activate dramatiq dashboard. 

#### Terminal 2

    touch /tmp/testfile.csv

### 2. Python Virtual Env

Note: for this to work you have to install redis first.

#### Terminal 1

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements
    cd dramatiq_flask
    ./start-web.sh

#### Terminal 2

    source venv/bin/activate
    cd dramatiq_flask
    ./start-worker.sh

#### Terminal 3

    touch /tmp/testfile.csv

## CONFIGURATION

### 1. To change from DEBUG to NORMAL mode edit following file:

    dramatiq_flask/application/__init__.py

and line:

    app.config.from_object('config.DevConfig')
    
change to:

    app.config.from_object('config.ProdConfig')

### 2. To change which path the watcher looks in for files:

#### Running from virtualenv

export WATCHER_PATH=/what/ever/path

#### Running docker

Note: the path has the be reached by both dramatiq_web and dramatiq_worker.

    docker-compose.yml:

and lines:

    volumes:
      - /tmp:/work

change to (for both dramatiq_worker and dramatiq_web):

    volumes:
      - /what/ever/you/would/like:/work

or lines:

    environment:
      ...
      WATCHER_PATH: /work

change to (for both dramatiq_worker and dramatiq_web):

    environment:
      ...
      WATCHER_PATH: /what/ever/you/would/like 

### 3. Proxy settings

edit following files:

  - nginx/nginx.conf
  - docker-compose.yml --> DASHBOARD_PREFIX ... (dramatiq_web)
  - docker-compose.yml --> --web.external-url ... (prometheus)


## LOGFILES

No system logfiles are configured or created.

## TODO

* apscheduler instead of watchdog?

