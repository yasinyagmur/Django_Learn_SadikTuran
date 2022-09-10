from pyexpat import model
from django.db import models
from django.utils.text import slugify
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=50)
    description=models.TextField()
    is_activate=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    # slugField modele daha sonradan eklendiği için ilk önce null kısmı True yapılır
    #  model de bulunan datalara slug eklendikten sonra silinir ya da false yapılır default değeri false
    # slug=models.SlugField(null=True,blank=True,unique=True,db_index=True)
    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def __str__(self):
        return f"{self.title}"


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

class Category(models.Model):
    name=models.CharField(max_length=150)
    lastName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"