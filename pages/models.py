from django.db import models

class Attack(models.Model):

    operators = models.CharField(max_length=10)

    def __str__(self):
        return str(self.operators)


class Defence(models.Model):

    operators = models.CharField(max_length=10)

    def __str__(self):
        return str(self.operators)