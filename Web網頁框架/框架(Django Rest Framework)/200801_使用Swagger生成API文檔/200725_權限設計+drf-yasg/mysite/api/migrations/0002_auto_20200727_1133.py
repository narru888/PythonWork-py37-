# Generated by Django 2.0 on 2020-07-27 03:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=32)),
                ('method', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('push_at', models.DateTimeField(default=datetime.datetime.now)),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Permission')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Role')),
            ],
        ),
        migrations.AlterField(
            model_name='userrole',
            name='push_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(through='api.RolePermission', to='api.Permission'),
        ),
    ]
