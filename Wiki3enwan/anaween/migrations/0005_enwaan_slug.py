# Generated by Django 4.2.11 on 2024-04-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anaween', '0004_alter_enwaan_الرقم'),
    ]

    operations = [
        migrations.AddField(
            model_name='enwaan',
            name='slug',
            field=models.SlugField(default='default', unique=True),
        ),
    ]