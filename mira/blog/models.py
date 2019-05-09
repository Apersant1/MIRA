from django.db import models

class NameModel(models.Model):
    name = models.TextField(max_length=20)


    def __str__(self):
        return '{}'.format(self.name)