# Generated by Django 5.0 on 2023-12-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_profile', models.URLField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
