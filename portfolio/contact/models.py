from django.db import models


# Create your models here.
class Contact(models.Model):
    """
    Représente le contact de utilisateur
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
