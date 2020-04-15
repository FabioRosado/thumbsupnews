import jsonlines
import requests
import time



with jsonlines.open('../scrapper/news.jl') as reader:
    for line in reader:
        print(line)
        r = requests.post('http://localhost:8000/headlines/',
                          headers={'Authorization': "Token db8f2e530bf43f0ca9cab6c5013c9daf521d5278"},
                          data=line)
        time.sleep(.5)