import graphene
from graphene_django import DjangoObjectType
from graphene_federation import build_schema, extend, external,key

from payment.models import PaymentMethod,Payment
from report.models import TrainingAttendance
from training.models import Venue,AudienceCategory,Training,TrainingApplication


@key(fields='id')
class PaymentMethodType(DjangoObjectType):
    class Meta:
        model = PaymentMethod

class PaymentType(DjangoObjectType):
    class Meta:
        model = Payment

class TrainingAttendanceType(DjangoObjectType):
    class Meta:
        model = TrainingAttendance

class VenueType(DjangoObjectType):
    class Meta:
        model = Venue


class AudienceCategoryType(DjangoObjectType):
    class Meta:
        model = AudienceCategory

class TrainingType(DjangoObjectType):
    class Meta:
        model = Training

class TrainingApplicationType(DjangoObjectType):
    class Meta:
        model = TrainingApplication

#============================================================================================================================================================ payments methods mutation......================================================================
class CreatePaymentMethodMutation(graphene.Mutation):
    payment_method = graphene.Field(PaymentMethodType)

    class Arguments:
        payment_method= graphene.String(required=True)
        institute_id= graphene.String()
        createdBy_id= graphene.String()

    # def mutate(self,info,payment_method,institute_id):
    #     payment_method_data = PaymentMethod(payment_method = payment_method)
    #     data = Institute.objects.get(id=institute_id)
    #     payment_method_data.institute_id = data

    #     payment_method_data.save()
    #     return CreatePaymentMethodMutation(payment_method=payment_method_data)

    def mutate(self,info,payment_method,institute_id,createdBy_id):
        payment_method_data = PaymentMethod(
            payment_method = payment_method,
            institute_id = institute_id,
            createdBy_id = createdBy_id,
            )

        payment_method_data.save()
        return CreatePaymentMethodMutation(payment_method=payment_method_data)

# class UpdatePaymentMethodMutation(graphene.Mutation):
#     update_payment_methd = graphene.Field(PaymentMethodType)

#     class Arguments:
#         id = graphene.ID()
#         payment_method = graphene.String(required=True)
#         institute_id  =  graphene.String()


#     @classmethod
#     def mutate(cls,root,info,id,payment_method,institute_id):
#         update_payment_m = PaymentMethod.objects.get(id=id)
#         update_payment_m.payment_method = payment_method
#         data = Institute.objects.get(id=institute_id)
#         update_payment_m.institute_id = data

#         update_payment_m.save()
#         return UpdatePaymentMethodMutation(update_payment_methd = update_payment_m)


