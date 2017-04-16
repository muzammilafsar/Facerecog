from django.db import models

# Create your models here.
class SearchHistory(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.ImageField(upload_to='unkown_people')
    date=models.DateTimeField(auto_now_add=True)