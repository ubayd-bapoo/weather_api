import requests

from datetime import datetime, timedelta

from django.conf import settings
from django.core.cache import cache

# ------------------------------------------------------------------------------
class Controller(object):
    def __init__(self, city, period):
        self._city = city.title()
        self._period = period.split(',')

    def weather_info(self,):
        """
        Builindg a dict of the correct format for the data
        """
        city_gps = self._get_gps()
        start_date = datetime.strptime(self._period[0], '%Y-%m-%d')
        end_date = datetime.strptime(self._period[1], '%Y-%m-%d')

        locations_data = {}
        for single_date in self._daterange(start_date, end_date):  # Looping through all the days
            string_date = single_date.strftime("%Y-%m-%d")
            locations_data.setdefault(string_date, self._location_data(city_gps, string_date))

        return locations_data

    def _get_gps(self):
        cached_city = cache.get(self._city)

        #  There is a limit on the amount of requests we can make per day. The cities GPS does not change there we can
        #  cache the results saying us time and requests being made.
        if cached_city is None:
            #  If city has not been cached will do so after making the request.
            response = requests.get(
                '%s' % settings.GEOCODING_API_URL,
                params={'user-id': settings.GEOCODING_API_ID,
                        'api-key': settings.GEOCODING_API_KEY,
                        'city': self._city,
                        },
            )
            cache.set(self._city, response)
        else:
            response = cached_city

        return [str(response.json()['locations'][0]['latitude']), str(response.json()['locations'][0]['longitude'])]

    def _location_data(self, location_gps, date):
        """
        Making request to Dark Sky
        """
        date_format = datetime.strptime(date, '%Y-%M-%d')
        url = '%s/%s/%s,%s' % (settings.DARKSKY_API_URL, settings.DARKSKY_API_KEY, ','.join(location_gps), date_format.isoformat())
        response = requests.get(url)
        data_cleaned = self._clean_data(response.json())

        return data_cleaned

    def _clean_data(self, data):
        """
        Returning the formatted data
        """

        data_cleaned = {}

        try:
            #  Stripping out data that is not needed.
            data_cleaned['humidity'] = data['currently']['humidity']
            data_cleaned['min'] = data['daily']['data'][0]['temperatureMin']
            data_cleaned['max'] = data['daily']['data'][0]['temperatureMax']
            data_cleaned['average'] = data['daily']['data'][0]['apparentTemperatureHigh']
            data_cleaned['median'] = data['daily']['data'][0]['apparentTemperatureMin']
        except:
            data_cleaned = data

        return data_cleaned

    def _daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)
