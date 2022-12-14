# Generated by Django 3.1.1 on 2022-10-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_remove_banner_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': 'Banner'},
        ),
        migrations.AddField(
            model_name='banner',
            name='alt_text',
            field=models.CharField(blank=True, default='Banner', max_length=255, verbose_name='Alt Text'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(help_text='Recommended Size: 1200x300 Pixels<br>Width: 1200px, Height: 300px', upload_to='course_page_banner_uploads/'),
        ),
    ]
