from django.db import models


class ExText(models.Model):
    titleText= models.CharField(max_length=200)
    descText= models.CharField(max_length=200)
    imagePath= models.CharField(max_length=200)
    
    def __str__(self):
        return self.titleText
