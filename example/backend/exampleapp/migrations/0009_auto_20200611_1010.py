# Generated by Django 3.0.6 on 2020-06-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleapp', '0008_auto_20200611_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateField(blank=True, verbose_name='published_at'),
        ),
    ]
