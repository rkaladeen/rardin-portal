# Generated by Django 2.2.3 on 2019-08-05 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default='Male', max_length=10),
            preserve_default=False,
        ),
    ]
