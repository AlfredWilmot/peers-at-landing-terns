import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from location.postcodes import PostCode


# list of weather-forecast websites
"""
https://www.bbc.co.uk/weather
https://www.metoffice.gov.uk/
https://www.accuweather.com/
"""

@dataclass
class Weather:
    temperature: float = None
    risk_of_rain: float = None
    location: str = None


def weatherforecast_bbc_weather(postcode: PostCode) -> Weather:
    """
    Weatherforecast from BBC weather.
    """

    outcode = postcode.split()[0].lower()
    url = f"https://www.bbc.co.uk/weather/{outcode}"
    soup = BeautifulSoup(requests.get(f"{url}").text, "html.parser")
    temperature_celcius = soup.find("div", {"class":"wr-time-slot-primary__temperature"}).text[0]

    return Weather(
        temperature = temperature_celcius,
        location    = postcode,
        )

def weatherforecast_metoffice():
    pass

def weatherforecast_accuweather():
    pass

if __name__ == "__main__":
    print(weatherforecast_bbc_weather(PostCode("S11 9AR")))
    print(weatherforecast_bbc_weather(PostCode("S6 2BD")))
