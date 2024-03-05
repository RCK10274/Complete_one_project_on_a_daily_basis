import pyowm
from os import path
import logging
from requests import Timeout
import requests as req
import time


logger = logging.getLogger("wb_logging.log")


def trans_temp_kelvin_to_celsius(temp):
    # 將溫度從絕對溫度轉成攝氏溫度
    return int(temp - 273.15)

class WeatherStation():
    # document: https://pyowm.readthedocs.io/en/latest/pyowm.weatherapi25.html
    def __init__(self, owm_api_key=None):
        self._owm_api_key = owm_api_key
        self._owm = None

    @property
    def owm(self):
        try:
            if not self._owm:
                self._owm = pyowm.OWM(self._owm_api_key)
        except Timeout as err:
            logger.error('WeatherStation owm fail with TimeOut error {}'.format(err))
        return self._owm

    def get_data_by_coord(self, lon, lat):
        maneger = self.owm.weather_manager()
        observation = maneger.weather_at_coords(lat=lat, lon=lon)
        weather = observation.weather
        return weather.to_dict()

class LineNotion():
    def __init__(self, notion_url):
        self.notion_url = notion_url

    def _enrich_message(self,messager):#從weather抓取,以及輸出後的資料內容,也是會出現在linenotion上的主要內容
        return str({
            'temperature': trans_temp_kelvin_to_celsius(
                messager.get('temperature', {}).get('temp', 'Null')),
            'humidity': messager.get('humidity', 'Null'),
            'status': messager.get('status', 'Null'),
        })
    def notify(self, token, messager):
        headers = {'Authorization': 'Bearer ' + token}
        payload = {'message': self._enrich_message(messager)}
        response = req.post(self.notion_url, headers=headers, params=payload)
        print(self._enrich_message(messager))
        return response

def main():
    
    #------------------------------------------------------------
    line_token = "3QfpV9YcuvdT5G2hlPiivKyPu6bMvNVCcg7IDcIXacH"
    line_url = 'https://notify-api.line.me/api/notify'
    api_key = '69dc38bc98f8d65300eba97d5a6d3531'
    #------------------------------------------------------------
    CURRENT_PATH = path.dirname(path.abspath(__file__))
    HOUR = 60*60
    users_data = [{
        "owm_api_key": api_key,
        "line_token": line_token,
        "longitude": 120.850209,
        "latitude": 24.574295
    }]
    
    ln = LineNotion(line_url)
    while True:
        for user_data in users_data:
            weather_station = WeatherStation(user_data.get('owm_api_key'))
            weather_data = weather_station.get_data_by_coord(
                user_data.get('longitude'), user_data.get('latitude')
            )
            status_code = ln.notify(user_data.get('line_token'), weather_data)
            print(weather_data)
            print(status_code)
        time.sleep(HOUR)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s')
    main()
