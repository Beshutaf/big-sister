# Generated by Django 2.0.3 on 2018-03-08 13:44

from django.db import migrations, models
import enumfields.fields
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180308_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='physical address'),
        ),
        migrations.AlterField(
            model_name='member',
            name='age_group',
            field=models.CharField(max_length=200, null=True, verbose_name='age group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateTimeField(null=True, verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='change_date',
            field=models.DateTimeField(null=True, verbose_name='date of last status update'),
        ),
        migrations.AlterField(
            model_name='member',
            name='comments',
            field=models.CharField(max_length=200, null=True, verbose_name='comments'),
        ),
        migrations.AlterField(
            model_name='member',
            name='education',
            field=models.CharField(max_length=200, null=True, verbose_name='education'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=enumfields.fields.EnumField(enum=members.models.Gender, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='job',
            field=models.CharField(max_length=200, null=True, verbose_name='profession'),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(null=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='member',
            name='neighborhood',
            field=models.CharField(max_length=200, null=True, verbose_name='neighborhood'),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(max_length=200, null=True, verbose_name='usual role in shifts'),
        ),
        migrations.AlterField(
            model_name='member',
            name='skills',
            field=models.CharField(max_length=200, null=True, verbose_name='skills'),
        ),
        migrations.AlterField(
            model_name='member',
            name='student',
            field=models.CharField(max_length=200, null=True, verbose_name='student status and degree'),
        ),
    ]
