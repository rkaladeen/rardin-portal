# Generated by Django 2.2.3 on 2019-08-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='priority',
            field=models.CharField(default='Unassigned', max_length=45),
        ),
    ]
