# Generated by Django 3.2 on 2022-10-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_alter_course_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(blank=True, default='English', max_length=255, verbose_name='Language'),
        ),
    ]
