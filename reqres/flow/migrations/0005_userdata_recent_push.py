# Generated by Django 2.1.1 on 2018-11-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0004_auto_20181108_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='recent_push',
            field=models.CharField(default='', max_length=200),
        ),
    ]