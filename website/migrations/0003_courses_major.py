# Generated by Django 3.0.6 on 2020-07-23 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='major',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='website.Major'),
            preserve_default=False,
        ),
    ]