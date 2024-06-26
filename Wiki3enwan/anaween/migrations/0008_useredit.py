# Generated by Django 4.2.11 on 2024-04-10 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anaween', '0007_alter_enwaan_الرقم'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEdit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('enwaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anaween.enwaan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
