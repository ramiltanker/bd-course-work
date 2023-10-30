# Generated by Django 4.2.5 on 2023-10-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautySalon', '0003_remove_service_image_service_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.IntegerField(default=None, verbose_name='Длительность, мин'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='master',
            name='image',
            field=models.ImageField(upload_to='images/masters/', verbose_name='Изображение'),
        ),
    ]