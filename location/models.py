from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LocalGovArea(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
