# Generated by Django 3.0.1 on 2020-01-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200128_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentprojectimages',
            name='image',
            field=models.ImageField(upload_to='currentProjectImages/', verbose_name=''),
        ),
    ]
