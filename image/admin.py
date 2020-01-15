from django.contrib import admin
from .models import ImageData, DeletedImage
# Register your models here.

admin.site.register(ImageData)
admin.site.register(DeletedImage)
