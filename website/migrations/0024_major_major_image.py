# Generated by Django 3.0.6 on 2020-07-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_activities_activitie_disc'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='major_image',
            field=models.ImageField(null=True, upload_to='major_pic'),
        ),
    ]