# Generated by Django 4.2.11 on 2024-04-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anaween', '0003_rename_name_enwaan_الأسم_rename_phone_enwaan_الرقم_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enwaan',
            name='الرقم',
            field=models.CharField(max_length=25),
        ),
    ]
