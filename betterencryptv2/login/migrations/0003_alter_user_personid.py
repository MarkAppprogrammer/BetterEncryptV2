# Generated by Django 5.0.7 on 2024-08-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_uid_user_personid_remove_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personid',
            field=models.IntegerField(null=True),
        ),
    ]