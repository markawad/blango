from django.db import models


class Tag(models.Model):

    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value
