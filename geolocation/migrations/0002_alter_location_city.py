# Generated by Django 4.2.7 on 2024-05-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geolocation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
