# Generated by Django 5.1.1 on 2024-12-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0005_recurringpayment"),
    ]

    operations = [
        migrations.AddField(
            model_name="recurringpayment",
            name="destination",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]