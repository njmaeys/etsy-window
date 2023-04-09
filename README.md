# Etsy Window

Solution for creators that want to list their Etsy shop offerings in their website to preserve their personal look and feel. It's window shopping but for your Etsy store. Users will still purchase from your Etsy store while you keep them enaged on your personalized website.

---
## Setup

This app is ran using Django. Set up the virtual environment, install the requirements, then spin up the local server.

```shell
$ # Virtualenv setup
$
$ virtualenv -m venv .venv
$
$ # Mac/Nix
$ source .venv/bin/activate
$
$ # Windows
$ source .venv/Scripts/activate
```

```shell
$ # Install deps (highly suggest you use the virtualenv)
$
$ pip install -r requirements.txt
```

## Running the server

```shell
$ # Run the local server
$
$ cd etsywindow
$ python manage.py runserver
```

## Tests

Tests are defined in the `tests` dir of the `web` application. The `manage.py` is able to run tests.

```shell
$ # Run tests
$
$ python manage.py test web.tests
$
$ # Run a single test class
$
$ python manage.py test web.tests.test_index.IndexViewTest
```

## Database commands

```shell
$ # Migrations
$
$ python manage.py makemigrations
$
$ python manage.py migrate <migration number>
```
