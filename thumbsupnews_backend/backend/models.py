from django.db import models


class Headline(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    categories = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=150)
    sentiment = models.CharField(max_length=10)
    is_positive = models.BooleanField(default=False)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']