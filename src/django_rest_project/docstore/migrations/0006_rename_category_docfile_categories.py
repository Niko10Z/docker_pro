# Generated by Django 4.2.5 on 2023-09-15 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docstore', '0005_docchat_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docfile',
            old_name='category',
            new_name='categories',
        ),
    ]
