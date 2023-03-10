# Generated by Django 4.1.3 on 2022-12-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_beritamodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeritaApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athor', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('urlToImage', models.ImageField(upload_to='')),
                ('publishedAt', models.DateTimeField(auto_now_add=True)),
                ('cotent', models.TextField()),
            ],
        ),
    ]
