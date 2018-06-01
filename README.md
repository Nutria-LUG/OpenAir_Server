# OpenAir_Server

Django server and APIs for Openair surveys and errors registration.

## Prerequisites

Required packages:

- **python3**
- **python3-pip**

Optional packages:
- **git** _(to clone the repository)_
- **python3-venv** _(to install into a virtual env)_

## Setting up the virtual environment (optional)

In order to install the server into a virtual environment, to delete everything later, we use the following code:

```bash
# create the folder
python3 -m venv .venv
# activate the virtual environment
source .venv/bin/activate
```

## Get Started

First of all, we need to clone the repository, install dependencies, create the db (sqlite3) and then run the server. Optionally, we can add a super-user to access the Django admin site.

```bash
# clone the repository
git clone https://github.com/Nutria-LUG/OpenAir_Server openair-server
cd openair-server
# install dependencies
pip3 install -r requirements.txt
# create the db
python3 manage.py migrate
# add a super-user (optional)
python3 manage.py createsuperuser
# models registration
python3 manage.py makemigrations
python3 manage.py migrate
# run the server
python3 manage.py runserver
```

## Models

Following, models used for storing data from surveys and errors.

### Device
- **name** _(string)_: name
- **mac_address** _(string)_: MAC address
- **ip_address** _(string)_: static IP assigned to the device
- **enum** _(integer)_: enum to identify the device
- **active** _(boolean)_: if disabled, API will reject requests

### Sensor
- **name** _(string)_: name
- **code** _(string)_: hexadecimal sensor code
- **enum** _(integer)_: enum to identify the sensor
- **active** _(boolean)_: unused

### Survey
- **inserted** _(datetime)_: set by the server, it's the timestamp of the inserted row
- **timestamp** _(integer)_: timestamp of the survey (client detection)
- **device** _(Device)_: set by the server, it's filled using the client ip, obtained by the request
- **sensor** _(Sensor)_: set by the server, it's filled using the enum sent with the request
- **value** _(float)_: value of the survey

### Error
- **inserted** _(datetime)_: set by the server, it's the timestamp of the inserted row
- **timestamp** _(integer)_: timestamp of the error (client detection)
- **device** _(Device)_: set by the server, it's filled using the client ip, obtained by the request
- **message** _(string)_: error message

## APIs

Current project makes use of Django REST framework library.

### Surveys

The API method will refuse all requests sent by clients with IPs not defined into the Device table.

- **address**: /openair/api/survey
- **method**: POST
- **accept**: JSON
- **responses**: 201 _(created)_, 400 _(bad request)_
- **data**: object, array of objects
    - timestamp _(timestamp)_
    - sensor _(integer)_
    - value _(float)_

### Errors

The API method will refuse all requests sent by clients with IPs not defined into the Device table.

- **address**: /openair/api/error
- **method**: POST
- **accept**: JSON
- **responses**: 201 _(created)_, 400 _(bad request)_
- **data**: object, array of objects
    - timestamp _(timestamp)_
    - message _(string)_