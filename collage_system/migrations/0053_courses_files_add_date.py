# Generated by Django 3.0.6 on 2020-10-13 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0052_auto_20201011_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses_files',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]