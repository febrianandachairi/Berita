# Generated by Django 4.1.3 on 2022-12-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
