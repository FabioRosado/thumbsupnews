import os
import subprocess
import jsonlines
import requests
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_DATASET = os.path.join(ROOT, 'classifier', 'datasets', 'news_dataset.json')
SCRAPPED_NEWS = os.path.join(ROOT, 'scrapper', 'news.jl')

print("Adding scrapped news to the dataset...")
with open(NEWS_DATASET,'a') as dataset:
    with jsonlines.open(SCRAPPED_NEWS) as reader:
        for item in reader.iter(type=dict, skip_invalid=True):
            dataset.write(f"{item}\n")



with jsonlines.open(SCRAPPED_NEWS) as reader:
    for line in reader:
        r = requests.post('http://localhost:8000/headlines/',
                        headers={'Authorization': f"Token {os.environ['DJANGO_TOKEN']}"},
                        data=line)

print("Done uploading todays headlines to backend. Removing file...")

try:
    os.remove(SCRAPPED_NEWS)

    print("Done. Headlines file removed successfully.")
except Exception as error:
    print(f"Ooops! There was an error trying to remove the file \nError: {error}")
