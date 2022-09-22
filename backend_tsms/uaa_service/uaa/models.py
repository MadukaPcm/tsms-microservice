from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import RegexValidator
import uuid

# Create your models here.
class Institute(models.Model):
    id =    models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    # createdBy_id = models.CharField(max_length=100)

    reg_no = models.CharField(max_length=20,unique=True)
    institute_name = models.CharField(max_length=50)
    institute_abbreviation = models.CharField(max_length=20)
    institute_description = models.TextField(max_length=40)
    institute_email = models.EmailField(max_length=30,unique=True)
    institute_location = models.CharField(max_length=50)
    post_office_address = models.CharField(max_length=20,unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.institute_abbreviation


# from uuidfield import UUIDField
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique = True)
    institution_id = models.ForeignKey(Institute,blank=True, null=True,on_delete=models.SET_NULL)
    employ_id = models.CharField(max_length=20, null=True, blank=True,unique = True)
    nida_no = models.CharField(max_length=25, null=True, blank=True, unique=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+255-000-000-000' ")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
      return "{}".format(self.email)


class TSMSUserRoles(models.Model):
    # id = models.AutoField(primary_key=True)
    role_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    institute = models.ForeignKey(Institute,on_delete=models.DO_NOTHING)
    role_name = models.CharField(default='', max_length=1600)
    role_description = models.CharField(default='', max_length=1600)
    role_createdby = models.ForeignKey(User, related_name='user_role_creator', on_delete=models.CASCADE)
    role_createddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.role_name)

    def get_role_permissions(self):
        return self.user_role_with_permission_role.all()

    class Meta:
        db_table = 'tsms_user_roles'
        ordering = ['-role_createddate']
        verbose_name_plural = "User Roles"


#these permissionsGroup model_name are binded to the ui:
class TSMSUserPermissionsGroup(models.Model):
    # primary_key = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=True)
    permission_group_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    permission_group_name = models.CharField(default='', max_length=1600)
    permission_group_description = models.CharField(default='', max_length=600, null=True)
    permission_group_createdby = models.ForeignKey(User, related_name='permission_group_creator',
                                                   on_delete=models.CASCADE)
    permission_group_createddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.permission_group_name, self.permission_group_description)

    class Meta:
        db_table = 'tsms_user_permissions_group'
        ordering = ['-permission_group_createddate']
        verbose_name_plural = "Permission Groups"


#these permissionsGroup model_name are binded to the ui:
class TSMSUserPermissions(models.Model):
    # primary_key = models.AutoField(primary_key=True)
    permission_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    permission_name = models.CharField(default='', max_length=1600)
    permission_code = models.CharField(default='', max_length=1600)
    permission_group = models.ForeignKey(TSMSUserPermissionsGroup, related_name='permission_group',
                                         on_delete=models.CASCADE, null=True)
    permission_createdby = models.ForeignKey(User, related_name='user_permission_creator', on_delete=models.CASCADE)
    permission_createddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.permission_name, self.permission_group)

    class Meta:
        db_table = 'tsms_user_permissions'
        ordering = ['-permission_createddate']
        verbose_name_plural = "User Permissions"


class TSMSUserRolesWithPermissions(models.Model):
    # primary_key = models.AutoField(primary_key=True)
    role_with_permission_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    role_with_permission_role = models.ForeignKey(TSMSUserRoles, related_name='user_role_with_permission_role',
                                                  on_delete=models.CASCADE)
    role_with_permission_permission = models.ForeignKey(TSMSUserPermissions,
                                                        related_name='user_role_with_permission_permission',
                                                        on_delete=models.CASCADE)
    permission_read_only = models.BooleanField(default=True)
    role_with_permission_createdby = models.ForeignKey(User, related_name='user_role_with_permission_creator',
                                                       on_delete=models.CASCADE)
    role_with_permission_createddate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'dtp_user_role_with_permissions'
        ordering = ['-role_with_permission_createddate']
        verbose_name_plural = "Roles with Permissions"


class TSMSUsersWithRoles(models.Model):
    # primary_key = models.AutoField(primary_key=True)
    user_with_role_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    user_with_role_role = models.ForeignKey(TSMSUserRoles, related_name='user_role_name', on_delete=models.CASCADE)
    user_with_role_user = models.ForeignKey(User, related_name='role_user', on_delete=models.CASCADE)
    user_with_role_createdby = models.ForeignKey(User, related_name='user_with_role_creator', on_delete=models.CASCADE)
    user_with_role_createddate = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'tsms_user_with_roles'
        ordering = ['-user_with_role_createddate']
        verbose_name_plural = "Users with Roles"


# Create your models here.

