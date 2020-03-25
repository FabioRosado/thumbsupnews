import contextlib
import re

# positive = list()
# negative = list()

# with open("./datasets/imdb_labelled.csv") as imdb:
#     for line in imdb.readlines():
#         text = line.split('  ')
        
#         with contextlib.suppress(IndexError):
#             if '1' in text[1]:
#                 positive.append(text[0])
#             else:
#                 negative.append(text[0])

# with open("./datasets/amazon_cells_labelled.csv") as amazon:
#     for line in amazon.readlines():
#         text = line.split('.,')
    
#     with contextlib.suppress(IndexError):
#         if '1' in text[1]:
#             positive.append(text[0])
#         else:
#             negative.append(text[0])

# with open('./datasets/yelp_labelled.csv') as yelp:
#     for line in yelp.readlines():
#         text = line.split('.,')
    
#         with contextlib.suppress(IndexError):
#             if '1' in text[1]:
#                 positive.append(text[0])
#             else:
#                 negative.append(text[0])

# with open("./datasets/training_1600000_processed_noemoticon.csv", encoding='latin1') as tweets:
#     for line in tweets.readlines():
#         text = line.split('","')
#         tweet = re.sub(r'@\w+\D', ' ', text[-1].rstrip().replace('"', ''))

#         if '4' in text[0]:
#             positive.append(tweet)
#         else:
#             negative.append(tweet)

# with open('./datasets/positive_tweets.txt') as neg_tweets:
#     for line in neg_tweets.readlines():
#         text = re.sub(r'@\w+\D', ' ', line.rstrip())
#         positive.append(text.replace("'", ''))

# with open('./datasets/negative_tweets.txt') as neg_tweets:
#     for line in neg_tweets.readlines():
#         text = re.sub(r'@\w+\D', ' ', line.rstrip())
#         negative.append(text.replace("'", ''))


# with open('./datasets/positive_text.txt', 'w') as pos:
#     for element in positive:
#         pos.write(element + '\n')

# with open('./datasets/negative_text.txt', 'w') as pos:
#     for element in negative:
#         pos.write(element + '\n')

# all_things = []
# positive = list()
# negative = list()

# with open('./datasets/positive_text.txt', 'r') as pos:
#     for element in pos.readlines():
#         positive.append('"{}",Positive'.format(element.rstrip()))

# with open('./datasets/negative_text.txt', 'r') as neg:
#     for element in neg.readlines():
#         negative.append('"{}",Negative'.format(element.rstrip()))

# all_things = positive[:7000] + negative[:7000]

# print(len(positive), len(negative))
# with open('./datasets/test.csv', 'w') as test:
#     for element in all_things:
#         test.write('{}\n'.format(element))
# import csv

# test = []
# with open('./datasets/uci-news-aggregator.csv', 'r') as news:
#     row = list(csv.reader(news))
#     for headline in row:
#         test.append(headline[1])

# with open('./datasets/news.csv', 'w') as file:
#     for element in test:
#         file.write('"{}"\n'.format(element))

from classifier import classify_sentence

with open('./datasets/classified_news.csv', 'w') as classified:
    with open('./datasets/news.csv') as news:
        for headline in news.readlines():
            sentiment = classify_sentence(headline, 'review')
            classified.write("{},{}\n".format(headline.rstrip(), sentiment))
        

# with open('./datasets/classified_news.csv', 'r') as class_news:
#     for element in classified:
#         class_news.write(element)