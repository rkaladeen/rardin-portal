# Generated by Django 2.2.3 on 2019-08-01 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('department', models.CharField(default='', max_length=45)),
                ('job_title', models.CharField(default='', max_length=45)),
                ('telephone', models.CharField(max_length=11)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('job_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('street_number', models.IntegerField()),
                ('street_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_store', to='main.Store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user_store', to='main.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Dept_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_dept', to='main.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user_dept', to='main.Employee')),
            ],
        ),
    ]
