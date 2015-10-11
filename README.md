# WeatherServer
Full Stack Embedded 2016 features a cheap weather station. This Django app 
serves the observed weather data in human and machine readable formats.

Please refer to ``LICENSE`` if you want to copy or use this software.

## Authors
The members of Full Stack Embedded 2016 are, in alphabetical order:

* Frederic Afadjigla
* Nico Caspari
* William Herndon
* Daniel Lee
* Gregor Schnee

This component was authored mainly by [Daniel Lee](erget2005@gmail.com) and 
[Gregor Schnee](schneegor@gmail.com).

## Setup
The following instructions detail how to install a minimal web server in a
development environment. If you are wanting to deploy the weather app in a
production environment, we suggest you read the [Django documentation for
deploying apps](https://docs.djangoproject.com/en/1.8/howto/deployment/).

For a quick minimal setup without worrying about the dependencies yourself,
run:

```
sudo ./configure
```

from the repository's root directory. Be warned, however, that this will
install all dependencies and install the app *systemwide* on your machine. If
you do this, you can skip all following steps in the tutorial.

### Dependencies
The following dependencies must be installed (e.g. with ``apt-get`` or
``zypper``:

* python3
* python3-pip (for installing Python dependencies)

Additionally, the following Python packages are required. Note that if you're
installing using ``setup.py`` you will not need to install anything manually
for running the app. Also, ``pandas`` is required to instal the random mock
data. This dependency will be removed along with the generation utility as soon
as real sample data has been integrated into the package.

* django
* pandas (only required for generating random sample data)

These packages can be installed without using ``setup.py`` e.g. with:

```
pip3 install $package
```

## Installation for deployment
It is suggested - but not necessary - to install the ``WeatherServer`` package
if you are wanting to deploy it in some kind of a web server.

If you haven't downloaded the sources you can use PyPI. Note: This is a planned
capability, the package won't be registered with PyPI until a release version
is available. Once the package has been registered, it can be installed as
follows:

```
pip install WeatherServer
```

If you have downloaded the sources you can install the package by navigating
into the package folder and using the following command:

```
python3 setup.py install
```

Remember to preface the commands with ``sudo`` if you wish to install the
package system wide.

## Setting up the project
Setup the app by initializing the database and setting up its tables. If you
don't configure ``weather_server/weather_server/settings.py`` this will
automatically use a SQLite database in the app's root folder.


```
me@host:~/WeatherServer/weather_server> # Setup database
me@host:~/WeatherServer/weather_server> python3 manage.py makemigrations
me@host:~/WeatherServer/weather_server> python3 manage.py migrate
me@host:~/WeatherServer/weather_server> # Setup super user - follow prompts
me@host:~/WeatherServer/weather_server> python3 manage.py createsuperuser
```

Now that the database is setup, you can start the development server as
follows:

```
me@host:~/WeatherServer/weather_server> python3 manage.py runserver
```

Now you can access the server by navigating e.g. to http://localhost:8000.

## Using test data
Test data is currently a hack because currently no actual data can enter the 
database - the weather station hardware does not exist yet. This section will
be removed in the future.

### Creating and importing test data
Test data can be created by executing
``show_weather/utils/create_mock_dataseries.py``. Note that this step requires
pandas.

```
me@host:~/WeatherServer/weather_server/show_weather/utils/> python3 create_mock_dataseries.py
```

This generates a randomized series of observations, stored as a CSV under
``weather_server/show_weather/utils/data_series.csv``. You can load this into
the database using
``weather_server/show_weather/utils/import_generated_series.py``. This is
slightly complicated because it uses Django's ORM, so it has to either be
started inside a Django shell, which takes care of all the bookkeeping legwork
for you (establishing DB connection, etc.) or you have to do Django's
administrative work for it. This example reduces the workload by using a Django
shell, but it's a bit esoteric for the same reason - the Django shell is
started, then the script is loaded as a string and executed inside that
environment. Don't worry, I washed my hands after writing it and it will soon
die.

``weather_server/show_weather/utils/import_generated_series.py`` creates an 
observing station and saves all of the observations as belonging to that 
station. It also expects the sample data series to be stored inside the 
``utils`` folder.

```
me@host:~/WeatherServer/weather_server> python3 manage.py shell
Python 3.4.1 (default, May 23 2014, 17:48:28) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> with open("show_weather/utils/import_generated_series.py") as script:
...     exec(script.read())
```

Lots of warnings follow because the ``datetime`` object used is timezone 
naive. Now your database is full of observations for my apartment, at the 
intersection of Constitution Hill, The Mall and Birdcage Walk.

### Examining test data
Now your development server is running. If you navigate to 
``localhost:8000/admin/`` you can login to the admin page and see the entries
in your database.

## API for viewing data
Currently, only CSVs are served as raw data. The following endpoints are 
supported:

* ``/data/csv/stations/`` - return a CSV of known station metadata
* ``/data/csv/$station_id/$start_date - $end_date`` - return a CSV of 
observations made at the station with ``$station_id`` between the dates 
(inclusively) specified. Dates are to be formated as ``YYYY-MM-DD HH:MM``.
