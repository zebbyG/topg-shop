# Generated by Django 4.2 on 2023-06-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='assets/zebbyG', height_field='image_height', upload_to='user_profiles/', width_field='image_width'),
        ),
    ]
