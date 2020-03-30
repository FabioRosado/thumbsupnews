from datetime import datetime, timedelta
from dateutil.parser import parse

def is_todays_article(node):
    """Get the date from the article and compare it to todays date
    if is the same them the article is returned otherwise not."""
        article_date = parse(node.xpath('pubDate/text()').get()).date()
        now = datetime.now().date()
        
        if article_date == now:
            return True
        return False
