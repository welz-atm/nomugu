# Generated by Django 3.1.3 on 2021-03-07 12:45

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210304_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[230, 192], upload_to='media'),
        ),
    ]
