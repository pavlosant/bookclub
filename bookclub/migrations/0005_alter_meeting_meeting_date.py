# Generated by Django 4.2.17 on 2024-12-16 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("bookclub", "0004_alter_meeting_meeting_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="meeting_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
