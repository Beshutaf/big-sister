# Generated by Django 2.0.2 on 2018-02-06 20:09

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import members.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='first name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('address', models.CharField(max_length=200, verbose_name='physical address')),
                ('gender', enumfields.fields.EnumField(enum=members.models.Gender, max_length=1)),
                ('status', enumfields.fields.EnumField(default='a', enum=members.models.Status, max_length=1)),
                ('join_date', models.DateTimeField(verbose_name='date joined')),
                ('change_date', models.DateTimeField(verbose_name='date of last status update')),
                ('birth_date', models.DateTimeField(verbose_name='birth date')),
                ('neighborhood', models.CharField(blank=True, max_length=200, verbose_name='neighborhood')),
                ('student', models.CharField(blank=True, max_length=200, verbose_name='student status and degree')),
                ('age_group', models.CharField(blank=True, max_length=200, verbose_name='age group')),
                ('role', models.CharField(blank=True, max_length=200, verbose_name='usual role in shifts')),
                ('comments', models.CharField(blank=True, max_length=200, verbose_name='comments')),
                ('job', models.CharField(blank=True, max_length=200, verbose_name='profession')),
                ('education', models.CharField(blank=True, max_length=200, verbose_name='education')),
                ('skills', models.CharField(blank=True, max_length=200, verbose_name='skills')),
                ('num_children', models.PositiveSmallIntegerField(default=0, verbose_name='number of children')),
                ('joint_share_with', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Member')),
            ],
        ),
    ]