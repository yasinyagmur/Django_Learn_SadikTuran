from pyexpat import model
from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=50)
    description=models.TextField()
    is_activate=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name=models.CharField(max_length=150)
    lastName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"