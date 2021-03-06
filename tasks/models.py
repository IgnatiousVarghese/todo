from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    title= models.CharField(max_length= 100)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    completed = models.BooleanField(default= False)
    author = models.ForeignKey(User, on_delete= models.CASCADE ,null=True)

    def __str__(self):
        return self.title
