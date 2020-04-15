import os
import subprocess
import jsonlines
import requests
import time


print("Starting to run scrapper to get todays feeds...")

subprocess.call(["python", "../scrapper/run_spiders.py"])

print("Done scrapping todays feeds. Starting to push them to the database...")

with jsonlines.open('../scrapper/news.jl') as reader:
    for line in reader:
        print(line)
        r = requests.post('http://localhost:8000/headlines/',
                          headers={'Authorization': f"Token {os.environ['DJANGO_TOKEN']}"},
                          data=line)

print("Done uploading todays headlines to backend. Removing file...")

try:
    os.remove('../scrapper/news.jl')

    print("Done. Headlines file removed successfully.")
except Exception as error:
    print(f"Ooops! There was an error trying to remove the file \nError: {error}")