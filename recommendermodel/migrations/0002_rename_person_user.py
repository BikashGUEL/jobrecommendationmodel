# Generated by Django 5.0.4 on 2024-04-22 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recommendermodel", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Person",
            new_name="User",
        ),
    ]
