# Generated by Django 3.0.5 on 2020-08-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0005_auto_20200731_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumedata',
            name='post_as',
            field=models.TextField(default='["Not answered", "Not answered", "Not answered", "Not answered"]'),
        ),
    ]
