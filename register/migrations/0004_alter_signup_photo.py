# Generated by Django 3.2.3 on 2021-05-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20210522_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images/', verbose_name='Photo'),
        ),
    ]
