# Generated by Django 4.0.5 on 2022-10-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrior',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resource', verbose_name='Изображение'),
        ),
    ]
