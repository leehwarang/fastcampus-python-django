from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    movie = models.ForeignKey('movie.Movie', on_delete = models.CASCADE)

    def __str__(self):
        return '{}리뷰'.format(self.title)
        
