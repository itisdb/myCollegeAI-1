# Generated by Django 3.1.4 on 2020-12-27 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201227_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpverification',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
