# Generated by Django 2.1.7 on 2019-03-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_auto_20190310_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(blank=True, height_field='30px', null=True, upload_to='static/library_app/images/book_covers', verbose_name='Book Cover', width_field='30px'),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, default=None, help_text='Biography', max_length=750, null=True, verbose_name='Author Biography'),
        ),
    ]
