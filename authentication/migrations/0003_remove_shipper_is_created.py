# Generated by Django 3.1.3 on 2021-03-04 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_shipper_is_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipper',
            name='is_created',
        ),
    ]
