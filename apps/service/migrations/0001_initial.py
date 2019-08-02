# Generated by Django 2.2.3 on 2019-08-01 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_by', models.CharField(max_length=45)),
                ('t_type', models.CharField(max_length=45)),
                ('short_desc', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('ts', models.TextField()),
                ('status', models.CharField(default='Not Acknowledged', max_length=45)),
                ('assign_to', models.CharField(default='Unassigned', max_length=45)),
                ('tech_note', models.TextField(default='')),
                ('res_note', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('viewed_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_ticket', to='main.Employee')),
                ('last_update', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_update_ticket', to='main.Employee')),
                ('last_view', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_view_ticket', to='main.Employee')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Employee')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Message')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Employee')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Ticket')),
            ],
        ),
    ]
