# Generated by Django 3.0.14 on 2022-10-18 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['timestamp'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]