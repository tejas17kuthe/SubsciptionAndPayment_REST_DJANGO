# Generated by Django 2.0.2 on 2021-01-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptionAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptiondetails',
            name='duration',
            field=models.IntegerField(default=1),
        ),
    ]
