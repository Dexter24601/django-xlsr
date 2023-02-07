from django.db import models

# Create your models here.

class visitors(models.Model):

    username = models.CharField(default='user',null=True, max_length=100)
    id = models.PositiveIntegerField(primary_key=True,default='')
    
    def __str__(self):
        return (f'{self.username}-{self.id}')