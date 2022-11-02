# Generated by Django 3.2 on 2022-10-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_remove_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='publish',
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(blank=True, default='4 Weeks', help_text='Ex.: 4 Weeks', max_length=255, verbose_name='Course Duration'),
        ),
        migrations.AlterField(
            model_name='course',
            name='rewards',
            field=models.BooleanField(blank=True, default=True, verbose_name='Enroll & Win Rewards'),
        ),
    ]