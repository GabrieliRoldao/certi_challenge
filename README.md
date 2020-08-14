# Numbers to word API

API that receive as input a number and than returns into the extensive form.

#### Requirements

This project runs on `Python 3.8`.

#### Run project

To run the project at console, run:

    $ python run.py
    
To run the project as a docker container, run:

    $ docker-compose up
    
#### REST API

Insert a number and return the number in the extensive form:

**Request**

`GET /<number>`

    curl http://localhost:5000/100

**Response**
    
`Code: 200`

    {
        "extenso": "cem"
    }

In case of errors the return will appear a message like this:

`Code: 500`

    {
        "error": "The input number 4dd it's not valid. Insert only numbers!!!"
    }

#### Run unit tests

To run all the unit tests, execute:

    $ python -m unittest discover -s tests/
