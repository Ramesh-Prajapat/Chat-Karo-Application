
## Prerequisites

- [Django](https://www.djangoproject.com/)
- [MySQL](https://www.mysql.com/)

## Installation
- Create a virtual environment
    ```bash
     virtualenv -p python3 foldername
    ```
- Activate the virtual environment
    ```bash
    source bin/activate
    ```
- Install all the dependencies from `requirements.txt`
    ```python
    pip3 install -r requirments.txt
    ```
- Run the django server
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
- Hit the url `http://localhost:8000/`
