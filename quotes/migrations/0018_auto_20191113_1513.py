# Generated by Django 2.2.5 on 2019-11-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0017_auto_20191113_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='quote_pics', verbose_name='Quote Imge'),
        ),
    ]
