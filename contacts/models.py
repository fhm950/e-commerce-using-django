from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name