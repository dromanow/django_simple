from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.dispatch import Signal

some_signal = Signal()


class HitCount(models.Model):
    url = models.CharField(max_length=256, primary_key=True)
    hits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.url} ({self.hits})'

    def save(self, *args, **kwargs):
        print(str(self))
        some_signal.send(self, test=1)
        super().save(*args, **kwargs)


@receiver(pre_save, sender=HitCount)
def print_hit_count(sender, instance, **kwargs):
    print(str(instance))
