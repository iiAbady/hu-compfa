# Generated by Django 3.0.6 on 2020-09-27 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0037_auto_20200928_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorialsvideos',
            options={'ordering': ['-pub_date']},
        ),
    ]