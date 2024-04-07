from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


# Create your models here.
class Routs(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Number of train')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Time in travel')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='rout_from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='rout_to_city')
    trains = models. ManyToManyField('train.Train', verbose_name='List of trains')

    def __str__(self):
        return f'Train of {self.name}'


