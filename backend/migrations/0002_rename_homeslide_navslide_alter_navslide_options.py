# Generated by Django 4.0.4 on 2022-05-11 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeSlide',
            new_name='NavSlide',
        ),
        migrations.AlterModelOptions(
            name='navslide',
            options={'verbose_name': 'Navbar slide', 'verbose_name_plural': 'Navbar slides'},
        ),
    ]