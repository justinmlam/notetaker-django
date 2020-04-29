from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title