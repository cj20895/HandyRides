# Generated by Django 4.2.10 on 2024-03-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rides", "0002_person_accessible_person_last_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="gas_mileage",
            field=models.IntegerField(default=0),
        ),
    ]