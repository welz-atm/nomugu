# Generated by Django 3.1.3 on 2020-12-15 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_product_view_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_one', models.ImageField(upload_to='media')),
                ('image_two', models.ImageField(upload_to='media')),
                ('image_three', models.ImageField(upload_to='media')),
                ('image_four', models.ImageField(upload_to='media')),
                ('image_five', models.ImageField(upload_to='media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ManyToManyField(to='product.Photo'),
        ),
    ]
