# Time Tracker Backend


## How to install this repository:

1. Clone this repository:
```
    git clone <GitHub repository link>
```

2. Create a virtual environment (in the project folder):
```
    python -m venv env
```

3. Install the dependencies:
```
    activate the virtual environment: env/Scripts/activate
    pip install -r requirements.txt
```

4. Set the environment variables:
```
    Create .env file and add the environment variables
```

5. Apply migrations:
```
    python manage.py makemigrations
    python manage.py migrate
```

6. Create a Superuser/ Admin:
```
    python manage.py createsuperuser
```

7. Start the local development server (on path: 127.0.0.1:8000):
```
    python manage.py runserver
```

8. Start time_tracker_frontend:<br/>
clone the repository and run the liveserver on path 127.0.0.1:4200
