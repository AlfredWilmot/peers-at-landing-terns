# How's the weather up there?

In this example, we're using the factory pattern to create a collection of
classes that each pull weather-forecast data from a particular website.

## Setting up `.venv`
Initial setup of hidden local venv (based on this [article](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)).
In this example, I have python 3.10 installed on my hostmachine.

Run the following command from a terminal in the same directory as this README:
> `virtualenv --python="/usr/bin/python3.10" ".venv"`

Activate the virtual environment you just set-up:
> `source .venv/bin/activate`

Install the required packages (while ensuring the venv is active!):
> `pip install -r requirements.txt`

Once you're done, you can either deactivate the venv, or simply close the
terminal session where it's active:
> `deactivate`


## A/C
- Specify the area (what modalities could we accept here? postcode, coordinates, city, country, etc)
    - allow for different types of input areas (perhaps this could be addressed by the builder pattern?)
- The main function should go through each website from a database, and return
an estimate of weather conditions based on this data.
- output format should be independent of the website from where the weather forecast information is derived from.

## ToDo
- create a list of websites to query for the weather
- specify a dataclass for the common output format
    - start small (e.g. temp, risk of rain), make it scalable for more data (e.g. wind direction and strength)
- create tests to reflect the general behaviour you're expecting to see from the system. 
(try property-based testing) 
- write some basic web-scraping code for pulling data from web-pages, use beautiful soup to parse.
