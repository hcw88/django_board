# Generated by Django 3.2.7 on 2021-10-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20211001_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='c_time',
            field=models.DateTimeField(null=True),
        ),
    ]
