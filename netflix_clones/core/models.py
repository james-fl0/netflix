from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Movie(models.Model):

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]
    
    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()  # Store the runtime in minutes
    image_card = models.ImageField(upload_to='movie_images/')  # Movie poster image
    image_cover = models.ImageField(upload_to='movie_images/')  # Movie poster image
    video = models.FileField(upload_to='movie_videos/')  # Movie video file
    movie_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)