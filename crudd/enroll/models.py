from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    """ def __str__(self):
        return f'{self.name}'
 """