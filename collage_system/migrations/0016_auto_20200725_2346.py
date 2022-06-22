# Generated by Django 3.0.6 on 2020-07-25 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collage_system', '0015_auto_20200725_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terms',
            name='levels',
        ),
        migrations.AddField(
            model_name='terms',
            name='levels',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collage_system.Level'),
        ),
    ]