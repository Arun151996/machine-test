# Generated by Django 4.0.1 on 2022-05-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addstudent',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]