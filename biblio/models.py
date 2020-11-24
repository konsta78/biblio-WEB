from django.db import models

# Create your models here.


class Book(models.Model):
    GENRE = (
        ('Классика', 'Классика'),
        ('Фантастика', 'Фантастика'),
        ('Проза', 'Проза'),

    )

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=15, choices=GENRE)
    year = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name