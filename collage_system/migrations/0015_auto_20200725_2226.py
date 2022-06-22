# Generated by Django 3.0.6 on 2020-07-25 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0014_auto_20200725_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='major',
        ),
        migrations.AddField(
            model_name='level',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collage_system.Major'),
        ),
    ]