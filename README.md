# Book Author project

## Python version: 3.11+

## Instructions to run the script

1. Goto the directory where you want to store your project.
2. Clone the git repository to the project directory.
3. Open the terminal and navigate to the project directory from the terminal.
4. Create virtual environment from the terminal by typing ```python -m venv venv``` and activate it by typing `source venv/bin/activate`(for Linux), `venv/Scripts/activate`(for Windows).

5. Install the project dependencies by typing `pip install -r requirements.txt` on the terminal.
6. Migrate the database by typing `python manage.py makemigrations` and then `python manage.py migrate` on the terminal.
7. Create admin user if you want by typing `python manage.py createsuperuser` and give the required credentials on the terminal.
8. Now, Run the project from your **localhost** by typing `python manage.py runserver`
9. Navigate to the URL [127.0.0.1:8000](127.0.0.1:8000) or [localhost:8000](localhost:8000) from your browser.
10. Please install **redis** if **redis** is not installed
11. Run celery worker and celery beat by running separately `celery -A mysite worker -l info` & `celery -A mysite beat -l info`
12. Third party library i used
* django-restframewrok to create API
* django-cors-headers for cross origin sharing
* djangorestframework-simplejwt for creating JWT token authentication
* Celery for Background Task
* Redis for caching
* drf-spectacular for api documentation
13. You can see the api doc by navigating to the URL `localhost:8000/api/schema/swagger-ui/` & `localhost:8000/api/schema/redoc/`

### URL's I've implemented:
* api/v1/register
* api/v1/token/
* api/v1/token/refresh/
* api/v1/books/
* api/v1/books/{book_id}
* api/v1/author/
* api/v1/author/{author_id}