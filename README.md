# Housing
Off-Campus Housing for SSU International Students

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* Python
* Django

### Installing

```
$ cd housing
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver

open the website(chrome best) and input
http://127.0.0.1:8000/
```

## Running the tests


```
python manage.py test
```

