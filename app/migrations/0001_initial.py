# Generated by Django 2.0.3 on 2018-03-06 14:54

import app.models
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', enumfields.fields.EnumField(default='R', enum=app.models.Permission, max_length=1)),
                ('password_hash', models.CharField(blank=True, max_length=128, verbose_name='password_hash')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
            options={
                'db_table': '"app_users"',
            },
        ),
    ]
