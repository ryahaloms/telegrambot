import requests
import json

URL = "https://weatherapi-com.p.rapidapi.com/current.json"

class Weather:
    def __init__(self):
        self.Locations = {'Tel Aviv': [32.08, 34.78],
                          'Haifa': [32.79, 34.98],
                          }

    def get_Weather(self, message: str) -> str:
        headers = {
            "X-RapidAPI-Key": "265216fb9dmsh86ad344ffb80d47p18d65djsn5d7c183c99c0",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        city = ""
        if 'tel aviv' in message.lower():
            querystring = {"q": {self.Locations['Tel Aviv'][0], self.Locations['Tel Aviv'][1]}}
            city = 'Tel Aviv'
        if 'haifa' in message.lower():
            querystring = {"q": {self.Locations['Haifa'][0], self.Locations['Haifa'][1]}}
            city = 'Haifa'

        if city != "":
            response = requests.get(URL, headers=headers, params=querystring)
            json_data = json.loads(response.text)
            return "The current temperature in " +  city  + " is " + str(json_data['current']['temp_c'])
        return ""


