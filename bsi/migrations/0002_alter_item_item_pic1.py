# Generated by Django 3.2.3 on 2021-05-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_pic1',
            field=models.ImageField(blank=True, null=True, upload_to='bsi/images', verbose_name='pic1'),
        ),
    ]