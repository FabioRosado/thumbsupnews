import os
import re
import csv
import itertools
import nltk
import jsonlines
import pickle

from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy
from nltk.corpus import stopwords
from nltk.tokenize.regexp import regexp_tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CategoryClassifier:
    def __init__(self):
        self.categories = {
                "politics": [],
                "wellness": [],
                "entertainment": [],
                "travel": [],
                "health": [],
                "food": [],
                "business": [],
                "comedy": [],
                "sports": [],
                "lifestyle": [],
                "women": [],
                "weird news": [],
                "religion": [],
                "science": [],
                "tech": [],
                "money": [],
                "arts": [],
                "parenting": [],
                "environment": [],
                "education": [],
                "impact": [],
         }
        try: 
            print("Loading category classifier...")
            self.classifier = self.load_classifier()
            print("Category classifier loaded!")
        except FileNotFoundError:
            print("No classifier found, opening dataset and will train new classifier.")
            self.classifier = self._train_classifier()

    def format_sentence(self, sent):
        """Tokenize sentence and return format that can work with NLTK.NaiveBayesClassifier."""
        return {
            word: True
            for word in regexp_tokenize(sent, pattern='\w+')
            if word not in stopwords.words('english')
            }

    def _read_dataset(self):
        """Open news dataset and divides contents by category."""
        print("Opening dataset News Category Dataset v2 (200k entries) and splitting data...")
        with jsonlines.open(os.path.join(ROOT, 'classifier', 'datasets', 'News_Category_Dataset_v2.json')) as news:
            for item in news.iter(type=dict, skip_invalid=True):
                cat = item['category'].lower()

                if 'style' in cat or 'home' in cat:
                    self.categories['lifestyle'].append(
                            [self.format_sentence(item['headline'].lower()), 'Lifestyle']
                            )
                    self.categories['lifestyle'].append(
                            [self.format_sentence(item['short_description'].lower()), 'Lifestyle']
                            )

                if 'food' in cat or 'taste' in cat:
                    self.categories['food'].append(
                            [self.format_sentence(item['headline'].lower()), 'Food']
                            )
                    self.categories['food'].append(
                            [self.format_sentence(item['short_description'].lower()), 'Food']
                            )

                if 'art' in cat:
                    self.categories['arts'].append(
                            [self.format_sentence(item['headline'].lower()), 'Arts']
                            )
                    self.categories['arts'].append(
                            [self.format_sentence(item['short_description'].lower()), 'Arts']
                            )

                if 'healthy' in cat:
                    self.categories['health'].append(
                            [self.format_sentence(item['headline'].lower()), 'Health']
                            )
                    self.categories['health'].append(
                            [self.format_sentence(item['short_description'].lower()), 'Health']
                            )

                if cat in self.categories.keys():
                    self.categories[cat].append(
                            [self.format_sentence(item['headline'].lower()), cat.title()]
                           )
                    self.categories[cat].append(
                            [self.format_sentence(item['short_description'].lower()), cat.title()]
                            )

        print("Done splitting data. Opening UCI News Aggregator (400k entries) and splitting data...")
        
        with open(os.path.join(ROOT, 'classifier', 'datasets', 'uci-news-aggregator.csv'),) as input_csv:
            news_reader = csv.reader(input_csv, delimiter =",")
            for row in news_reader:
                if row[4] == 'b':
                    self.categories['business'].append(
                        [self.format_sentence(row[1].lower()), 'Business']
                    )
                
                if row[4] == 't':
                    self.categories['tech'].append(
                        [self.format_sentence(row[1].lower()), 'Tech']
                    )

                if row[4] == 'e':
                    self.categories['entertainment'].append(
                        [self.format_sentence(row[1].lower()), 'Entertainment']
                    )
                if row[4] == 'm':
                    self.categories['health'].append(
                        [self.format_sentence(row[1].lower()), 'Health']
                    )
        print("Done splitting ")


    def get_dataset_numbers(self):
        for key, value in self.categories.items():
            print(f"{key}: {len(value)}")
    
    def _train_classifier(self):
        """Use 80% of hedlines to train a classifier."""
        self._read_dataset()
        
        flatten = itertools.chain.from_iterable
                
        training = list(flatten([item[:int(.8 * len(item))] for item in self.categories.values()]))
        testing = list(flatten([item[int(.8 * len(item)):] for item in self.categories.values()]))
        print("Trainig Classifier...")

        classifier = NaiveBayesClassifier.train(training)
        print(f"Classifier trained with successfully - accuracy rating: {round(accuracy(classifier, testing), 2)}%")

        self.save_classifier(classifier)
        return classifier

    def classify(self, text):
        """Uses trained classifier to classify a piece of text."""
        classified = self.classifier.classify(self.format_sentence(text))
        return classified

    def save_classifier(self, classifier):
        with open(os.path.join(ROOT, 'classifier', 'category.pickle'), 'wb') as save_classifier:
            pickle.dump(classifier, save_classifier)

    def load_classifier(self):
        with open(os.path.join(ROOT, 'classifier', 'category.pickle'), 'rb') as loaded_classifier:
            return pickle.load(loaded_classifier)
