import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

from graphene_django import DjangoObjectType
from graphene_federation import build_schema, extend, external,key

from graphql_jwt.shortcuts import get_token, create_refresh_token

from uaa.models import Institute,User,TSMSUserRoles,TSMSUserPermissionsGroup,TSMSUserPermissions,TSMSUserRolesWithPermissions,TSMSUsersWithRoles

from . producer import publish


@key(fields='id')
class TSMSUserObject(graphene.ObjectType):
    id=graphene.String(required=True)
    first_name=graphene.String(required=True)
    last_name=graphene.String(required=True)

    def __resolve_reference(self, info, **kwargs):
        user_data=User.objects.filter(id=self.id).first()
        return TSMSUserObject(
            user_data.id,
            user_data.first_name,
            user_data.last_name,
        )


@key(fields='id')
class InstituteType(DjangoObjectType):
    class Meta:
        model = Institute

class UserType(DjangoObjectType):
    class Meta:
        model = User

class TSMSUserRolesType(DjangoObjectType):
    class Meta:
        model = TSMSUserRoles

class TSMSUserPermissionsGroupType(DjangoObjectType):
    class Meta:
        model = TSMSUserPermissionsGroup

class TSMSUserPermissionsType(graphene.ObjectType):
    permission_unique_id=graphene.String(required=True)
    permission_name=graphene.String(required=True)
    permission_code=graphene.String(required=True)

class TSMSUserRolesWithPermissionsType(DjangoObjectType):
    class Meta:
        model = TSMSUserRolesWithPermissions

class TSMSUsersWithRolesType(DjangoObjectType):
    class Meta:
        model = TSMSUsersWithRoles


#============================================================================================================================================================ institute mutation......================================================================
class CreateInstitute(graphene.Mutation):
    institute = graphene.Field(InstituteType)

    class Arguments:
        # createdBy_id = graphene.String(required=True)
        reg_no = graphene.String(required=True)
        institute_name = graphene.String(required=True)
        institute_abbreviation = graphene.String(required=True)
        institute_description = graphene.String(required=True)
        institute_email = graphene.String(required=True)
        institute_location = graphene.String(required=True)
        post_office_address = graphene.String(required=True)

    def mutate(self,info,reg_no,institute_name,institute_abbreviation,institute_description,institute_email,institute_location,post_office_address):
        institute_data = Institute(
        reg_no=reg_no,
        institute_name=institute_name,
        institute_abbreviation=institute_abbreviation,
        institute_description=institute_description,
        institute_email=institute_email,
        institute_location=institute_location,
        post_office_address=post_office_address)

        institute_data.save()
        # publish()
        return CreateInstitute(institute=institute_data)

class UpdateInstituteMutation(graphene.Mutation):
    update_institute = graphene.Field(InstituteType)

    class Arguments:
        id = graphene.ID()
        reg_no = graphene.String(required=True)
        institute_name = graphene.String(required=True)
        institute_abbreviation = graphene.String(required=True)
        institute_description = graphene.String(required=True)
        institute_email = graphene.String(required=True)
        institute_location = graphene.String(required=True)
        post_office_address = graphene.String(required=True)


    @classmethod
    def mutate(cls,root,info,id,reg_no,institute_name,institute_abbreviation,institute_description,institute_email,institute_location,post_office_address):
        update_institute = Institute.objects.get(id=id)
        update_institute.reg_no = reg_no
        update_institute.institute_name = institute_name
        update_institute.institute_abbreviation = institute_abbreviation
        update_institute.institute_description = institute_description
        update_institute.institute_email = institute_email
        update_institute.institute_location = institute_location
        update_institute.post_office_address = post_office_address

        update_institute.save()

        return UpdateInstituteMutation(update_institute = update_institute)

