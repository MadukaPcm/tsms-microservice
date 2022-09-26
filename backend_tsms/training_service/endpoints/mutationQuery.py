import graphene
from graphene_django import DjangoObjectType
from graphene_federation import build_schema, extend, external,key

from payment.models import PaymentMethod,Payment
from report.models import TrainingAttendance
from training.models import Venue,AudienceCategory,Training,TrainingApplication



@extend(fields='id')
class TSMSUserObject(graphene.ObjectType):
    id=external(graphene.String(required=True))




class TSMSTrainingObject(graphene.ObjectType):
    id=graphene.String(required=True)
    training_unique_id=graphene.String(required=True)
    training_title=graphene.String(required=True)
    trainer=graphene.Field(TSMSUserObject)




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

    get_all_training_list = graphene.List(TSMSTrainingObject)

    def resolve_get_all_training_list(root,info,**kwargs):
        trainings=Training.objects.all()

        training_list=[]
        for training in trainings:
            training_list.append(TSMSTrainingObject(
                training.id,
                training.id,
                training.theme,
                TSMSUserObject(id=training.trainer)
            ))

        return training_list









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

