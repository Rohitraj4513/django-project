from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
