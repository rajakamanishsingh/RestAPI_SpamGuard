# Generated by Django 4.2.3 on 2023-07-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_detection_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_spam',
            field=models.BooleanField(default=False),
        ),
    ]