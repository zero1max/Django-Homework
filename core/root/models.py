from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title