## Running on your local Machine

```python
>>> virtualenv --python=python3.x venv
>>> . venv/bin/activate
>>> pip3 install -r requirements.txt
>>> python manage.py migrate
>>> python manage.py get_gyms #  to retrieve 1 page of gyms for testing
>>> python manage.py runserver_plus (using django extensions)
```
