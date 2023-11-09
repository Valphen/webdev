from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    creation_datetime = models.DateTimeField(auto_now=True)

