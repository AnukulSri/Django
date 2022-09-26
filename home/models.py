from django.db import models


#  makemigrations - it means create changes and store in a file
# migrate - it means apply the pemding changes created by makemigrations


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    message=models.TextField()
    Password=models.CharField(max_length=20)
    date=models.DateField()

    def __str__(self):
     return self.name
    


# Create your models here
