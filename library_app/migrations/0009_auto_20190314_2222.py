# Generated by Django 2.1.7 on 2019-03-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0008_remove_book_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, default=None, max_length=750, null=True, verbose_name='Author Biography'),
        ),
    ]
