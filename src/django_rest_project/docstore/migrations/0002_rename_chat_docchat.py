# Generated by Django 4.2.5 on 2023-09-13 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chat',
            new_name='DocChat',
        ),
    ]
