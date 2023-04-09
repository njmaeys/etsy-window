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

## Running the server

```shell
$ # Run the local server
$
$ cd etsywind
$ python manage.py runserver
```

## Database commands

```shell
$ # Migrations
$
$ python manage.py makemigrations
$
$ python manage.py migrate <migration number>
```
