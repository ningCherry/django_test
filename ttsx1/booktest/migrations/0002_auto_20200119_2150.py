# Generated by Django 3.0.2 on 2020-01-19 13:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BooInfo',
            new_name='BookInfo',
        ),
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('books1', django.db.models.manager.Manager()),
            ],
        ),
    ]
