# Generated by Django 5.2 on 2025-04-17 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_project_customer"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"get_latest_by": "created_on"},
        ),
    ]
