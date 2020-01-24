from rest_framework import serializers
from image.models import ImageData, DeletedImage
import base64
from PIL import Image
import os
from django.conf import settings


class ImageSerializer(serializers.ModelSerializer):
    decode = serializers.SerializerMethodField()
    class Meta:
        model = ImageData
        fields = ('id','name', 'image', 'decode', 'ward')

    def get_decode(self, instance):
        # with open('media/' + str(self.image), "rb") as img_file:
    #         img_encode = base64.b64encode(img_file.read()).decode("utf-8")
    #         print(img_encode)
    #
    #     # print("aaaaa")
    #     # print(base64.b64encode(image))
    #
    #     # if self.image:
    #     print()
        image_url = instance.image.url[1:]
        print(image_url)

        with open(image_url, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read())
            decoded_string = encoded_string.decode("utf-8")


        image = Image.open(instance.image)

        image_name, image_extension = os.path.splitext(instance.image.name)
        print(image_name)
        image_extension = image_extension.lower()

        decode = 'data:image/%s;base64,%s' % (image_extension, decoded_string)

        return decode

class DeletedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeletedImage
        fields = '__all__'

