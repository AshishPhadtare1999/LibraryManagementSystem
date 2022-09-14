from django.db import models
from django.contrib.auth.models import User
# Create your models here.

User._meta.get_field('email')._unique = True

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=200)
    price=models.FloatField()
    date=models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table="books"
        