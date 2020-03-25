# Followed instructions from: https://edmundmartin.com/text-classification-with-python-nltk/
import re
import nltk 
from nltk.classify.scikitlearn import SklearnClassifier
from random import shuffle
import pickle

class NewsHeadlinerClassifier:
    def __init__(self, csv_file, featureset_size=1000, test_ratio=0.1):
        self.csv_file = csv_file
        self.documents = []
        self.words = []
        self.featureset_size = featureset_size
        self.test_ratio = test_ratio
        self.feature_words = None
        self.classifier = None
    
    def _read_csv(self):
        with open(self.csv_file, 'r') as input_csv:
            for item in input_csv:
                item = item.split(',')
                doc, label = re.findall('\w+', ''.join(item[:-1]).lower()), item[-1].strip()
                for word in doc:
                    self.words.append(word.lower())
                self.documents.append((doc, label))
    
    def get_words_only(self, sentence):
        """Get only words from sentence."""
        return re.findall('\w+', sentence)
    
    def _generate_word_features(self):
        frequency_dist = nltk.FreqDist()
        for word in self.words:
            frequency_dist[word] += 1
        self.feature_words = list(frequency_dist)[:self.featureset_size]
        print(self.feature_words[123])

    def _document_features(self, document):
        document_words = set(document)
        features = {}
        for word in self.feature_words:
            features['contains({})'.format(word)] = (word in document_words)
        return features
    
    def train_naive_bayes_classifier(self):
        print("Initializing classifier training.")
        if not self.feature_words:
            self._read_csv()
            self._generate_word_features()
        print('Shuffling documents...')
        shuffle(self.documents)
        print('Getting feature set from documents...')
        feature_sets = [(self._document_features(d), c) for (d, c) in self.documents]
        print('Getting cutoff size...')
        cutoff = int(len(feature_sets) * self.test_ratio)
        print('Splitting feature set into training and test sets...')
        train_set, test_set = feature_sets[cutoff:], feature_sets[:cutoff]
        print('Finally starting to train classifier...')
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
        print('Achieved {0:.2f}% accuracy against training set'.format(nltk.classify.accuracy(self.classifier, train_set)*100))
        print('Achieved {0:.2f}% accuracy against test set'.format(nltk.classify.accuracy(self.classifier, test_set)*100))
    
    def classify_new_sentence(self, sentence):
        # print("Starting to classify '{}'".format(sentence))
        if not self.feature_words:
            self._read_csv()
            self._generate_word_features()
        test_features = {}
        for word in self.feature_words:
            test_features['contains({})'.format(word.lower())] = (word.lower() in nltk.word_tokenize(sentence))
        return self.classifier.classify(test_features)

    def save_model(self, filename):
        save_classifier = open(filename, "wb")
        pickle.dump(self.classifier, save_classifier)
        save_classifier.close()
        save_vocab = open('vocab-{}'.format(filename), "wb")
        pickle.dump(self.feature_words, save_vocab)
        save_vocab.close()
 
    def load_model(self, model_filename, vocab_filename):
        classifier_f = open(model_filename, "rb")
        self.classifier = pickle.load(classifier_f)
        classifier_f.close()
        vocab_f = open(vocab_filename, "rb")
        self.feature_words = pickle.load(vocab_f)
        vocab_f.close()


def classify_sentence(text, classifier_name):
    classifier = NewsHeadlinerClassifier('./datasets/classified_news.csv', featureset_size=50000)
    
    try:
        classifier.load_model(classifier_name, 'vocab-{}'.format(classifier_name))
    except Exception:
        classifier.train_naive_bayes_classifier()
        classifier.classifier.show_most_informative_features(20)
        classifier.save_model(classifier_name)
    
    return classifier.classify_new_sentence(text)
