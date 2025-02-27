# Generated by Django 3.1.5 on 2021-06-20 23:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('abbreviated_name', models.CharField(max_length=50, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=500, null=True)),
                ('meta', models.TextField(blank=True, null=True)),
                ('exam_level', models.CharField(max_length=150, null=True)),
                ('conducting_body', models.CharField(max_length=255, null=True)),
                ('website', models.CharField(max_length=255, null=True)),
                ('tentative_date', models.CharField(max_length=100, null=True)),
                ('basic_eligibility', models.CharField(max_length=100, null=True)),
                ('about', models.TextField(null=True)),
                ('important_detais', models.JSONField(null=True)),
                ('cutoff', models.JSONField(null=True)),
                ('eligibility', models.TextField(null=True)),
                ('application_form', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('is_top', models.BooleanField(default=False, null=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
