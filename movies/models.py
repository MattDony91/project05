from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=150)
    watch_grade = models.CharField(max_length=150)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)