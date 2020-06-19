# elite2020-creative-webd

## Steps

- Clone; `$ cd website/`
- Install missing packages through trial-error
- `$ python manage.py makemigrations accounts`
- `$ python manage.py makemigrations jobs`
- `$ python manage.py makemigrations app_profile`
- `$ python manage.py migrate`
- `$ python manage.py createsuperuser`
- `$ python populate_db.py`
- `$ python manage.py runserver`
- Checkout Website
- Go to `website_url` + **/admin**
- Login with sudo credentials prev. created