from django.db import models

# Create your models here.


# from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=50)
    



    # def __str__(self):
    #     return self.name
    def __str__(self):
        return self.name