# Generated by Django 3.1.1 on 2022-10-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'Admin'), (2, 'Student')], default=2, help_text='Choose User Role', verbose_name='Role'),
        ),
    ]
