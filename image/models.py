from django.db import models
import base64
from PIL import Image
import os
from django.conf import settings


# Create your models here.


class ImageData(models.Model):
    name = models.CharField(max_length=500)
    image = models.FileField()

    def __str__(self):
        return self.name

    # def image_as_base64(self):
    #     # print(str(self.image))
    #     with open('media/' + str(self.image), "rb") as img_file:
    #         img_encode = base64.b64encode(img_file.read()).decode("utf-8")
    #         print(img_encode)
    #
    #     # print("aaaaa")
    #     # print(base64.b64encode(image))
    #
    #     # if self.image:
    #
    #     # with open(image, "rb") as img_file:
    #     #     encoded_string = base64.b64encode(img_file.read())
    #     #     decoded_string = encoded_string.decode("utf-8")
    #     #
    #     #     print(decoded_string)
    #
    #     # image = Image.open(self.image)
    #
    #     # image_name, image_extension = os.path.splitext(self.image.name)
    #     # image_extension = image_extension.lower()
    #     #
    #     # self.encode = 'data:image/%s;base64,%s' % {image_extension,decoded_string}
    #
    #     return True
    #
    # def save(self, *args, **kwargs):
    #     if not self.image_as_base64():
    #         raise Exception('Could not create base64 of image')
    #     super(ImageData, self).save(*args, **kwargs)


class DeletedImage(models.Model):
    image_id = models.IntegerField()

