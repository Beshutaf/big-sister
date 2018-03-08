# Generated by Django 2.0.3 on 2018-03-08 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import members.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_name',
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
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
            field=models.DateTimeField(null=True, verbose_name='תאריך הצטרפות'),
        ),
        migrations.AlterField(
            model_name='member',
            name='joint_share_with',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='joint_share', to='members.Member'),
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
