# Generated by Django 5.2 on 2025-04-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_customer_phone_customer_image_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="name",
            new_name="title",
        ),
        migrations.AddField(
            model_name="project",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
