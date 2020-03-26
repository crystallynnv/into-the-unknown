from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
RATINGS = (
    ('🤮🤬😱', '🤮🤬😱'),
    ('💩🤔😰', '💩🤔😰'),
    ('😑😶🙄', '😑😶🙄'),
    ('😉🧐🙂', '😉🧐🙂'),
    ('🤩🥳😎', '🤩🥳😎')
)

class Place(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places_detail', kwargs={'place_id': self.id})

class Review(models.Model):
    date = models.DateField('review date')
    details = models.CharField(max_length=500)
    rating = models.CharField(
        max_length=100,
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for place_id: {self.place_id} @{self.url}"
