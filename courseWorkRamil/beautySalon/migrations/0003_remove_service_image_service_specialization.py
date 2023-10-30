# Generated by Django 4.2.5 on 2023-10-05 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautySalon', '0002_remove_master_specialization_alter_service_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='specialization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='beautySalon.specialization', verbose_name='Сепциализация'),
            preserve_default=False,
        ),
    ]
