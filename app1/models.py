from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    director = models.CharField(max_length=150, verbose_name="Director")
    release_year = models.IntegerField(verbose_name="Release Year")
    genre = models.CharField(max_length=100, verbose_name="Genre")
    duration = models.IntegerField(verbose_name="Duration (min)")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0, verbose_name="Rating (0-10)")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} ({self.release_year})"
