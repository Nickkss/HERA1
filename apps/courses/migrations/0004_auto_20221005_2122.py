# Generated by Django 3.1.1 on 2022-10-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20221005_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Video Title'),
        ),
    ]