from django.db import models
from nlp.classifier import NewsHeadlineClassifier
from nlp.summary import SummaryClass

CLASSIFIER = NewsHeadlineClassifier()


class Headline(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(max_length=300)
    description = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    categories = models.CharField(max_length=300, blank=True)
    source = models.CharField(max_length=150)
    sentiment = models.CharField(max_length=10)
    is_positive = models.BooleanField(default=False)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

    class Meta:
        managed = True
        ordering = ["created"]


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Sentiment(models.Model):
    message = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        self.sentiment = CLASSIFIER.classify(self.message)
        super(Sentiment, self).save(*args, **kwargs)


class Summary(models.Model):
    text = models.TextField()
    summary = models.TextField(blank=True)
    sentences = models.IntegerField(default=7)
    words = models.IntegerField(default=30)

    def save(self, *args, **kwargs):
        text_summary = SummaryClass(self.text, sentences=self.sentences, words=self.words)
        self.summary = text_summary.get_summary().replace('"', "'")
        super(Summary, self).save(*args, **kwargs)