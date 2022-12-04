import uuid
from django.db import models


# Create your models here.
class GetInTouch(models.Model):
    uuid_code = models.UUIDField('UUID CODE', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
