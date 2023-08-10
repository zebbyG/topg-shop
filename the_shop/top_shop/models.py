from django.db import models


class Message(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.CharField(max_length=2500)

    def __str__(self):
        return f'A message from {self.email}'
