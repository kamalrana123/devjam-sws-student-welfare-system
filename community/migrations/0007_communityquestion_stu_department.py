# Generated by Django 3.2.3 on 2021-05-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_communityanswer_communityquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityquestion',
            name='stu_department',
            field=models.CharField(default='0000000', max_length=255),
        ),
    ]
