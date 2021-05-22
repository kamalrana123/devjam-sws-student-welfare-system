# Generated by Django 3.2.3 on 2021-05-22 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_signup_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='course',
            field=models.CharField(choices=[('BTech', 'BTech'), ('MTech', 'MTech'), ('MCA', 'MCA'), ('MSc', 'MSc'), ('MBA', 'MBA'), ('Ph.D', 'Ph.D')], max_length=20, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images', verbose_name='Photo'),
        ),
    ]
