# Generated by Django 4.0.4 on 2022-05-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_trandy',
            field=models.BooleanField(default=False),
        ),
    ]
