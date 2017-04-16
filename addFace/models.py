from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=50,null=True)
    profession=models.CharField(max_length=20,null=True)
    photo=models.ImageField(upload_to='Known_people')
    def __str__(self):
        return self.name

