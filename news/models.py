from django.db import models

# Create your models here.


# from __future__ import unicode_literals
from django.db import models
# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=50)
    short_text = models.TextField()
    body_text = models.TextField()
    date = models.CharField(max_length=12)
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50, default="-")
    catid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)




    # def __str__(self):
    #     return self.name
    def __str__(self):
        return self.name