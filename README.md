# Thumbs Up News

Thumbs Up News is a project that aims to scrape different news sources and use a sentiment analysis classifier to check if the headline of the article is a positive/neutral one or negative. If the article is negative we want to remove it from the list of articles to be shown on the website.

## Structure

- **classifier** - contains all the necessary code to train, safe and load both our sentiment analysis classifier and the category classifier.
- **scrapper** - Using scrappy to scrape RSS feeds. We are running all the scraper spiders from within the `run_spiders.py` script.
- **scripts** - This is the folder that contains important scripts for the project. We run `upload_backend.py` to push new RSS data into the backend. _Note: Django server must be running otherwise you won't be able to call the api endpoint._
- **thumbsupnews_backend** - Django backend. We are using a single app which is using Django Rest Framework to manage our db and api.
- **frontend** - Nextjs frontend using tailwindcss and a lot of custom css rules. We are querying the rest api endpoint created by django backend, which means it needs to be working before we start the frontent.
