# Generated by Django 5.1 on 2024-10-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_email',
            field=models.EmailField(blank=True, max_length=80, null=True),
        ),
    ]