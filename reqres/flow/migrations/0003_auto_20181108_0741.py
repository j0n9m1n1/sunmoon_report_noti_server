# Generated by Django 2.1.1 on 2018-11-07 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0002_auto_20181106_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='sub_name',
            new_name='old_reports',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='sub_report_old',
            new_name='old_subjects',
        ),
    ]