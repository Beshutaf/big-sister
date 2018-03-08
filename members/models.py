from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from enumfields import Enum, EnumField
from phonenumber_field.modelfields import PhoneNumberField


class Gender(Enum):
    FEMALE = 'f'
    MALE = 'm'
    OTHER = 'o'


class Status(Enum):
    ACTIVE = 'a'
    FROZEN = 'f'
    LEFT = 'l'


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(_('physical address'), max_length=200, blank=True)
    phone_number = PhoneNumberField(_('phone number'), blank=True),
    gender = EnumField(Gender, max_length=1, name=_('gender'), blank=True)
    status = EnumField(Status, max_length=1, name=_('status'), default=Status.ACTIVE)
    join_date = models.DateTimeField(_('date joined'), blank=True)
    change_date = models.DateTimeField(_('date of last status update'), blank=True)
    birth_date = models.DateTimeField(_('birth date'), blank=True)
    joint_share_with = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True)
    neighborhood = models.CharField(_('neighborhood'), max_length=200, blank=True)
    student = models.CharField(_('student status and degree'), max_length=200, blank=True)
    age_group = models.CharField(_('age group'), max_length=200, blank=True)
    role = models.CharField(_('usual role in shifts'), max_length=200, blank=True)
    comments = models.CharField(_('comments'), max_length=200, blank=True)
    job = models.CharField(_('profession'), max_length=200, blank=True)
    education = models.CharField(_('education'), max_length=200, blank=True)
    skills = models.CharField(_('skills'), max_length=200, blank=True)
    num_children = models.PositiveSmallIntegerField(_('number of children'), default=0)


@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    del sender, kwargs
    if created:
        Member.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_member(sender, instance, **kwargs):
    del sender, kwargs
    instance.member.save()
