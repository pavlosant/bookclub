# Generated by Django 4.2.17 on 2024-12-16 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookclub", "0005_alter_meeting_meeting_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="chosen_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book_chooser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
