from django.db import models

# Create your models here.


class QuoteTable(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
