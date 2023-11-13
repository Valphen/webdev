from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    creation_datetime = models.DateTimeField(auto_now=True)

class Commentary(models.Model):                                     #У комментария есть время написания, у комментария есть автора, у комментария есть текст, у комменатрия есть количество лайков
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Tag(models.Model):                                            #У тега есть название с припиской #
    name = models.CharField(max_length=50)

class Category(models.Model):                                       #У категории есть название
    name = models.CharField(max_length=100)