#Use aipython utube vedio  referance (In 5 steps |Using weather api in python to get weather-report of any place)
import requests
import json
import os
from datetime import datetime



#location = input("Enter the city name: ")
#posted from website :   api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

complete_api_link = "https://api.covid19api.com/summary"

api_link = requests.get(complete_api_link)
api_data = api_link.json()
#api_content = json.loads(api_link)
#location = input("Enter the city name: ")
print("Golbally TotalConfirmed: "+str(api_data['Global']['TotalConfirmed']))
print("Globally TotalRecovered: "+str(api_data['Global']['TotalRecovered']))
for x in range(len(api_data['Countries'])):
    print("Country: "+api_data['Countries'][x]['Country'])
    print("TotalConfirmed: "+str(api_data['Countries'][x]['TotalConfirmed']))
    print("TotalRecovered: "+str(api_data['Countries'][x]['TotalRecovered']))
    print("Date: "+str(api_data['Countries'][x]['Date']))


