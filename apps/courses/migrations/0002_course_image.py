# Generated by Django 3.1.1 on 2022-10-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='course_image_uploads/'),
        ),
    ]
