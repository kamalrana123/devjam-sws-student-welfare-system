# Generated by Django 3.2.3 on 2021-05-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_auto_20210517_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityquestion',
            name='stu_department',
            field=models.CharField(default='0000000', max_length=255, null=True),
        ),
    ]
