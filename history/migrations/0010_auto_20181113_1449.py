# Generated by Django 2.1.3 on 2018-11-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0009_auto_20181113_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='date',
            field=models.DateTimeField(default='2018-11-13 14:49'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='date',
            field=models.DateTimeField(default='2018-11-13 14:49'),
        ),
        migrations.AlterField(
            model_name='personalmessage',
            name='date',
            field=models.DateTimeField(default='2018-11-13 14:49'),
        ),
    ]
