from django.db import models
from django.utils.translation import ugettext as _
from enumfields import Enum, EnumField


class Permission(Enum):
    ADMIN = 'A'
    MANAGER = 'M'
    SUPPLIER = 'S'
    REGULAR = 'R'


class AppUser(models.Model):
    class Meta:
        db_table = '"app_users"'
    member = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    permission = EnumField(Permission, max_length=1, name='permission', default=Permission.REGULAR)
    password_hash = models.CharField(_('password_hash'), max_length=128, blank=True)
