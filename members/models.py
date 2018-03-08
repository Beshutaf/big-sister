import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.utils import IntegrityError
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
    address = models.CharField(_('physical address'), max_length=200, null=True)
    phone_number = PhoneNumberField(_('phone number'), null=True),
    gender = EnumField(Gender, max_length=1, name=_('gender'), null=True)
    status = EnumField(Status, max_length=1, name=_('status'), default=Status.ACTIVE)
    join_date = models.DateTimeField(_('date joined'), null=True)
    change_date = models.DateTimeField(_('date of last status update'), null=True)
    birth_date = models.DateTimeField(_('birth date'), null=True)
    joint_share_with = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True)
    neighborhood = models.CharField(_('neighborhood'), max_length=200, null=True)
    student = models.CharField(_('student status and degree'), max_length=200, null=True)
    age_group = models.CharField(_('age group'), max_length=200, null=True)
    role = models.CharField(_('usual role in shifts'), max_length=200, null=True)
    comments = models.CharField(_('comments'), max_length=200, null=True)
    job = models.CharField(_('profession'), max_length=200, null=True)
    education = models.CharField(_('education'), max_length=200, null=True)
    skills = models.CharField(_('skills'), max_length=200, null=True)
    num_children = models.PositiveSmallIntegerField(_('number of children'), default=0)

    @classmethod
    def create_all(cls, members, status=Status.ACTIVE):
        for member in members:
            try:
                gender, first_name, last_name, phone_number, email, *_ = member
            except ValueError as e:
                raise ValueError(member) from e
            try:
                user = User.objects.create_user(" ".join((first_name, last_name)), email)
            except IntegrityError as e:
                logging.warning(e, member)
                continue
            user.first_name = first_name
            user.last_name = last_name
            user.member.phone_number = phone_number
            user.member.gender = {"אדון": Gender.MALE, "גברת": Gender.FEMALE}.get(gender, Gender.OTHER)
            user.member.status = status
            user.save()


@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    del sender, kwargs
    if created:
        Member.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_member(sender, instance, **kwargs):
    del sender, kwargs
    instance.member.save()
