## Url Shorten

## Features:
- Make a short url valid for 2 days. 

1. Create virtual environment to install dependencies.

```shell script
$ virtualenv venv -p python3
``` 

2. Activate virtual environment.

```shell script
$ source venv/bin/activate
```

3. Install all the dependencies using below command.

```shell script
(venv)$ pip install -r requirements.txt
```

4. Setup PostgreSQL
    - Install the postgresql database in your local computer from the official [site link](https://www.postgresql.org/download/).

5. Create a new database using the postgresql command line

```shell script
$ CREATE DATABASE abc
```

8. Change username and password for database in .env file according to your postgres configuration.
    - e.g  If your postgres username is 'ABC' and password is 'XYZ', then update .env file as
```
      DB_NAME=abc
      DB_USER=ABC
      DB_PASSWORD=XYZ
      DB_HOST=localhost
      DB_PORT=5432
```

8. Add other required setting in .env as following

```
      URL_SIZE=4 (short url size)
      LINK_VALID=5 (Number of days)
```


10. After creating database apply migrations using below command

```shell script
(venv)$ python manage.py migrate
```

11. Run project on server using below command:
```shell script
(venv)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.


12. Create Short url from following api endpoint.

`http://127.0.0.1:8000/api/short-n-url/create/`

