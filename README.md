# chargepoint-system

To run the project:

- Create the .env file based on the env.template
- Go to src/ and run the command python manage.py runserver
- Go to /api/

If you are running docker, make sure to set the variables 
in the file docker.env
- run docker-compose up

Go to /api/

To run the tests:
- python manage.py test --settings=main.test_settings