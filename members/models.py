from django.db import models
from enumfields import Enum, EnumField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _


class Gender(Enum):
    FEMALE = 'f'
    MALE = 'm'
    OTHER = 'o'


class Status(Enum):
    ACTIVE = 'a'
    FROZEN = 'f'
    LEFT = 'l'


class Member(models.Model):
    first_name = models.CharField(_('first name'), max_length=200)
    last_name = models.CharField(_('last name'), max_length=200)
    email = models.EmailField(_('email address'))
    address = models.CharField(_('physical address'), max_length=200)
    phone_number = PhoneNumberField(_('phone number')),
    gender = EnumField(Gender, max_length=1, name=_('gender'))
    status = EnumField(Status, max_length=1, name=_('status'), default=Status.ACTIVE)
    join_date = models.DateTimeField(_('date joined'))
    change_date = models.DateTimeField(_('date of last status update'))
    birth_date = models.DateTimeField(_('birth date'))
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
