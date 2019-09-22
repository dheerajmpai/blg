from django.db import models

# Create your models here.
from django.db import models

class ArticleModel(models.Model):
    author = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    para2 = models.CharField(max_length=1000)
    para1 = models.CharField(max_length=1000)
    art_slug = models.CharField(max_length=100)
   

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
