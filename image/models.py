from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class ImageData(models.Model):
    name = models.CharField(max_length=500)
    image = models.FileField()

    def __str__(self):
        return self.name




class DeletedImage(models.Model):
    image_id = models.IntegerField()




#signals
@receiver(post_delete, sender=ImageData)
def my_handler(sender, **kwargs):
    instance = kwargs['instance']
    image_id = instance.id
    delted_image = DeletedImage.objects.create(image_id=image_id)



