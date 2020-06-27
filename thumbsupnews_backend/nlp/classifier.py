import os
import re
import nltk
import pickle

from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy
from nltk.corpus import stopwords
from nltk.tokenize.regexp import regexp_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class NewsHeadlineClassifier:
    def __init__(self):
        self.positive_headlines = list()
        self.negative_headlines = list()
        try:
            print("Loading sentiment classifier...")
            self.classifier = self.load_classifier()
            print(f"Sentiment classifier loaded...")
        except FileNotFoundError:
            print(f"No classifier found, opening dataset and will train new classifier.")
            self.classifier = self._train_classifier()

    def format_sentence(self, sent):
        """Tokenize sentence and return format that can work with
        NLTK.NaiveBayesClassifier."""
        return {
            word: True 
            for word in regexp_tokenize(sent, pattern='\w+') 
            if word not in stopwords.words('english')
        }

    # def _read_csv(self):
    #     with open(os.path.join(ROOT, 'nlp', 'dataset', 'dataset.csv'), 'r') as input_csv:
    #         for item in input_csv:
    #             item = item.split(',')
    #             doc, label = re.findall('\w+', ''.join(item[:-1]).lower()), item[-1].strip()

    #             if label == 'positive':
    #                 self.positive_headlines.append([self.format_sentence(' '.join(doc)), 'positive'])
    #             else: 
    #                 self.negative_headlines.append([self.format_sentence(' '.join(doc)), 'negative'])
    #     print("Positive: {} \n Negative: {} \n\n\n".format(len(self.positive_headlines), len(self.negative_headlines)))

    def _train_classifier(self):
        """Use 80% of tweets to train a classifier."""
        # self._read_csv()

        training = self.positive_headlines[:int(.8 * len(self.positive_headlines))] + \
            self.negative_headlines[:int(.8 * len(self.negative_headlines))]

        testing = self.negative_headlines[int(.8 * len(self.positive_headlines)):] + \
            self.negative_headlines[int(.8 * len(self.negative_headlines)):]
        print("Training Classifier...")
        
        print(training[:5])

        classifier = NaiveBayesClassifier.train(training)
        print(f"Classifier trained with "
              f"success - accuracy rating: {round(accuracy(classifier, testing), 2)}%")

        self.save_classifier(classifier)
        return classifier

    def classify(self, text):
        """Uses trained classifier to classify a piece of text."""
        classified = self.classifier.classify(self.format_sentence(text))
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(text)

        if score['neu'] == 1.0:
            return classified

        if score['pos'] > score['neg'] and classified == 'positive':
            return 'positive'

        return 'negative'

    def save_classifier(self, classifier):
        with open(os.path.join(ROOT, 'nlp', 'news.pickle'), 'wb') as save_classifier:
            pickle.dump(classifier, save_classifier)

    def load_classifier(self):
        with open(os.path.join(ROOT, 'nlp', 'news.pickle'), "rb") as loaded_classifier:
            return pickle.load(loaded_classifier)