class DeletePaymentMethodMutation(graphene.Mutation):
    delete_payment_method = graphene.Field(PaymentMethodType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_payment_method = PaymentMethod.objects.get(id=id)
        delete_payment_method.delete()

        return DeletePaymentMethodMutation(delete_payment_method=delete_payment_method)

#============================================================================================================================================================ payments mutation......================================================================

class CreatePaymentMutation(graphene.Mutation):
    payment = graphene.Field(PaymentType)

    class Arguments:
        institute_id= graphene.String()
        createdBy_id= graphene.String()
        training_id= graphene.String()
        payment_method_id= graphene.String()
        currency= graphene.String(required=True)
        amount= graphene.Float(required=True)

    def mutate(self,info,institute_id,createdBy_id,training_id,payment_method_id,currency,amount):
        payment_data = Payment(institute_id=institute_id,createdBy_id=createdBy_id,currency = currency,amount=amount)
        # pk1 = Institute.objects.get(id=institute_id)
        pk2 = Training.objects.get(id=training_id)
        pk3 = PaymentMethod.objects.get(id=payment_method_id)
        # payment_data.institute_id = pk1
        payment_data.training_id = pk2
        payment_data.payment_method_id = pk3

        payment_data.save()
        return CreatePaymentMutation(payment=payment_data)


# class UpdatePaymentMutation(graphene.Mutation):
#     update_payment = graphene.Field(PaymentType)

#     class Arguments:
#         id = graphene.ID()
#         institute_id= graphene.String()
#         training_id= graphene.String()
#         payment_method_id= graphene.String()
#         currency= graphene.String(required=True)
#         amount= graphene.Float(required=True)


#     @classmethod
#     def mutate(cls,root,info,id,institute_id,training_id,payment_method_id,currency,amount):
#         update_payment = Payment.objects.get(id=id)
#         update_payment.currency = currency
#         update_payment.amount = amount
#         pk1 = Institute.objects.get(id=institute_id)
#         pk2 = Training.objects.get(id=training_id)
#         pk3 = PaymentMethod.objects.get(id=payment_method_id)
#         update_payment.institute_id = pk1
#         update_payment.training_id = pk2
#         update_payment.payment_method_id = pk3

#         update_payment.save()
#         return UpdatePaymentMutation(update_payment = update_payment)


class DeletePaymentMutation(graphene.Mutation):
    delete_payment = graphene.Field(PaymentType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_payment = Payment.objects.get(id=id)
        delete_payment.delete()

        return DeletePaymentMutation(delete_payment=delete_payment)

"""
#============================================================================================================================================================ TrainingAttendance mutation......================================================================

class CreateTrainingAttendanceMutation(graphene.Mutation):
    create_training_attendance = graphene.Field(TrainingAttendanceType)

    class Arguments:
        institute_id = graphene.String(required=True)
        createdBy_id = graphene.String(required=True)
        training_id = graphene.String(required=True)

    def mutate(self,info,institute_id,createdBy_id,training_id,user_id):
        training_attendance_data = TrainingAttendance(
            institute_id=institute_id,
            createdBy_id=createdBy_id
        )
        pk2 = Training.objects.get(id=training_id)
        training_attendance_data.training_id = pk2

        training_attendance_data.save()
        return CreateTrainingAttendanceMutation(create_training_attendance=training_attendance_data)


# class UpdateTrainingAttendanceMutation(graphene.Mutation):
#     update_training_attendance = graphene.Field(TrainingAttendanceType)

#     class Arguments:
#         id = graphene.ID()
#         institute_id = graphene.String()
#         training_id = graphene.String()
#         user_id = graphene.String()


#     @classmethod
#     def mutate(cls,root,info,id,institute_id,training_id,user_id):
#         update_training_attendance = TrainingAttendance.objects.get(id=id)
#         pk1 = Institute.objects.get(id=institute_id)
#         pk2 = Training.objects.get(id=training_id)
#         pk3 = User.objects.get(id=user_id)
#         update_training_attendance.institute_id = pk1
#         update_training_attendance.training_id = pk2
#         update_training_attendance.user_id = pk3

#         update_training_attendance.save()
#         return UpdateTrainingAttendanceMutation(update_training_attendance = update_training_attendance)


class DeleteTrainingAttendanceMutation(graphene.Mutation):
    delete_training_attendance = graphene.Field(TrainingAttendanceType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_training_attendance = TrainingAttendance.objects.get(id=id)
        delete_training_attendance.delete()

        return DeleteTrainingAttendanceMutation(delete_training_attendance=delete_training_attendance)

#============================================================================================================================================================ venue mutation......================================================================
# class InstituteInput(graphene.InputObjectType):
#     id = graphene.ID(required=True)

# class RolesInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     description = graphene.String()


# class PermissionsInput(graphene.InputObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     description = graphene.String()

# class Role_PermissionsInput(graphene.InputObjectType):
#     id = graphene.ID()
#     roleId = graphene.ID()
#     permissionId = graphene.ID()

# class CreateRolePermission(graphene.Mutation):
#     class Arguments:
#         role_permission_data = Role_PermissionsInput(required=True)

#     role_permission = graphene.Field(RolePermissionsType)

#     @staticmethod
#     def mutate(root, info, role_permission_data=None):
#         role_permission_instance = RolePermissions(
#             role =role_permission_data.roleId,
#             permission=role_permission_data.permissionId,
#         )
#         role_permission_instance.save()
#         return CreateRolePermission(role_permission=role_permission_instance)



# class CreateVenueMutation(graphene.Mutation):
#     create_venue = graphene.Field(VenueType)

#     class Arguments:
#         # institute_id = graphene.String()
#         institutes_id = graphene.List(InstituteInput, required=True)
#         location_name = graphene.String(required=True)
#         capacity = graphene.Int(required=True)

#     def mutate(self,info,institutes_id,location_name,capacity):
#         create_venue = Venue(location_name=location_name,capacity=capacity)
#         create_venue.institute_id = Institute.objects.filter(pk__in=institutes_id)

#         create_venue.save()
#         return CreateVenueMutation(create_venue=create_venue)

class UpdateVenueMutation(graphene.Mutation):
    update_venue = graphene.Field(VenueType)

    class Arguments:
        id = graphene.ID()
        institute_id = graphene.String()
        location_name = graphene.String(required=True)
        capacity = graphene.Int(required=True)

    @classmethod
    def mutate(cls,root,info,id,institute_id,location_name,capacity):
        update_venue = Venue.objects.get(id=id)
        update_venue.location_name = location_name
        update_venue.capacity = capacity
        data = Institute.objects.get(id=institute_id)
        update_venue.institute_id = data

        update_venue.save()
        return UpdateVenueMutation(update_venue = update_venue)

class DeleteVenueMutation(graphene.Mutation):
    delete_venue = graphene.Field(VenueType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,rootull, info,id):
        delete_venue = Venue.objects.get(id=id)
        delete_venue.delete()

        return DeleteVenueMutation(delete_venue=delete_venue)

#============================================================================================================================================================ venueinstitute mutation......================================================================
class CreateVenueInstituteMutation(graphene.Mutation):
    instititute_venue = graphene.Field(VenueInstituteType)

    class Arguments:
        venue = graphene.String()
        institute = graphene.String()

    def mutate(self, info, **arg):
        venue = arg.get("venue")
        institute = arg.get("institute")
        instititute_venue_instance, created = VenueInstitute.objects.update_or_create(
            venue_id=venue,
            institute_id=institute,
        )
        return CreateVenueInstituteMutation(instititute_venue=instititute_venue_instance)

#============================================================================================================================================================ audiency mutation......================================================================
class CreateAudienceCategoryMutation(graphene.Mutation):
    create_audience_category = graphene.Field(AudienceCategoryType)

    class Arguments:
        institute_id = graphene.String()
        category_name = graphene.String(required=True)

    def mutate(self,info,institute_id,category_name):
        create_audience_category = AudienceCategory(category_name=category_name)
        data = Institute.objects.get(id=institute_id)
        create_audience_category.institute_id = data

        create_audience_category.save()
        return CreateAudienceCategoryMutation(create_audience_category=create_audience_category)

class UpdateAudienceCategoryMutation(graphene.Mutation):
    update_audience_category = graphene.Field(AudienceCategoryType)

    class Arguments:
        id = graphene.ID()
        institute_id = graphene.String()
        category_name = graphene.String(required=True)

    @classmethod
    def mutate(cls,root,info,id,institute_id,category_name):
        update_audience_category = AudienceCategory.objects.get(id=id)
        update_audience_category.category_name = category_name
        data = Institute.objects.get(id=institute_id)
        update_audience_caulltegory.institute_id = data

        update_audience_category.save()
        return UpdateAudienceCategoryMutation(update_audience_category = update_audience_category)

class DeleteAudienceCategoryMutation(graphene.Mutation):
    delete_audience_category = graphene.Field(AudienceCategoryType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_audience_category = AudienceCategory.objects.get(id=id)
        delete_audience_category.delete()

        return DeleteAudienceCategoryMutation(delete_audience_category=delete_audience_category)

#============================================================================================================================================================ Training mutation......================================================================
class CreateTrainingMutation(graphene.Mutation):
    create_training = graphene.Field(TrainingType)

    class Arguments:
        institute_id = graphene.String()
        venue_id = graphene.String()
        AudienceCategory_id = graphene.String()
        mode_of_delivery = graphene.Int(required=True)
        description = graphene.String(required=True)
        theme = graphene.String(required=True)
        cost = graphene.Float(required=True)
        topic = graphene.String(required=True)
        start_date = graphene.DateTime(required=True)
        end_date = graphene.DateTime(required=True)
        participant_limit = graphene.Int(required=True)
        status = graphene.Boolean(required=True)
        slots_remaining = graphene.Int(required=True)

    def mutate(self,info,institute_id,venue_id,AudienceCategory_id,mode_of_delivery,description,theme,cost,topic,start_date,end_date,participant_limit,status,slots_remaining):
        create_training = Training(mode_of_delivery=mode_of_delivery,description=description,theme=theme,cost=cost,topic=topic,start_date=start_date,end_date=end_date,participant_limit=participant_limit,status=status,slots_remaining=slots_remaining)
        data1 = Institute.objects.get(id=institute_id)
        data2 = Venue.objects.get(id=venue_id)
        data3 = AudienceCategory.objects.get(id=AudienceCategory_id)
        create_training.institute_id = data1
        create_training.venue_id = data2
        create_training.AudienceCategory_id = data3

        create_training.save()
        return CreateTrainingMutation(create_training=create_training)

class UpdateTrainingMutation(graphene.Mutation):
    update_training = graphene.Field(TrainingType)

    class Arguments:
        id = graphene.ID()
        institute_id = graphene.String()
        venue_id = graphene.String()
        AudienceCategory_id = graphene.String()
        mode_of_delivery = graphene.Int(required=True)
        description = graphene.String(required=True)
        theme = graphene.String(required=True)
        cost = graphene.Float(required=True)
        topic = graphene.String(required=True)
        start_date = graphene.DateTime(required=True)
        end_date = graphene.DateTime(required=True)
        participant_limit = graphene.Int(required=True)
        status = graphene.Boolean(required=True)
        slots_remaining = graphene.Int(required=True)

    @classmethod
    def mutate(cls,root,info,id,institute_id,venue_id,AudienceCategory_id,mode_of_delivery,description,theme,cost,topic,start_date,end_date,participant_limit,status,slots_remaining):
        update_training = Training.objects.get(id=id)

        update_training.mode_of_delivery = mode_of_delivery
        update_training.description = description
        update_training.theme = theme
        update_training.cost = cost
        update_training.topic = topic
        update_training.start_date = start_date
        update_training.end_date = end_date
        update_training.participant_limit = participant_limit
        update_training.status = status
        update_training.slots_remaining = slots_remaining

        data1 = Institute.objects.get(id=institute_id)
        data2 = Venue.objects.get(id=venue_id)
        data3 = AudienceCategory.objects.get(id=AudienceCategory_id)
        create_training.institute_id = data1
        create_training.venue_id = data2
        create_training.AudienceCategory_id = data3

        update_training.save()
        return UpdateTrainingMutation(update_training = update_training)

class DeleteTrainingMutation(graphene.Mutation):
    delete_training = graphene.Field(TrainingType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_training = Training.objects.get(id=id)
        delete_training.delete()

        return DeleteTrainingMutation(delete_training=delete_training)


#============================================================================================================================================================ TrainingApplication mutation......================================================================
class CreateTrainingApplicationMutation(graphene.Mutation):
    create_training = graphene.Field(TrainingApplicationType)

    class Arguments:
        institute_id = graphene.String()
        training_id = graphene.String()
        request_type = graphene.Int()
        participant_no = graphene.Int(required=True)
        # status_feedback = graphene.Int(required=True)

    def mutate(self,info,institute_id,training_id,request_type,participant_no):
        create_training = TrainingApplication(request_type=request_type,participant_no=participant_no)
        # status_feedback=status_feedback)
        data1 = Institute.objects.get(id=institute_id)
        data2 = Training.objects.get(id=training_id)
        create_training.institute_id = data1
        create_training.training_id = data2


        create_training.save()
        return CreateTrainingApplicationMutation(create_training=create_training)


class UpdateTrainingApplicationMutation(graphene.Mutation):
    update_training_application = graphene.Field(TrainingApplicationType)

    class Arguments:
        id = graphene.ID()
        institute_id = graphene.String()
        training_id = graphene.String()
        request_type = graphene.Int(required=True)
        participant_no = graphene.Int(required=True)
        status_feedback = graphene.Int(required=True)

    @classmethod
    def mutate(cls,root,info,id,institute_id,category_name):
        update_training_application = TrainingApplication.objects.get(id=id)
        update_training_application.request_type = request_type
        update_training_application.participant_no = participant_no
        update_training_application.status_feedback = status_feedback

        data1 = Institute.objects.get(id=institute_id)
        data2 = Training.objects.get(id=training_id)
        create_training.institute_id = data1
        create_training.training_id = data2

        create_training.save()
        return UpdateTrainingApplicationMutation(update_training_application = update_training_application)

class DeleteTrainingApplicationMutation(graphene.Mutation):
    delete_training_application = graphene.Field(TrainingApplicationType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls,root, info,id):
        delete_training_application = TrainingApplication.objects.get(id=id)
        delete_training_application.delete()

        return DeleteTrainingApplicationMutation(delete_training_application=delete_training_application)


#============================================================================================================================================================ General mutation class......================================================================
class DataMutation(graphene.ObjectType):

    # mutation for payment-method model
    CreatePaymentMethod = CreatePaymentMethodMutation.Field()
    updatePaymentMethod = UpdatePaymentMethodMutation.Field()
    deletePaymentMethod = DeletePaymentMethodMutation.Field()

    # mutation for payment model
    CreatePayment = CreatePaymentMutation.Field()
    updatePayment = UpdatePaymentMutation.Field()
    deletePayment = DeletePaymentMutation.Field()

    # mutation for training-attendancy
    createTrainingAttendance = CreateTrainingAttendanceMutation.Field()
    updateTrainingAttendance = UpdateTrainingAttendanceMutation.Field()
    deleteTrainingAttendance = DeleteTrainingAttendanceMutation.Field()

    # mutation for venue
    # createVenue = CreateVenueMutation.Field()
    updateVenue = UpdateVenueMutation.Field()
    deleteVenue = DeleteVenueMutation.Field()

    # mutation for venue
    createVenueInstitute = CreateVenueInstituteMutation.Field()

    # mutation for audiency-category
    createAudienceCategory= CreateAudienceCategoryMutation.Field()
    updateAudienceCategory= UpdateAudienceCategoryMutation.Field()
    deleteAudienceCategory= DeleteAudienceCategoryMutation.Field()

    # mutation for Training
    createTraining = CreateTrainingMutation.Field()
    UpdateTraining = UpdateTrainingMutation.Field()
    deleteTraining = DeleteTrainingMutation.Field()

    # mutation for TrainingApplication
    createTrainingApplication = CreateTrainingApplicationMutation.Field()
    updateTrainingApplication = UpdateTrainingApplicationMutation.Field()
    deleteTrainingApplication = DeleteTrainingApplicationMutation.Field()

"""

#============================================================================================================================================================ General mutation class......================================================================
class DataMutation(graphene.ObjectType):
    # mutation for payment-method model
    CreatePaymentMethod = CreatePaymentMethodMutation.Field()
    # updatePaymentMethod = UpdatePaymentMethodMutation.Field()
    deletePaymentMethod = DeletePaymentMethodMutation.Field()

    # mutation for payment model
    CreatePayment = CreatePaymentMutation.Field()
    # updatePayment = UpdatePaymentMutation.Field()
    deletePayment = DeletePaymentMutation.Field()


class DataQuery(graphene.ObjectType):
    all_payment_methods = graphene.List(PaymentMethodType)
    all_payments = graphene.List(PaymentType)
    all_training_attendance = graphene.List(TrainingAttendanceType)
    all_venues = graphene.List(VenueType)
    all_audience_category = graphene.List(AudienceCategoryType)
    all_training = graphene.List(TrainingType,)
    
    specific_training = graphene.List(TrainingType,id=graphene.String(),)
    single_training = graphene.List(TrainingType,id=graphene.String(),)
    all_training_application = graphene.List(TrainingApplicationType)
    applied_training_by_institute = graphene.List(TrainingApplicationType,id = graphene.String())

    # all_training = graphene.List(
    #     TrainingType,
    #     first=graphene.Int(),
    #     skip=graphene.Int()
    #     )

    def resolve_all_payment_methods(root,info):
        return PaymentMethod.objects.all()

    def resolve_all_payments(root,info):
        return Payment.objects.all()

    def resolve_all_training_attendance(root,info):
        return TrainingAttendance.objects.all()

    def resolve_all_venues(root,info):
        return Venue.objects.all()

    def resolve_all_audience_category(root,info):
        return  AudienceCategory.objects.all()

    def resolve_all_training(root,info,**kwargs):
        return  Training.objects.all()

    def resolve_specific_training(root,info,id,**kwargs):
        return  Training.objects.filter(institute_id=id)

    def resolve_single_training(root,info,id):
        return  Training.objects.filter(id=id)

    def resolve_all_training_application(root,info):
        return  TrainingApplication.objects.all()

    def resolve_applied_training_by_institute(root,info,id):
        return TrainingApplication.objects.filter(institute_id=id)

    # def resolve_specific_training(root,info,id,first=None,skip=None,**kwargs):

    #     s_tr = Training.objects.filter(institute_id=id)
    #     if skip:
    #         s_tr = s_tr[skip:]
    #     if first:
    #         s_tr = s_tr[:first]
    #     return  s_tr

class Mutation(DataMutation,graphene.ObjectType):
    pass

class Query(DataQuery,graphene.ObjectType):
    pass

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = build_schema(Query,Mutation)


#================================================================= =================================================================================PAYMENT =======================================================================================   regNo:"123344",
#     instituteAbbreviation:"pcm"){
#     institute{
#       id
#       instituteName
#       instituteLocation
#     }
#   }
#   }

# =============================================PAYMENT METHOD=========================================================================

# mutation{
#   CreatePaymentMethod(
#     paymentMethod:"Maduka",
#   	instituteId:"4b1ee0bb-e4be-4ba8-9e44-9926cc49a0b1"
#   ){
#     paymentMethod{
#       paymentMethod
#     }
#   }
#   }


# mutation{
#   updatePaymentMethod(
#     id:"f84c1b2a-6b88-4ec2-aedb-df0ec1f42cff",
#     instituteId:"9418d023-560a-4e9c-803f-a7a45def0541",
#     paymentMethod:"Njoo nikuage mamaye"
    
#   ){
#     updatePaymentMethd{
#          paymentMethod
#     }
#   }
# }



# mutation{
#   deletePaymentMethod(id:"f84c1b2a-6b88-4ec2-aedb-df0ec1f42cff")
#   {
#     deletePaymentMethod{
#       id
#     }
#   }
# }

#

#create venue======
# mutation{
#   updateTeam(
#     ...
#     groupsId: [{id: 1}, {id: 2}]
#   ) {
#     ...
#   }

