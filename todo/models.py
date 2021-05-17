from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=100)
    time = models.DateTimeField('last updated time')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
