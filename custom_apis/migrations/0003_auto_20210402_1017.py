# Generated by Django 3.1.4 on 2021-04-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_apis', '0002_auto_20210107_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyotp',
            name='phone',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
