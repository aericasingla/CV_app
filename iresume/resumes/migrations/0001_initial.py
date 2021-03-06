# Generated by Django 3.0.5 on 2020-07-21 22:20

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import resumes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.TextField(null=True)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.IntegerField(max_length=12, null=True)),
                ('personal_profile', models.TextField(null=True)),
                ('work_experience', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(verbose_name=resumes.models.Experience), null=True, size=None)),
                ('key_skills', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, null=True, size=None)),
                ('education', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(verbose_name=resumes.models.Education), null=True, size=None)),
            ],
        ),
    ]
