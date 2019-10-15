import requests
import os
import argparse
import sys

API = os.getenv('OPEN_API_KEY')

parser = argparse.ArgumentParser()

parser.add_argument('--city',required=True)

args=parser.parse_args()

if not API:
	print ('API key not found.')
	sys.exit(1)

response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={args.city}&appid={API}')

print ("City: ",response.json()['name'])
print ("Current Weather: ",response.json()['weather'][0]['description'])
print ("Temperature: "+ str(round(response.json()['main']['temp']-273.15,1)) + " degrees")
