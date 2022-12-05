from django.db import models


# Create your models here.
class GetInTouch(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
