from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Number of train')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Time in travel')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city')

    def __str__(self):
        return f'Train of {self.name}'

    class Meta:
        pass

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Change city')
        qs = Train.objects.filter(from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Change time of travel')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

