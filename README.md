## Getting started

Steps:

1. First and Foremost Clone/pull/download this repository.
2. Install Virtualenv by `pip install virtualenv`
3. Create a virtualenv with `virtualenv env` and install dependencies with `pip install -r requirements.txt`
4. Activate virtual environment by `source pathofvenv/scripts/activate` for linux
5. Then run `python manage.py makemigrations`
6. after that run `python manage.py migrate`
7. Last but not least run the server by `python manage.py runserver`

This project includes:

1. Settings modules for deploying with Azure
2. Django commands for renaming your project and creating a superuser
3. A cli tool for setting environment variables for deployment
