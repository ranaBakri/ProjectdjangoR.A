# Generated by Django 4.0.5 on 2022-10-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_delete_book_event_alter_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='available_seats',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='booked_seats',
            field=models.PositiveIntegerField(),
        ),
    ]
