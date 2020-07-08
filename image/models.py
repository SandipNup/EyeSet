from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.


class ImageData(models.Model):
    WARD_CHOICES = (
        ('0', 'All Ward'),
        ('test', 'test'),
        ('lmc2', 'LMC 2'),
        ('lmc9', 'LMC 9'),
        ('lmc11', 'LMC 11'),
        ('kmc10', 'KMC 10'),
        ('kmc12', 'KMC 12'),
        ('kmc31', 'KMC 31'),
    )

    name = models.CharField(max_length=500)
    image = models.FileField()
    ward = models.CharField(choices=WARD_CHOICES, default='0', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class DeletedImage(models.Model):
    image_id = models.IntegerField()


# signals
@receiver(post_delete, sender=ImageData)
def my_handler(sender, **kwargs):
    instance = kwargs['instance']
    image_id = instance.id
    delted_image = DeletedImage.objects.create(image_id=image_id)
