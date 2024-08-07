from django.db import models

# Create your models here.
class User(models.Model):
    #name = models.CharField(max_length=100) 
    username = models.CharField(max_length=100)
    credential = models.CharField(max_length=100, null=True)
    personid = models.IntegerField(null=True)
    passwords = models.JSONField(default=list)

    def __str__(self):
        return self.username
    
    def get_passwords(self):
        return self.passwords