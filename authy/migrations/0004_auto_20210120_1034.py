# Generated by Django 3.1.5 on 2021-01-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_auto_20210119_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_info',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
