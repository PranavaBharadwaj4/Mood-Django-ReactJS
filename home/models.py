from django.db import models

# Create your models here.
class Contact(models.Model):
    class Reaction(models.IntegerChoices):
        AWFUL = 1
        BAD = 2
        MEH = 3
        GOOD = 4
        RAD = 5

    reaction = models.IntegerField(choices=Reaction.choices)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self) -> str:
        return self.name