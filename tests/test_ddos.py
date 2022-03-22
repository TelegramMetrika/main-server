import requests
import datetime


for i in range(0, 20):
    requests.post('http://0.0.0.0:5000/get')