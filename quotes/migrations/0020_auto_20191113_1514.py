# Generated by Django 2.2.5 on 2019-11-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0019_auto_20191113_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature',
            field=models.BooleanField(default=False, verbose_name='Feature Quote'),
        ),
    ]