# Generated by Django 4.2 on 2023-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0008_brand_brand_image_brand_image_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_image',
            field=models.ImageField(default='shoes/topg-logo.gif', height_field='image_height', upload_to='brand-logos/', width_field='image_width'),
        ),
    ]