# Generated by Django 3.1.3 on 2020-11-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=256, verbose_name='8E5407D80099862B36F4DB644E0B5CD2'),
        ),
    ]
