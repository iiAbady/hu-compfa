# Generated by Django 3.0.6 on 2020-09-19 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_teacher_teacher_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorials_name', models.CharField(max_length=50)),
                ('tutorials_image', models.ImageField(null=True, upload_to='tutorials')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialsTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('tutorials_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tutorials_name', models.CharField(max_length=300)),
                ('videos_number', models.IntegerField()),
                ('tutorials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Tutorials')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialsVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='VideoTutorials')),
                ('video_name', models.CharField(blank=True, max_length=300, null=True)),
                ('tutorialsteacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.TutorialsTeacher')),
            ],
        ),
    ]
