# Generated by Django 2.0.5 on 2020-01-14 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20200114_0616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageData',
        ),
    ]
