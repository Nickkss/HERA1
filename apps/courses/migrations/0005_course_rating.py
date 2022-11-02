# Generated by Django 3.1.1 on 2022-10-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20221005_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
    ]