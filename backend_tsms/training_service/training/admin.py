from django.contrib import admin
from .models import Venue,AudienceCategory,Training,TrainingApplication,AudienceCategoryTraining


# Register your models here.
admin.site.register(Venue)
admin.site.register(AudienceCategory)
admin.site.register(Training)
admin.site.register(AudienceCategoryTraining)
admin.site.register(TrainingApplication)

