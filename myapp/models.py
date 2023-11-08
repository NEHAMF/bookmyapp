from django.db import models
class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    page_no=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return(self.name)
    
    
# Create your models here.
