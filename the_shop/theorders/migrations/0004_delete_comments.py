# Generated by Django 4.2.3 on 2023-08-08 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theorders', '0003_alter_comments_date_added'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]