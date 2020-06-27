from django.db import models
# from backend.classifier import NewsHeadlineClassifier
from nlp.classifier import NewsHeadlineClassifier

CLASSIFIER = NewsHeadlineClassifier()


class Headline(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField(max_length=300)
    description = models.TextField(blank=True)
    categories = models.CharField(max_length=300, blank=True)
    source = models.CharField(max_length=150)
    sentiment = models.CharField(max_length=10)
    is_positive = models.BooleanField(default=False)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Sentiment(models.Model):
    message = models.TextField()
    sentiment =  models.CharField(max_length=10, blank=True)
    
    def save(self, *args, **kwargs):
        self.sentiment = CLASSIFIER.classify(self.message)
        super(Sentiment, self).save(*args, **kwargs)