from django.db import models

# Create your models here.
class Projet (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologie = models.CharField(max_length=300)
    git_url = models.URLField(blank=True)
    image = models.ImageField(blank=True, upload_to='projects/')

    def __str__(self):
        return self.title