# Generated by Django 2.2.3 on 2019-08-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user_type',
            field=models.CharField(default='User', max_length=45),
        ),
    ]
