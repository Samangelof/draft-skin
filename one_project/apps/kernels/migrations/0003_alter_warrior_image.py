# Generated by Django 4.0.5 on 2022-10-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernels', '0002_alter_warrior_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrior',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='resource', verbose_name='Изображение'),
        ),
    ]