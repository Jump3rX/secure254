# Generated by Django 3.1.7 on 2022-01-22 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('secure254app', '0005_auto_20220122_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='occurence_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]