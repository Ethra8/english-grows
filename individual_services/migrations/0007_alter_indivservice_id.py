# Generated by Django 5.1 on 2024-11-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individual_services', '0006_alter_indivservice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indivservice',
            name='id',
            field=models.CharField(editable=False, max_length=2, primary_key=True, serialize=False, unique=True),
        ),
    ]