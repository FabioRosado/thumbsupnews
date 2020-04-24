import os
import subprocess
import jsonlines
import requests
import time


print("Adding scrapped news to the dataset...")
with open('../classifier/datasets/new_classified_news.csv','a') as dataset:
    with jsonlines.open('../scrapper/news.jl') as reader:
        for item in reader.iter(type=dict, skip_invalid=True):
            dataset.write(f"{item['title']},{item['sentiment']}\n")


with jsonlines.open('../scrapper/news.jl') as reader:
    for line in reader:
        r = requests.post('http://localhost:8000/headlines/',
                        headers={'Authorization': f"Token {os.environ['DJANGO_TOKEN']}"},
                        data=line)

print("Done uploading todays headlines to backend. Removing file...")

try:
    os.remove('../scrapper/news.jl')

    print("Done. Headlines file removed successfully.")
except Exception as error:
    print(f"Ooops! There was an error trying to remove the file \nError: {error}")
