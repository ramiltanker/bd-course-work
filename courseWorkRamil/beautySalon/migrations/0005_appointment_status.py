# Generated by Django 4.2.5 on 2023-10-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautySalon', '0004_service_duration_alter_master_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Запись закрыта'),
        ),
    ]
