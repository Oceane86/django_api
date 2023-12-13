import requests
import csv

FILE = "jobs.csv"
API_URL = "http://127.0.0.1:8000/api/v1/bookmarks/"

headers = {
    "Content-Type": "application/json"
}

data_template = {
    "name": "",
    "url": "",
    "tags": "",
    "comment": "",
    "user": 1
}

with open(FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)
    for row in csv_reader:
        print(row)
        name, url = row
        data = data_template.copy()
        data["name"] = name
        data["url"] = url
        print(data)
        response = requests.post(API_URL, json=data, headers=headers)
