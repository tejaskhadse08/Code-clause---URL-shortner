from django.db import models

# Create your models here.


class ShortUrl(models.Model):
    long_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100)

    def __str__(self):
        return self.long_url
