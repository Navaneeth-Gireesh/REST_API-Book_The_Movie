from django.db import models

# Create your models here.

class MoviesData(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DecimalField(max_digits=2, decimal_places=1)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genere = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_images', default='movie_images/defaultimage.png')
    
    def __str__(self):
        return self.name