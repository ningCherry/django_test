# Generated by Django 2.2 on 2020-02-04 09:39

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('parea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booktest.AreaInfo')),
            ],
        ),
    ]
