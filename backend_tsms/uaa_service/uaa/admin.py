from django.contrib import admin
from . models import Institute,User,TSMSUserRoles,TSMSUserPermissionsGroup,TSMSUserPermissions,TSMSUserRolesWithPermissions,TSMSUsersWithRoles
# from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Institute)
admin.site.register(User)
# admin.site.register(Permission)
@admin.register(TSMSUserRoles)
class TSMSUserRolesAdmin(admin.ModelAdmin):
    search_fields = [
        # 'primary_key',
        'role_unique_id',
        'role_name',
        'role_description',
        'role_createdby__username',
        'role_createddate'
    ]
    list_display = (
        # 'primary_key',
        'role_unique_id',
        'role_name',
        'role_description',
        'role_createdby',
        'role_createddate'
    )


@admin.register(TSMSUserPermissionsGroup)
class TSMSUserPermissionsGroupAdmin(admin.ModelAdmin):
    search_fields = [
        # 'primary_key',
        'permission_group_unique_id',
        'permission_group_name',
        'permission_group_description',
        'permission_group_createdby__username',
        'permission_group_createddate',
    ]
    list_display = (
        # 'primary_key',
        'permission_group_unique_id',
        'permission_group_name',
        'permission_group_description',
        'permission_group_createdby',
        'permission_group_createddate',
        'number_of_permissions'
    )

    def number_of_permissions(self, obj):
        from django.db.models import Count
        result = TSMSUserPermissions.objects.filter(permission_group=obj).count()
        return result


@admin.register(TSMSUserPermissions)
class TSMSUserPermissionsAdmin(admin.ModelAdmin):

    search_fields = [
        # 'primary_key',
        'permission_unique_id',
        'permission_name',
        'permission_code',
        'permission_group__permission_group_name',
        'permission_createdby__username',
        'permission_createddate'
    ]
    list_display = (
        # 'primary_key',
        'permission_unique_id',
        'permission_name',
        'permission_code',
        'permission_group',
        'permission_createdby',
        'permission_createddate'
    )


@admin.register(TSMSUserRolesWithPermissions)
class TSMSUserRolesWithPermissionsAdmin(admin.ModelAdmin):
    search_fields = [
        # 'primary_key',
        'role_with_permission_unique_id',
        'role_with_permission_role__role_name',
        'role_with_permission_permission__permission_name',
        'permission_read_only',
        'role_with_permission_createdby__username',
        'role_with_permission_createddate'
    ]
    list_display = (
        # 'primary_key',
        'role_with_permission_unique_id',
        'role_with_permission_role',
        'role_with_permission_permission',
        'permission_read_only',
        'role_with_permission_createdby',
        'role_with_permission_createddate'
    )


@admin.register(TSMSUsersWithRoles)
class TSMSUsersWithRolesAdmin(admin.ModelAdmin):
    search_fields = [
        # 'primary_key',
        'user_with_role_unique_id',
        'user_with_role_role__role_name',
        'user_with_role_user__username',
        'user_with_role_createdby__username',
        'user_with_role_createddate'
    ]
    list_display = (
        # 'primary_key',
        'user_with_role_unique_id',
        'user_with_role_role',
        'user_with_role_user',
        'user_with_role_createdby',
        'user_with_role_createddate'
    )
