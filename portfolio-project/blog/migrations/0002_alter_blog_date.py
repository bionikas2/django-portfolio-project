# Generated by Django 4.1.4 on 2023-01-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
