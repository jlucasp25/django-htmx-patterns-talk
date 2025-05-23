# Generated by Django 5.2 on 2025-04-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="phone",
        ),
        migrations.AddField(
            model_name="customer",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="customer",
            name="signup_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