class DeleteInstituteMutation(graphene.Mutation):
    delete_institute = graphene.Field(InstituteType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_institute = Institute.objects.get(id=id)
        delete_institute.delete()

        return DeleteInstituteMutation(delete_institute=delete_institute)


#============================================================================================================================================================ create_user mutation......================================================================

class UserCreateMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        institution_id = graphene.String(required=True)
        employ_id = graphene.String(required=True)
        nida_no = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        password1 = graphene.String(required=True)
        # password2 = graphene.String(required=True)

    @staticmethod
    def mutate(root, info,first_name,last_name,email,username,institution_id,employ_id,nida_no,phone_number,password1):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist as e:
            user = None

        if user:
            raise Exception('Email Already Exists!')
        else:
            user_instance = User(first_name=first_name,last_name=last_name,email=email,username=username,employ_id=employ_id,nida_no=nida_no,phone_number=phone_number)
            # user_instance.user.email = input.email
            user_instance.set_password(password1)
            # user_instance.user.is_applicant = True
            pk1 = Institute.objects.get(id=institution_id)
            user_instance.institution_id = pk1
            data = user_instance.save()

            #Adding default role to the first created user
            user_id = User.objects.filter(email=email)[0]
            role_id = TSMSUserRoles.objects.filter(role_name="user").first()
            print(role_id)
            TSMSUsersWithRoles.objects.create(user_with_role_user=user_id, user_with_role_role=role_id, user_with_role_createdby=user_id)

            token = get_token(user_instance)
            refresh_token = create_refresh_token(user_instance)

            return UserCreateMutation(user=user_instance,
                                    token=token,
                                    refresh_token=refresh_token,
                                    success=True)


#============================================================================================================================================================ General mutation class......================================================================
class DataMutation(graphene.ObjectType):
    # mutation for User model -uaa

    # mutation for instititute model
    createInstitute = CreateInstitute.Field()
    updateInstitute = UpdateInstituteMutation.Field()
    deleteInstitute = DeleteInstituteMutation.Field()

    #mutation for creating user custom user model
    create_account =UserCreateMutation.Field()
    # register = mutations.Register.Field()

    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()

    # update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class DataQuery(graphene.ObjectType):
    all_institute = graphene.List(InstituteType)
    all_users = graphene.List(UserType)
    get_users_list = graphene.List(TSMSUserObject)

    all_mypermissions = graphene.List(TSMSUserPermissionsType)

    def resolve_all_institute(root,info):
        # publish('institute_list',Institute.objects.all())
        publish()
        return  Institute.objects.all()

    def resolve_all_users(root,info):
        return  User.objects.all()

    def resolve_all_mypermissions(root,info,**kwargs):
        #returns permissions for the cureently authenticated user
        user = info.context.user
        if not user.is_authenticated:
            return 401
        else:
            userRole = TSMSUsersWithRoles.objects.get(user_with_role_user=user)
            print(userRole.user_with_role_role)
            rolePermissions = TSMSUserRolesWithPermissions.objects.filter(role_with_permission_role=userRole.user_with_role_role)
            permissions = []
            for rolePermission in rolePermissions:
                permissions.append(rolePermission.role_with_permission_permission)
            # permissions=TSMSUserPermissions.objects.all()
            # print(permissions)
            return permissions


class Mutation(DataMutation,graphene.ObjectType):
    pass

class Query(DataQuery,UserQuery, MeQuery,graphene.ObjectType):
    pass

schema = build_schema(DataQuery,DataMutation)


# mutation {
#   register(
#     email: "new_user@email.com",
#     username: "new_user",
#     password1: "123456",
#     password2: "123456",
#   ) {
#     success,
#     errors,
#     token,
#     refreshToken
#   }
# }

# mutation {
#   register(
#     email: "new_user@email.com",
#     username: "new_user",
#     password1: "supersecretpassword",
#     password2: "supersecretpassword",
#   ) {
#     success,
#     errors,
#     token,
#     refreshToken
#   }
# }

# query {
#   users (last: 1){
#     edges {
#       node {
#         id,
#         username,
#         email,
#         isActive,
#         archived,
#         verified,
#         secondaryEmail
#       }
#     }
#   }
# }

# query {
#   user (id: "<USER ID>"){
#     username,
#     verified
#   }
# }

# mutation {
#   verifyAccount(token: "YOUR TOKEN HERE") {
#     success,
#     errors
#   }
# }

#==============================try to login
# mutation {
#   tokenAuth(username: "new_user", password: "supersecretpassword") {
#     success,
#     errors,
#     unarchiving,
#     token,
#     refreshToken,
#     unarchiving,
#     user {
#       id,
#       username,
#     }
#   }
# }

#==============================dealing with token auth,, using update mutation class......
#On the headers pane, create a new header:
# name: Authorization
# value: JWT <TOKEN FROM THE LOGIN>

# mutation {
#   updateAccount(
#     firstName: "Joe"
#   ) {
#     success,
#     errors
#   }
# }

# query {
#   user (id: "<USER ID>"){
#     username,
#     firstName
#   }
# }

# mutation {
#   updateInstitute(
#     id: "76ac44b8-dfc9-42dc-8ec2-9843f9cedc17",
#     regNo: "34536h",
#     instituteName: "egoverment",
#     instituteAbbreviation: "madukapcm",
#     instituteDescription: "serikali mtandao",
#     instituteEmail: "ega@gmail.com",
#     instituteLocation: "Dodoma",
#     postOfficeAddress: "123 abc")
#   {
#     updateInstitute{
#       id
#       regNo
#       instituteName
#       instituteAbbreviation
#     }
#   }
# }


