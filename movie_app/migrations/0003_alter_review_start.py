# Generated by Django 5.1.4 on 2025-01-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_review_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='start',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, null=True),
        ),
    ]
