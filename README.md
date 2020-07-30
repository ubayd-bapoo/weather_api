# Weather API Project
## Overview
Steps to run weather system that will determine the weather for given city and period of time. 
 The data returned will be the min, max, average and median temperature and humidity.

The system is built using Python 3.7.4 with a Django framework and the Django Rest 
Framework package for the API aspect.

We are also using Django's built in file system caching to save the 
cities GPS co-ordinates.

API endpoint looks like this:
```bash
/apis/v1/weather?city=Cape+Town&period=2020-07-01%2C2020-07-08
```

```bash
city - String with City name  
period - String with from date first then to date separated by a ','  
the date formats needs to be "YYYY-MM-DD"
```

API JSON returned in a format such as this:
```bash
{
	'2020-06-28': {
		'humidity': 0.76, 
		'min': 60.18, 
		'max': 73.64, 
		'average': 73.14, 
		'median': 60.67
	}, 
	'2020-06-29': {
		'humidity': 0.92, 
		'min': 65.16, 
		'max': 72.24, 
		'average': 71.92, 
		'median': 65.68
	}
}
```

* Weather info is collected from [Darksky API](https://darksky.net/) 
we on allowed 1000 free requests per day.
* Geocoding info collected from [Neutrino API](https://www.neutrinoapi.com/)
we only allowed 25 free daily requests so we cache the results of the Geocoding.

## Installation
### Initial Installation
Install Python 3.7 and follow commands. Allow Python to be added to 
the PATH.

Once Python is installed. Install virtualenv via pip so that all 
dependencies are stored inside the virtual enviroment. Open the 
command line and run the following.

```bash
pip install virtualenv
```

Create virtual enviroment using the following command:
```bash
virtualenv venv
```

Activate the virtual enviroment. On Windows use the following.
```bash
venv\Scripts\activate.bat
```

Install the required packages, using pip and the requirements file.
```bash
pip install -r requirements.txt
```

## Setup
Run the django migrate
```bash
python manage.py migrate
```

Create a super user to access the admin interface, follow the promtes.
```bash
python manage.py createsuperuser
```

## Testing
Run the Django built in testing using the following command:
```bash
python manage.py test
```

If tests passed with no errors you can run the system.

Instructions on how to run application in the Activate section.

## Adding User to System
Once the system is running you can create a user by using the 
Admin Backend:

NB: There is no signup form for this system.

### Admin Backend
Once you have created a super user you can create a user by going to
the admin backend.
```bash
{{ IP Address/URL }}/admin
```
Use the super user account details, as created above in the setup 
section, to login.

Once logged in you'll be redirected to the admin backend. Click on the
"Users" link. You'll be redirected to the frontend for the "Users" table.

On the top right click on the "Add User".

Fill in all the details and click "Save".

## Activate Application without Docker
Run the server and start using the application.
```bash
python manage.py runserver
```

## Activate Application with Docker
Open Docker and navigate to the application via the Docker terminal.
Once at the application run the following commands:
```bash
docker-compose up -d --build
```

Once everything is done, run the next command:
```bash
docker-compose up
```

Once the web service is running you can use the system on the 
following URL:
[http://192.168.99.100:8000/](http://192.168.99.100:8000/)

To stop Docker once is running press CNTRL + C. Once the web service has stopped.
Run the following command:
```bash
docker-compose down
```