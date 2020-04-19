import sys

import re
from datetime import datetime, timedelta
from dateutil.parser import parse
import importlib
from classifier import NewsHeadlineClassifier

def is_todays_article(node):
    """Get the date from the article and compare it to todays date
    if is the same them the article is returned otherwise not."""
    try:
        article_date = parse(node.xpath('pubDate/text()').get()).date()
        now = datetime.now().date()
        
        if article_date == now:
            return True
        return False
    except Exception:
        return False
    

def transform_date(date):
    """Transform date to return just day, month and year.
    The date obtained from the feed will have the following 
    format - `2020-04-03T03:01:00Z` and we want to just get
    the date."""
    return parse(date, ignoretz=True).date()

def remove_html(description):
    try:
        plain_text = re.sub('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});|\\n|\\t|\[|\]', '', description)
        return plain_text.replace('"', "'").strip()
    except Exception:
        return description
