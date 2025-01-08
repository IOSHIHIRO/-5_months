from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    GENRE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    test = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.CharField(max_length=100, choices=GENRE, null=True)


    def __str__(self):
        return self.test
