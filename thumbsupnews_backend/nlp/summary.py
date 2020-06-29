"""https://stackabuse.com/text-summarization-with-nltk-in-python/"""
import re
import heapq
import nltk

from nltk.corpus import stopwords
from collections import defaultdict


class Summary:
    def __init__(self, text, sentences=7, words=30):
        self.text = text
        self.sentences = sentences
        self.words = words
        self.formatted_text = None
        self.word_frequencies = {}
        self.sentence_score = {}
        self.sentence_list = []
        self.stopwords = stopwords.words("english")

    def clean_text(self):
        """Clean up text."""
        text = re.sub(r"\[[0-9]*\]", " ", self.text)
        self.text = re.sub(r"\s+", " ", text)

        formatted_text = re.sub(r"[^a-zA-Z]|\s+", " ", self.text)
        self.formatted_text = re.sub(r"\s+", " ", formatted_text)

        self.sentence_list = nltk.sent_tokenize(self.text)

    def get_word_frequencies(self):
        """Get word frequency from text."""
        frequency = defaultdict(lambda: 0)

        for word in nltk.word_tokenize(self.formatted_text):
            if word not in self.stopwords:
                frequency[word] += 1

        maximum_frequency = max(frequency.values())

        for word in frequency.keys():
            self.word_frequencies[word] = frequency[word] / maximum_frequency

    def get_sentence_scores(self):
        """Get sentence score."""
        for sentence in self.sentence_list:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in self.word_frequencies.keys():
                    if len(sentence.split(" ")) < self.words:
                        if sentence not in self.sentence_score.keys():
                            self.sentence_score[sentence] = self.word_frequencies[word]
                        else:
                            self.sentence_score[sentence] += self.word_frequencies[word]

    def get_summary(self):
        """Get the summary from text, use all the methods available."""
        self.clean_text()
        self.get_word_frequencies()
        self.get_sentence_scores()

        return " ".join(
            heapq.nlargest(
                self.sentences, self.sentence_score, key=self.sentence_score.get
            )
        )
