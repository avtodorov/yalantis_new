# Setup instructions

1. Instal virtual env
```
python3.9 -m venv venv
```

2. Activate virtual env

```
source env/bin/acivate
```

3. Install deps

```
pip3 install -r requirements.txt
```

4. Migrate database

```
python3 manage.py migrate
```

5. Create super user

```
python3 manage.py createsuperuser
```
6. Add some models

```
http://localhost:8000/admin/
```

7. Run server

```
python3 manage.py runserver
```


Links

[check](http://localhost:8000/check/)