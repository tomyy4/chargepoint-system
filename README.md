# chargepoint-system

To run the project:

- Create the .env file based on the env.template

If you are running docker, make sure to set the variables 
in the file docker.env
- run docker-compose up

To run the tests:
- python manage.py test --settings=main.test_settings