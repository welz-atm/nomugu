# Generated by Django 3.1.3 on 2020-11-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_account_is_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='bvn',
        ),
        migrations.AddField(
            model_name='account',
            name='account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='employer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='employer_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='job_role',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(),
        ),
    ]
