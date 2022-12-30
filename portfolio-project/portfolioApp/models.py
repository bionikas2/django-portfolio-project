from django.db import models

# Create your models here.
class Project(models.Model):
    titles = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolioApp/images/")
    url = models.URLField(blank=True)
