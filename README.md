# DjangoGooglePlaySearch
A search engine built on Django which can Search, Cache and Display results from Google Play Store. It caches search result (obtained by parsing from PlayStore) everytime onto database so that whenever same term is searched later, it will be retrieved directly from the database.

## Requirements
Python 3.5 or higher

## Features
* Provides list of top 10 results fetched from the Play Store

* Searching/ Parsing results from Google Play Store

* Caching of the search results everytime.

* App specific page providing details of the app.

## Setting up
1. Clone the repo.
```html
git clone https://github.com/SubhamBhattacharjee/DjangoGooglePlaySearch.git
```

2. Create a [virtualenv](https://virtualenv.pypa.io/en/stable/) with python 3.5 interpreter.
```html
mkvirtualenv <virtualenv_name> --python=<path_to_python3>
Example: mkvirtualenv googleplaysearch --python=/usr/local/bin/python3
```

3. Install the requirements.
```html
pip install -r requirements.txt
```

4. Perform migrations. (SQLite3 database is used by default).
```html
python manage.py migrate
```

5. Run the server.
```html
python manage.py runserver
```
Server will be live at http://127.0.0.1:8000
