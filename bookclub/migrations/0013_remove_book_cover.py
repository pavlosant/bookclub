# Generated by Django 4.2.17 on 2024-12-19 13:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookclub", "0012_book_cover_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="cover",
        ),
    ]