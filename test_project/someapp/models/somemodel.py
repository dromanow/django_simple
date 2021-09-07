from django.db import models
from django.contrib.sites.models import Site
from django.dispatch import receiver
from .hit_count import some_signal


@receiver(some_signal)
def print_some_signal(sender, **kwargs):
    pass


class SomeOtherModel(models.Model):
    value = models.CharField(max_length=65)

    def __str__(self):
        return self.value


class SomeModel(models.Model):
    value = models.CharField(max_length=65)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    # on_site = CurrentSiteManager('site')
    other = models.ForeignKey(SomeOtherModel, on_delete=models.CASCADE)
    other1 = models.ManyToManyField(SomeOtherModel, related_name='other1')

    def __str__(self):
        return self.value

