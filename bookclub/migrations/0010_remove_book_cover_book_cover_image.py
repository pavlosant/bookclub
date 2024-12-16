# Generated by Django 4.2.17 on 2024-12-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookclub", "0009_alter_book_cover"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="cover",
        ),
        migrations.AddField(
            model_name="book",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="book_covers/"),
        ),
    ]