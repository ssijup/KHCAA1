# Generated by Django 4.2.2 on 2023-07-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp1', '0002_userdetails_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_entrolment_id',
            field=models.CharField(max_length=20),
        ),
    ]
